#!/usr/bin/env python3
"""
WhatsApp Number Tracker
Tool untuk melacak informasi nomor WhatsApp
"""

import requests
import json
import sys
from datetime import datetime

class WATracker:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def format_number(self, number):
        """Format nomor telepon ke format internasional"""
        # Hapus karakter non-digit
        number = ''.join(filter(str.isdigit, number))
        
        # Jika dimulai dengan 0, ganti dengan 62 (Indonesia)
        if number.startswith('0'):
            number = '62' + number[1:]
        # Jika tidak dimulai dengan +, tambahkan 62
        elif not number.startswith('62'):
            number = '62' + number
            
        return number
    
    def check_whatsapp(self, number):
        """Cek apakah nomor terdaftar di WhatsApp"""
        formatted_number = self.format_number(number)
        
        print(f"\n{'='*50}")
        print(f"🔍 WHATSAPP NUMBER TRACKER")
        print(f"{'='*50}")
        print(f"\n📱 Nomor yang dicek: +{formatted_number}")
        print(f"⏰ Waktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Informasi dasar nomor
        self.display_number_info(formatted_number)
        
        # Link WhatsApp
        self.display_wa_links(formatted_number)
        
        print(f"\n{'='*50}")
        print("✅ Proses selesai!")
        print(f"{'='*50}\n")
    
    def display_number_info(self, number):
        """Tampilkan informasi nomor"""
        print(f"\n📊 INFORMASI NOMOR:")
        print(f"   • Format Internasional: +{number}")
        print(f"   • Format Lokal: 0{number[2:]}")
        
        # Deteksi negara berdasarkan kode
        if number.startswith('62'):
            country = "Indonesia 🇮🇩"
            if number[2:4] in ['81', '82', '83', '85', '87', '88', '89']:
                provider = "Telkomsel"
            elif number[2:4] in ['95', '96']:
                provider = "XL Axiata"
            elif number[2:4] in ['99']:
                provider = "Smartfren"
            elif number[2:4] in ['85', '86', '87']:
                provider = "Indosat/3"
            else:
                provider = "Unknown"
            
            print(f"   • Negara: {country}")
            print(f"   • Provider: {provider}")
        else:
            print(f"   • Negara: International")
    
    def display_wa_links(self, number):
        """Tampilkan link WhatsApp"""
        print(f"\n🔗 LINK WHATSAPP:")
        
        # Link chat langsung
        chat_link = f"https://wa.me/{number}"
        print(f"   • Chat Langsung: {chat_link}")
        
        # Link dengan pesan
        message_link = f"https://wa.me/{number}?text=Halo"
        print(f"   • Chat dengan Pesan: {message_link}")
        
        # Link API
        api_link = f"https://api.whatsapp.com/send?phone={number}"
        print(f"   • API Link: {api_link}")
    
    def batch_check(self, numbers):
        """Cek multiple nomor sekaligus"""
        print(f"\n🔄 Memproses {len(numbers)} nomor...\n")
        
        for i, number in enumerate(numbers, 1):
            print(f"\n[{i}/{len(numbers)}]")
            self.check_whatsapp(number)
            
            if i < len(numbers):
                input("\nTekan Enter untuk lanjut ke nomor berikutnya...")

def print_banner():
    """Tampilkan banner aplikasi"""
    banner = """
    ╔══════════════════════════════════════════╗
    ║     WhatsApp Number Tracker v1.0         ║
    ║     Tool untuk Termux                    ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)

def print_menu():
    """Tampilkan menu"""
    print("\n📋 MENU:")
    print("   1. Lacak 1 Nomor")
    print("   2. Lacak Multiple Nomor")
    print("   3. Keluar")
    print()

def main():
    """Fungsi utama"""
    print_banner()
    tracker = WATracker()
    
    while True:
        print_menu()
        choice = input("Pilih menu (1-3): ").strip()
        
        if choice == '1':
            number = input("\n📱 Masukkan nomor WhatsApp: ").strip()
            if number:
                tracker.check_whatsapp(number)
            else:
                print("❌ Nomor tidak boleh kosong!")
        
        elif choice == '2':
            print("\n📝 Masukkan nomor (pisahkan dengan koma):")
            numbers_input = input("Contoh: 081234567890, 082345678901\n> ").strip()
            
            if numbers_input:
                numbers = [n.strip() for n in numbers_input.split(',')]
                tracker.batch_check(numbers)
            else:
                print("❌ Input tidak valid!")
        
        elif choice == '3':
            print("\n👋 Terima kasih telah menggunakan WA Tracker!")
            print("   Dibuat dengan ❤️ untuk Termux\n")
            sys.exit(0)
        
        else:
            print("❌ Pilihan tidak valid! Pilih 1-3.")
        
        input("\nTekan Enter untuk kembali ke menu...")
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program dihentikan oleh user.")
        print("👋 Sampai jumpa!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
