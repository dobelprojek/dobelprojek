# 📱 WhatsApp Number Tracker

Tool Python untuk melacak dan mendapatkan informasi nomor WhatsApp. Dibuat khusus untuk Termux.

## ✨ Fitur

- 🔍 Lacak informasi nomor WhatsApp
- 📊 Deteksi provider (Telkomsel, XL, Indosat, dll)
- 🔗 Generate link WhatsApp otomatis
- 📝 Support multiple nomor sekaligus
- 🎨 Interface CLI yang user-friendly
- 🇮🇩 Support format nomor Indonesia

## 📋 Persyaratan

- Termux
- Python 3.x
- Internet connection

## 🚀 Instalasi di Termux

### 1. Update & Install Python

```bash
pkg update && pkg upgrade
pkg install python
pkg install git
```

### 2. Clone atau Download Tool

```bash
# Jika menggunakan git
git clone <repository-url>
cd <folder-name>

# Atau buat manual
mkdir wa-tracker
cd wa-tracker
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Berikan Permission Execute

```bash
chmod +x wa_tracker.py
```

## 💻 Cara Penggunaan

### Menjalankan Tool

```bash
python wa_tracker.py
```

atau

```bash
./wa_tracker.py
```

### Menu Utama

Setelah menjalankan, Anda akan melihat menu:

```
📋 MENU:
   1. Lacak 1 Nomor
   2. Lacak Multiple Nomor
   3. Keluar
```

### 1. Lacak 1 Nomor

- Pilih menu `1`
- Masukkan nomor WhatsApp (format bebas)
- Contoh input:
  - `081234567890`
  - `+6281234567890`
  - `6281234567890`
  - `0812-3456-7890`

### 2. Lacak Multiple Nomor

- Pilih menu `2`
- Masukkan beberapa nomor dipisahkan koma
- Contoh: `081234567890, 082345678901, 085678901234`

## 📊 Informasi yang Ditampilkan

Tool ini akan menampilkan:

1. **Format Nomor**
   - Format internasional (+62xxx)
   - Format lokal (0xxx)

2. **Informasi Provider**
   - Deteksi operator (Telkomsel, XL, Indosat, dll)
   - Negara asal

3. **Link WhatsApp**
   - Link chat langsung
   - Link dengan pesan custom
   - API link

## 🎯 Contoh Output

```
==================================================
🔍 WHATSAPP NUMBER TRACKER
==================================================

📱 Nomor yang dicek: +6281234567890
⏰ Waktu: 2025-10-29 10:30:45

📊 INFORMASI NOMOR:
   • Format Internasional: +6281234567890
   • Format Lokal: 081234567890
   • Negara: Indonesia 🇮🇩
   • Provider: Telkomsel

🔗 LINK WHATSAPP:
   • Chat Langsung: https://wa.me/6281234567890
   • Chat dengan Pesan: https://wa.me/6281234567890?text=Halo
   • API Link: https://api.whatsapp.com/send?phone=6281234567890

==================================================
✅ Proses selesai!
==================================================
```

## 🔧 Tips Penggunaan

1. **Format Nomor Fleksibel**
   - Tool otomatis format nomor ke format internasional
   - Bisa input dengan/tanpa +62, 0, atau spasi

2. **Batch Processing**
   - Gunakan menu 2 untuk cek banyak nomor sekaligus
   - Hemat waktu untuk database nomor

3. **Copy Link**
   - Long press pada link untuk copy
   - Bisa langsung paste ke browser atau aplikasi lain

## ⚠️ Catatan Penting

- Tool ini hanya untuk informasi dan generate link WhatsApp
- Tidak melakukan scraping atau akses ilegal ke WhatsApp
- Gunakan dengan bijak dan bertanggung jawab
- Hormati privasi orang lain

## 🐛 Troubleshooting

### Error: Module 'requests' not found

```bash
pip install requests
```

### Error: Permission denied

```bash
chmod +x wa_tracker.py
```

### Python tidak ditemukan

```bash
pkg install python
```

## 📝 Lisensi

Tool ini gratis untuk digunakan dan dimodifikasi.

## 👨‍💻 Kontribusi

Silakan fork dan submit pull request untuk improvement!

## 📞 Support

Jika ada pertanyaan atau issue, silakan buat issue di repository.

---

**Dibuat dengan ❤️ untuk Termux Users**
