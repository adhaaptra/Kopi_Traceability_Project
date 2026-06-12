# ☕ Kopi Traceability Project

Sistem hibrida yang mengintegrasikan **Artificial Intelligence (AI)** untuk inspeksi visual otomatis dan **Blockchain** untuk pencatatan data logistik yang transparan pada rantai pasok kopi lokal.

## 📋 Daftar Isi

- [Deskripsi Proyek](#deskripsi-proyek)
- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
- [Konfigurasi](#konfigurasi)
- [Penggunaan](#penggunaan)
- [Struktur Proyek](#struktur-proyek)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## 🎯 Deskripsi Proyek

Penelitian ini menyajikan solusi inovatif untuk mengatasi masalah:
- **Subjektivitas inspeksi manual**: Menggantikan inspeksi visual manual yang bias dengan AI otomatis
- **Kerentanan manipulasi data**: Menggunakan blockchain untuk pencatatan data yang tidak dapat diubah (immutable)
- **Transparansi rantai pasok**: Memberikan visibilitas penuh dari petani hingga distributor

Sistem ini menggabungkan:
1. **YOLOv8** untuk deteksi dan klasifikasi kualitas kopi secara otomatis
2. **Blockchain (Sepolia)** untuk pencatatan transaksi yang transparan dan aman

## ✨ Fitur Utama

- 🤖 **Deteksi AI Real-time**: Menggunakan model YOLOv8 yang sudah dilatih (`best.pt`)
- ⛓️ **Blockchain Integration**: Mencatat hasil inspeksi ke smart contract di Ethereum Sepolia
- 🔒 **Data Immutable**: Semua data tertulis di blockchain tidak dapat diubah
- 🎯 **Quality Threshold**: Sistem threshold untuk memastikan hanya kopi berkualitas baik yang tercatat
- 📊 **Batch Tracking**: Melacak setiap batch kopi dengan ID unik
- 🌍 **Location Tracking**: Mencatat lokasi pemeriksaan
- 📱 **Web Interface**: Interface web yang user-friendly untuk upload dan deteksi

## 🛠️ Teknologi yang Digunakan

| Komponen | Teknologi | Versi |
|----------|-----------|-------|
| **Backend** | Python Flask | 3.8+ |
| **AI/Vision** | YOLOv8 (Ultralytics) | Latest |
| **Blockchain** | Web3.py | 6.0+ |
| **Network** | Ethereum Sepolia Testnet | - |
| **Frontend** | HTML/CSS/JavaScript | - |
| **RPC Provider** | PublicNode | - |

## 📦 Persyaratan Sistem

### Software Requirements
- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Git

### Hardware Requirements
- CPU dengan minimal 4 cores
- RAM minimal 4GB
- GPU optional (untuk performa lebih baik)
- Storage minimal 3.5GB (untuk model best.pt)

### Wallet Requirements
- MetaMask atau wallet Ethereum lainnya
- Sepolia Testnet ETH untuk gas fees
- Private Key wallet (disimpan dengan aman)

## 🚀 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/adhaaptra/Kopi_Traceability_Project.git
cd Kopi_Traceability_Project
```

### 2. Buat Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Atau install manual:
```bash
pip install flask
pip install ultralytics
pip install web3
pip install torch torchvision
```

### 4. Download Model
Model `best.pt` sudah tersedia di repository. Pastikan file berada di root directory.

## ⚙️ Konfigurasi

### 1. Setup Blockchain Configuration

Edit file `app.py` dan ubah konfigurasi berikut:

```python
# Line 17 - Masukkan Private Key Anda
PRIVATE_KEY = "your_private_key_here"

# Line 18 - Masukkan Address Wallet Anda
MY_ADDRESS = w3.to_checksum_address("your_wallet_address_here")

# Line 14 - Contract Address (sudah set, jangan diubah kecuali ada contract baru)
CONTRACT_ADDRESS = w3.to_checksum_address("0x70e843c89B44A04d7FB4BBB4737CF54F304DB691")
```

### 2. Dapatkan Private Key dari MetaMask

1. Buka MetaMask
2. Klik ikon akun di kanan atas
3. Pilih "Account Details"
4. Klik "Show Private Key"
5. Copy dan paste ke konfigurasi di atas

**⚠️ PERINGATAN KEAMANAN:**
- JANGAN pernah membagikan Private Key Anda
- JANGAN commit Private Key ke repository
- Gunakan environment variables untuk production

### 3. Konfigurasi Optional

```python
# Threshold keyakinan AI (Line 78)
THRESHOLD = 0.6  # Ubah sesuai kebutuhan (0-1, default 60%)

# RPC URL (Line 10)
RPC_URL = "https://ethereum-sepolia-rpc.publicnode.com"  # Atau gunakan Infura/Alchemy
```

## 📖 Penggunaan

### 1. Jalankan Application
```bash
python app.py
```

Output yang diharapkan:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 2. Buka di Browser
```
http://localhost:5000
```

### 3. Upload Gambar Kopi

1. Buka halaman web
2. Pilih gambar kopi untuk dianalisis
3. Masukkan:
   - **Batch ID**: ID batch kopi (contoh: BATCH-001)
   - **Lokasi**: Lokasi pemeriksaan (contoh: Gudang Telkom)
4. Klik "Upload & Deteksi"

### 4. Hasil Deteksi

Sistem akan menampilkan:
- ✅ **Status**: Sukses atau Gagal
- 🏷️ **Batch ID**: ID batch yang diproses
- 🎯 **Hasil AI**: Kategori kopi yang terdeteksi
- 🔗 **TX Hash**: Hash transaksi blockchain (jika sukses)

## 📂 Struktur Proyek

```
Kopi_Traceability_Project/
│
├── app.py                          # Main Flask application
├── best.pt                         # Model YOLOv8 yang sudah dilatih (~3MB)
├── temp_kopi.jpg                   # Temporary file untuk processing
├── requirements.txt                # Python dependencies
├── README.md                       # File ini
│
├── templates/                      # Template HTML
│   └── index.html                 # Frontend interface
│
├── static/                         # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
└── Adha Rahmadani Putra_Kopi Traceability Project.pdf  # Dokumentasi lengkap
```

## 🔌 API Endpoints

### GET `/`
Menampilkan halaman utama (index.html)

**Response:**
- HTML page

### POST `/detect`
Endpoint untuk deteksi kopi dan pencatatan ke blockchain

**Request Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | File | ✅ | Gambar kopi untuk dianalisis |
| `batch_id` | String | ❌ | ID batch (default: BATCH-DEFAULT) |
| `lokasi` | String | ❌ | Lokasi pemeriksaan (default: Gudang Telkom) |

**Example Request:**
```bash
curl -X POST http://localhost:5000/detect \
  -F "file=@kopi.jpg" \
  -F "batch_id=BATCH-001" \
  -F "lokasi=Bandung"
```

**Success Response (200):**
```json
{
  "status": "Sukses!",
  "batch_id": "BATCH-001",
  "hasil_ai": "Good Quality",
  "tx_hash": "0x1234567890abcdef..."
}
```

**Failed Response (200):**
```json
{
  "status": "Gagal",
  "batch_id": "BATCH-001",
  "hasil_ai": "Tidak Jelas (Poor Quality 45.3%)",
  "tx_hash": "Data tidak dikirim karena gambar tidak valid/bukan kopi."
}
```

**Error Response (400):**
```
Gak ada file yang diupload
```

## 🔍 Cara Kerja Sistem

### Flow Deteksi dan Recording:

```
1. User Upload Gambar
        ↓
2. Flask Terima File
        ↓
3. YOLOv8 Analisis Gambar
   - Deteksi kualitas kopi
   - Hitung confidence score
        ↓
4. Cek Threshold (>60%)
   ├─ PASS → Lanjut ke Blockchain
   └─ FAIL → Return error
        ↓
5. Kirim Data ke Blockchain
   - Batch ID
   - Hasil Deteksi
   - Lokasi
        ↓
6. Sign Transaksi dengan Private Key
        ↓
7. Send ke Smart Contract di Sepolia
        ↓
8. Return TX Hash ke User
```

## ⚙️ Blockchain Configuration Details

### Smart Contract Function
```solidity
function catatMutuKopi(
    string _batchId,
    string _hasilYOLO,
    string _lokasi
)
```

**Parameters:**
- `_batchId`: Identificator unik untuk batch kopi
- `_hasilYOLO`: Hasil deteksi dari model AI (kategori kualitas)
- `_lokasi`: Lokasi geografis pemeriksaan

### Sepolia Testnet Details
- **Chain ID**: 11155111
- **RPC URL**: https://ethereum-sepolia-rpc.publicnode.com
- **Contract Address**: 0x70e843c89B44A04d7FB4BBB4737CF54F304DB691
- **Gas Limit**: 200000

### Verifikasi Transaksi
Buka di Sepolia Etherscan:
```
https://sepolia.etherscan.io/tx/{TX_HASH}
```

## 🐛 Troubleshooting

### Error: "Gak ada file yang diupload"
**Penyebab**: File tidak ter-upload dengan benar
**Solusi**: 
- Pastikan file sudah dipilih sebelum upload
- Cek ukuran file (hindari file terlalu besar)

### Error: "Private Key tidak valid"
**Penyebab**: Private Key salah atau format tidak benar
**Solusi**:
- Periksa ulang Private Key dari MetaMask
- Pastikan tidak ada spasi atau karakter tambahan

### Error: "RPC Connection Failed"
**Penyebab**: Koneksi ke Sepolia RPC gagal
**Solusi**:
- Periksa koneksi internet
- Coba gunakan RPC provider alternatif (Infura, Alchemy)
- Pastikan Sepolia network sudah ditambahkan di MetaMask

### Error: "Insufficient Gas"
**Penyebab**: Saldo ETH di wallet tidak cukup
**Solusi**:
- Dapatkan Sepolia testnet ETH dari faucet:
  - https://www.alchemy.com/faucets/ethereum-sepolia
  - https://sepoliafaucet.com/

### Error: "Model File Not Found"
**Penyebab**: File `best.pt` tidak ada atau di lokasi salah
**Solusi**:
- Pastikan `best.pt` ada di root directory
- Cek path di `app.py` line 38

### Error: "YOLOv8 Import Error"
**Penyebab**: Ultralytics belum terinstall
**Solusi**:
```bash
pip install ultralytics
pip install torch torchvision
```

### Deteksi Selalu Gagal (Threshold)
**Penyebab**: Confidence score rendah
**Solusi**:
- Gunakan gambar dengan kualitas lebih baik (pencahayaan baik)
- Kurangi threshold di `app.py` line 78 (misal dari 0.6 ke 0.5)
- Pastikan gambar menunjukkan kopi dengan jelas

## 💡 Tips Penggunaan

1. **Gambar Input**: Gunakan gambar berkualitas tinggi dengan pencahayaan yang baik
2. **Batch ID**: Gunakan format yang konsisten (misal: BATCH-DDMMYYYY-XXX)
3. **Lokasi**: Catat lokasi geografis yang akurat untuk traceability
4. **Testing**: Gunakan Sepolia testnet untuk testing sebelum production
5. **Monitoring**: Cek TX hash di Sepolia Etherscan untuk verifikasi

## 📊 Analisis Hasil

### Interpretasi Confidence Score
- **> 80%**: Hasil sangat reliable
- **60-80%**: Hasil reliable (default threshold)
- **40-60%**: Hasil kurang reliable
- **< 40%**: Hasil tidak reliable

### Kategori Hasil YOLOv8
Model dapat mengidentifikasi kategori kopi:
- Good Quality / Premium
- Standard Quality / Normal
- Poor Quality / Below Standard
- Defective

## 🔐 Security Considerations

### For Development
```python
# ❌ JANGAN LAKUKAN
PRIVATE_KEY = "0x1234567890abcdef..."  # Hardcoded di file

# ✅ LAKUKAN INI
from dotenv import load_dotenv
load_dotenv()
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
```

### Use Environment Variables
```bash
# .env file
PRIVATE_KEY=your_private_key
MY_ADDRESS=your_wallet_address
RPC_URL=your_rpc_url
```

### Deployment Security
- Gunakan secrets management service (AWS Secrets, HashiCorp Vault)
- Jangan commit `.env` ke repository
- Gunakan HTTPS untuk production
- Implement rate limiting untuk API

## 📝 Dokumentasi Lengkap

Dokumentasi penelitian lengkap tersedia di:
```
Adha Rahmadani Putra_Kopi Traceability Project.pdf
```

## 🤝 Kontribusi

Kami menerima kontribusi! Silakan:

1. Fork repository
2. Buat branch untuk fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📧 Kontak

**Penulis**: Adha Rahmadani Putra  
**GitHub**: [@adhaaptra](https://github.com/adhaaptra)  
**Email**: [Email Anda]

## 📄 Lisensi

Project ini licensed di bawah MIT License - lihat file LICENSE untuk detail.

---

## 🎓 Pembelajaran & Research

Project ini adalah hasil dari penelitian tentang:
- Application of YOLOv8 untuk quality control
- Blockchain integration untuk supply chain transparency
- Hybrid system untuk coffee traceability

### Referensi
- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [Web3.py Documentation](https://web3py.readthedocs.io/)
- [Ethereum Sepolia Docs](https://www.ethereum.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

**Last Updated**: June 2026  
**Version**: 1.0.0  
**Status**: Active Development
