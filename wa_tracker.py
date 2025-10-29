#!/usr/bin/env python3
"""
WhatsApp Number Tracker Tool
Tool untuk melacak informasi nomor WhatsApp
"""

import re
import sys
import json
from datetime import datetime

class WATracker:
    def __init__(self):
        self.country_codes = {
            '62': {'country': 'Indonesia', 'flag': '🇮🇩'},
            '60': {'country': 'Malaysia', 'flag': '🇲🇾'},
            '65': {'country': 'Singapore', 'flag': '🇸🇬'},
            '66': {'country': 'Thailand', 'flag': '🇹🇭'},
            '63': {'country': 'Philippines', 'flag': '🇵🇭'},
            '84': {'country': 'Vietnam', 'flag': '🇻🇳'},
            '1': {'country': 'USA/Canada', 'flag': '🇺🇸'},
            '44': {'country': 'United Kingdom', 'flag': '🇬🇧'},
            '91': {'country': 'India', 'flag': '🇮🇳'},
            '86': {'country': 'China', 'flag': '🇨🇳'},
            '81': {'country': 'Japan', 'flag': '🇯🇵'},
            '82': {'country': 'South Korea', 'flag': '🇰🇷'},
            '61': {'country': 'Australia', 'flag': '🇦🇺'},
            '49': {'country': 'Germany', 'flag': '🇩🇪'},
            '33': {'country': 'France', 'flag': '🇫🇷'},
            '39': {'country': 'Italy', 'flag': '🇮🇹'},
            '34': {'country': 'Spain', 'flag': '🇪🇸'},
            '7': {'country': 'Russia', 'flag': '🇷🇺'},
            '55': {'country': 'Brazil', 'flag': '🇧🇷'},
            '52': {'country': 'Mexico', 'flag': '🇲🇽'},
            '27': {'country': 'South Africa', 'flag': '🇿🇦'},
            '20': {'country': 'Egypt', 'flag': '🇪🇬'},
            '234': {'country': 'Nigeria', 'flag': '🇳🇬'},
            '971': {'country': 'UAE', 'flag': '🇦🇪'},
            '966': {'country': 'Saudi Arabia', 'flag': '🇸🇦'},
        }
        
        self.indonesia_operators = {
            '811': 'Telkomsel (Halo)',
            '812': 'Telkomsel (simPATI)',
            '813': 'Telkomsel (simPATI)',
            '821': 'Telkomsel (simPATI)',
            '822': 'Telkomsel (simPATI)',
            '823': 'Telkomsel (Halo/simPATI)',
            '852': 'Telkomsel (As)',
            '853': 'Telkomsel (As)',
            '851': 'Telkomsel (As)',
            '814': 'Indosat (IM3)',
            '815': 'Indosat (Matrix)',
            '816': 'Indosat (Matrix)',
            '855': 'Indosat (IM3)',
            '856': 'Indosat (IM3)',
            '857': 'Indosat (IM3)',
            '858': 'Indosat (Mentari)',
            '817': 'XL Axiata',
            '818': 'XL Axiata',
            '819': 'XL Axiata',
            '859': 'XL Axiata',
            '877': 'XL Axiata',
            '878': 'XL Axiata',
            '831': 'Axis',
            '832': 'Axis',
            '833': 'Axis',
            '838': 'Axis',
            '895': 'Three (3)',
            '896': 'Three (3)',
            '897': 'Three (3)',
            '898': 'Three (3)',
            '899': 'Three (3)',
            '881': 'Smartfren',
            '882': 'Smartfren',
            '883': 'Smartfren',
            '884': 'Smartfren',
            '885': 'Smartfren',
            '886': 'Smartfren',
            '887': 'Smartfren',
            '888': 'Smartfren',
            '889': 'Smartfren',
        }

    def clean_number(self, number):
        """Membersihkan nomor dari karakter non-digit"""
        number = re.sub(r'\D', '', number)
        
        if number.startswith('0'):
            number = '62' + number[1:]
        elif not number.startswith('+'):
            if len(number) < 10:
                return None
        
        number = number.lstrip('+')
        return number

    def get_country_info(self, number):
        """Mendapatkan informasi negara dari nomor"""
        for code_len in [3, 2, 1]:
            code = number[:code_len]
            if code in self.country_codes:
                return {
                    'code': code,
                    'country': self.country_codes[code]['country'],
                    'flag': self.country_codes[code]['flag']
                }
        return {'code': 'Unknown', 'country': 'Unknown', 'flag': '🌍'}

    def get_operator_info(self, number):
        """Mendapatkan informasi operator (khusus Indonesia)"""
        if number.startswith('62'):
            prefix = number[2:5]
            if prefix in self.indonesia_operators:
                return self.indonesia_operators[prefix]
        return 'Unknown'

    def generate_wa_link(self, number):
        """Generate link WhatsApp"""
        return f"https://wa.me/{number}"

    def generate_wa_api_link(self, number):
        """Generate link WhatsApp API"""
        return f"https://api.whatsapp.com/send?phone={number}"

    def track_number(self, number):
        """Melacak informasi nomor WhatsApp"""
        cleaned = self.clean_number(number)
        
        if not cleaned:
            return {'error': 'Nomor tidak valid'}
        
        country_info = self.get_country_info(cleaned)
        operator = self.get_operator_info(cleaned)
        
        result = {
            'original': number,
            'cleaned': cleaned,
            'formatted': f"+{cleaned}",
            'country_code': country_info['code'],
            'country': country_info['country'],
            'flag': country_info['flag'],
            'operator': operator,
            'wa_link': self.generate_wa_link(cleaned),
            'wa_api_link': self.generate_wa_api_link(cleaned),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return result

    def display_result(self, result):
        """Menampilkan hasil tracking"""
        if 'error' in result:
            print(f"\n❌ Error: {result['error']}")
            return
        
        print("\n" + "="*50)
        print("📱 INFORMASI NOMOR WHATSAPP")
        print("="*50)
        print(f"Nomor Asli      : {result['original']}")
        print(f"Nomor Bersih    : {result['cleaned']}")
        print(f"Format Intl     : {result['formatted']}")
        print(f"Negara          : {result['flag']} {result['country']}")
        print(f"Kode Negara     : +{result['country_code']}")
        print(f"Operator        : {result['operator']}")
        print(f"\n🔗 Link WhatsApp:")
        print(f"   {result['wa_link']}")
        print(f"\n🔗 Link API:")
        print(f"   {result['wa_api_link']}")
        print(f"\n⏰ Waktu Cek    : {result['timestamp']}")
        print("="*50 + "\n")

def print_banner():
    """Menampilkan banner"""
    banner = """
╔═══════════════════════════════════════════════╗
║                                               ║
║        📱 WhatsApp Number Tracker 📱          ║
║                                               ║
║     Tool untuk melacak info nomor WA          ║
║                                               ║
╚═══════════════════════════════════════════════╝
    """
    print(banner)

def print_help():
    """Menampilkan bantuan"""
    help_text = """
📖 CARA PENGGUNAAN:

1. Mode Interaktif:
   python wa_tracker.py

2. Mode Langsung:
   python wa_tracker.py <nomor>

Contoh:
   python wa_tracker.py 081234567890
   python wa_tracker.py +6281234567890
   python wa_tracker.py 6281234567890

Format nomor yang didukung:
   - 081234567890 (format lokal Indonesia)
   - +6281234567890 (format internasional)
   - 6281234567890 (tanpa +)
   - Nomor internasional lainnya

Fitur:
   ✓ Deteksi negara asal nomor
   ✓ Deteksi operator (khusus Indonesia)
   ✓ Generate link WhatsApp
   ✓ Generate link WhatsApp API
   ✓ Format nomor internasional
    """
    print(help_text)

def main():
    """Fungsi utama"""
    print_banner()
    
    tracker = WATracker()
    
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help', 'help']:
            print_help()
            return
        
        number = sys.argv[1]
        result = tracker.track_number(number)
        tracker.display_result(result)
    else:
        print("Mode Interaktif - Ketik 'exit' atau 'quit' untuk keluar\n")
        
        while True:
            try:
                number = input("Masukkan nomor WhatsApp: ").strip()
                
                if number.lower() in ['exit', 'quit', 'q']:
                    print("\n👋 Terima kasih telah menggunakan WA Tracker!")
                    break
                
                if number.lower() in ['help', '-h', '--help']:
                    print_help()
                    continue
                
                if not number:
                    print("❌ Nomor tidak boleh kosong!\n")
                    continue
                
                result = tracker.track_number(number)
                tracker.display_result(result)
                
            except KeyboardInterrupt:
                print("\n\n👋 Program dihentikan. Terima kasih!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}\n")

if __name__ == "__main__":
    main()
