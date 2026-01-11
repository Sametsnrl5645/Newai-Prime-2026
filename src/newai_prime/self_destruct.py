import os
import shutil
import sys

class EmergencySystem:
    def __init__(self, brain):
        self.brain = brain
        self.trigger_code = "SH-88-DESTROY" # Sadece senin bildiğin gizli kod

    def activate_self_destruct(self, input_code):
        """Sistemi tamamen ve kalıcı olarak temizler."""
        if input_code == self.trigger_code:
            print(">>> KRİTİK PROTOKOL: Kendi kendini imha başlatıldı...")
            
            # 1. Uydu Tünellerini ve İnternet Sürücülerini Kapat
            self.brain.satellite.shutdown()
            
            # 2. Yerel Veri Tabanlarını ve Cache'i Sil
            if os.path.exists("db/"):
                shutil.rmtree("db/")
            
            # 3. Bulut Erişim Anahtarlarını İptal Et
            self.brain.cloud.logout_and_clear_keys()
            
            # 4. Uygulamayı Kapat ve Bir Daha Açılmasını Engelle
            print(">>> Newai Prime Uykuya Geçti. İzler silindi.")
            sys.exit()