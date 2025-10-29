# 📱 Cara Install WhatsApp Number Tracker di Termux

## 🚀 Instalasi di Termux

### Langkah 1: Update & Install Python
```bash
# Update package list
pkg update && pkg upgrade

# Install Python
pkg install python

# Cek versi Python (harus 3.6+)
python --version
```

### Langkah 2: Install Git (Opsional)
```bash
pkg install git
```

### Langkah 3: Download Tool

**Opsi A: Jika punya Git**
```bash
# Clone repository (sesuaikan dengan repo Anda)
git clone <url-repository>
cd <nama-folder>
```

**Opsi B: Manual Download**
```bash
# Buat folder untuk tool
mkdir wa-tracker
cd wa-tracker

# Download file wa_tracker.py
# (copy paste kode atau download dari browser)
```

### Langkah 4: Berikan Permission
```bash
chmod +x wa_tracker.py
```

### Langkah 5: Jalankan Tool
```bash
# Mode interaktif
python wa_tracker.py

# Mode langsung dengan nomor
python wa_tracker.py 081234567890
```

---

## 📖 Cara Penggunaan

### Mode Interaktif
```bash
python wa_tracker.py
```
Kemudian masukkan nomor WhatsApp saat diminta.

### Mode Langsung
```bash
# Format lokal Indonesia
python wa_tracker.py 081234567890

# Format internasional
python wa_tracker.py +6281234567890

# Tanpa tanda +
python wa_tracker.py 6281234567890

# Nomor luar negeri
python wa_tracker.py +60123456789
```

### Perintah Bantuan
```bash
python wa_tracker.py --help
```

---

## ✨ Fitur Tool

✅ **Deteksi Negara** - Mendeteksi negara asal nomor dari kode negara  
✅ **Deteksi Operator** - Mendeteksi operator seluler (khusus Indonesia)  
✅ **Format Nomor** - Memformat nomor ke format internasional  
✅ **Generate Link WA** - Membuat link WhatsApp langsung  
✅ **Generate Link API** - Membuat link WhatsApp API  
✅ **Multi Format** - Mendukung berbagai format input nomor  

---

## 🌍 Negara yang Didukung

- 🇮🇩 Indonesia
- 🇲🇾 Malaysia
- 🇸🇬 Singapore
- 🇹🇭 Thailand
- 🇵🇭 Philippines
- 🇻🇳 Vietnam
- 🇺🇸 USA/Canada
- 🇬🇧 United Kingdom
- 🇮🇳 India
- 🇨🇳 China
- 🇯🇵 Japan
- 🇰🇷 South Korea
- 🇦🇺 Australia
- Dan banyak lagi...

---

## 📱 Operator Indonesia yang Didukung

- **Telkomsel** (Halo, simPATI, As)
- **Indosat** (IM3, Matrix, Mentari)
- **XL Axiata**
- **Axis**
- **Three (3)**
- **Smartfren**

---

## 🔧 Troubleshooting

### Error: Python tidak ditemukan
```bash
pkg install python
```

### Error: Permission denied
```bash
chmod +x wa_tracker.py
```

### Error: Module tidak ditemukan
Tool ini hanya menggunakan library standar Python, tidak perlu install package tambahan.

---

## 💡 Tips Penggunaan

1. **Simpan Alias** untuk akses cepat:
   ```bash
   echo "alias watrack='python ~/wa-tracker/wa_tracker.py'" >> ~/.bashrc
   source ~/.bashrc
   
   # Sekarang bisa langsung:
   watrack 081234567890
   ```

2. **Buat Shortcut** di home directory:
   ```bash
   ln -s ~/wa-tracker/wa_tracker.py ~/watrack.py
   
   # Jalankan dari mana saja:
   python ~/watrack.py 081234567890
   ```

3. **Batch Processing** - Cek banyak nomor sekaligus:
   ```bash
   # Buat file numbers.txt berisi list nomor
   # Kemudian:
   while read number; do python wa_tracker.py "$number"; done < numbers.txt
   ```

---

## 📝 Contoh Output

```
╔═══════════════════════════════════════════════╗
║                                               ║
║        📱 WhatsApp Number Tracker 📱          ║
║                                               ║
║     Tool untuk melacak info nomor WA          ║
║                                               ║
╚═══════════════════════════════════════════════╝

==================================================
📱 INFORMASI NOMOR WHATSAPP
==================================================
Nomor Asli      : 081234567890
Nomor Bersih    : 6281234567890
Format Intl     : +6281234567890
Negara          : 🇮🇩 Indonesia
Kode Negara     : +62
Operator        : Telkomsel (simPATI)

🔗 Link WhatsApp:
   https://wa.me/6281234567890

🔗 Link API:
   https://api.whatsapp.com/send?phone=6281234567890

⏰ Waktu Cek    : 2025-10-29 10:30:45
==================================================
```

---

## 🆘 Bantuan

Jika ada masalah atau pertanyaan:
1. Jalankan: `python wa_tracker.py --help`
2. Pastikan Python versi 3.6 atau lebih baru
3. Pastikan file wa_tracker.py ada di folder yang benar

---

## 📄 Lisensi

Tool ini gratis untuk digunakan dan dimodifikasi.

---

**Selamat menggunakan! 🎉**
