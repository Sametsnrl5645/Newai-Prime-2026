import os
import shutil

class PhoenixRecovery:
    def __init__(self, brain):
        self.brain = brain
        # Dosyaların kuantum yedeğinin tutulduğu gizli bulut dizini
        self.shadow_cloud_path = "newai_prime_cloud/shadow_backups/"

    def auto_save_shadow(self, file_path):
        """Her kritik dosyanın anında bir gölge kopyasını buluta yükler."""
        # Dosya yerelde silinse bile bulutta mühürlü kalır
        self.brain.cloud.upload_to_infinite_storage(file_path, is_shadow=True)

    def recover_all_systems(self):
        """Tehlike geçtiğinde tüm sistemi ve dosyaları saniyeler içinde geri yükler."""
        print(">>> ANKA KUŞU PROTOKOLÜ: Dosyalar kurtarılıyor...")
        
        # 1. Buluttaki gölge kopyaları çek
        recovered_files = self.brain.cloud.download_all_shadows()
        
        # 2. Sistem dosyalarını orijinal yerlerine yerleştir
        for file in recovered_files:
            shutil.copy(file['cloud_path'], file['local_path'])
            
        print(">>> RECOVERY TAMAMLANDI: Newai Prime eski gücüne kavuştu.")
        return True

    def detect_attack_and_protect(self):
        """Sisteme bir müdahale (silme denemesi) algıladığında dosyaları kilitler."""
        # Eğer yetkisiz biri dosyaları silmeye çalışırsa, Newai dosyaları 
        # anında buluta 'sharding' (parçalayarak) gönderir ve yereli temizler.
        pass