import os
from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
from web3 import Web3

app = Flask(__name__)

# 1. SETTING BLOCKCHAIN (Sepolia)
# Ganti URL RPC ini jika kamu punya dari Infura/Alchemy, atau pakai yang publik ini
RPC_URL = "https://ethereum-sepolia-rpc.publicnode.com"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# DATA KONTRAK KAMU (Jangan diubah)
CONTRACT_ADDRESS = w3.to_checksum_address("0x70e843c89B44A04d7FB4BBB4737CF54F304DB691")
# Private Key wallet kamu (Buka MetaMask -> Account Details -> Show Private Key)
# PERINGATAN: Jangan sebarkan Private Key ini ke siapa pun!
PRIVATE_KEY = ""
MY_ADDRESS = w3.to_checksum_address("0x499D2497e214583f31fb46680f50Ee86B9f81631")

# ABI Sederhana (Hanya fungsi catatMutuKopi)
ABI = [
	{
		"inputs": [
			{"internalType": "string", "name": "_batchId", "type": "string"},
			{"internalType": "string", "name": "_hasilYOLO", "type": "string"},
			{"internalType": "string", "name": "_lokasi", "type": "string"}
		],
		"name": "catatMutuKopi",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

# 2. LOAD MODEL YOLOv8 KAMU
model = YOLO('best.pt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return "Gak ada file yang diupload", 400
    
    file = request.files['file']
    batch_id = request.form.get('batch_id', 'BATCH-DEFAULT')
    lokasi = request.form.get('lokasi', 'Gudang Telkom')
    
    # Simpan file sementara
    img_path = "temp_kopi.jpg"
    file.save(img_path)
    
# JALANKAN AI (best.pt)
    results = model(img_path)
    
    # Ambil label hasil deteksi paling tinggi dan tingkat keyakinannya
    probs = results[0].probs
    class_id = probs.top1
    hasil_deteksi = results[0].names[class_id]
    
    # Mengambil skor keyakinan (0.0 sampai 1.0)
    # Pastikan menggunakan atribut yang benar dari ultralytics (top1conf)
    conf = float(probs.top1conf) 

    # --- TAMBAHAN: PRINT KE TERMINAL (BIAR MUNCUL LAGI DI VS CODE) ---
    print("\n" + "=".center(40, "="))
    print(f"🔍 BATCH ID: {batch_id}")
    print(f"☕ HASIL DETEKSI: {hasil_deteksi}")
    print(f"🎯 CONFIDENCE: {conf*100:.2f}%")
    print("=".center(40, "=") + "\n")
    # ----------------------------------------------------------------

    # --- LOGIKA THRESHOLD (PAGAR KEAMANAN) ---
    THRESHOLD = 0.6  # Batas minimal 60% keyakinan
    
    if conf < THRESHOLD:
        return jsonify({
            "status": "Gagal",
            "batch_id": batch_id,
            "hasil_ai": f"Tidak Jelas ({hasil_deteksi} {conf*100:.1f}%)",
            "tx_hash": "Data tidak dikirim karena gambar tidak valid/bukan kopi."
        })
    # -----------------------------------------

    # KIRIM KE BLOCKCHAIN SEPOLIA (Hanya jalan jika lolos threshold di atas)
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    tx = contract.functions.catatMutuKopi(
        batch_id, 
        hasil_deteksi, 
        lokasi
    ).build_transaction({
        'chainId': 11155111, # ID Sepolia
        'gas': 200000,
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce,
    })
    
    # Tanda tangan transaksi
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    return jsonify({
        "status": "Sukses!",
        "batch_id": batch_id,
        "hasil_ai": hasil_deteksi,
        "tx_hash": w3.to_hex(tx_hash)
    })

if __name__ == '__main__':
    app.run(debug=True)