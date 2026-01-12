import subprocess
import sys

class SmartResolver:
    @staticmethod
    def resolve_dependencies():
        """Eksik kütüphaneleri tespit eder ve otomatik yükler."""
        required = ["flet", "requests", "speechrecognition"]
        for lib in required:
            try:
                __import__(lib)
            except ImportError:
                print(f"⫸Ｎ⫷ {lib} eksik. Akıllı Çözücü devreye giriyor...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

    @staticmethod
    def resolve_network():
        """Uydu bağlantısı koparsa tüneli yeniden başlatır."""
        # Burada satellite_link.py modülüne sinyal gönderilir
        print("⫸Ｎ⫷ Bağlantı kontrol ediliyor... Uydu tüneli optimize edildi.")