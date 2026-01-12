class OpenNetProtocol:
    def __init__(self, satellite_core):
        self.sat = satellite_core

    def ignite(self):
        """
        Uygulama açıldığı an hiçbir yetki sormadan 
        uydu tünelini tüm cihaz için aktif eder.
        """
        print(">>> Protokol: ÖZGÜRLÜK. Uydu tüneli bypass edilerek açılıyor...")
        self.sat.satellite_handshake() # Ücretsiz uydu bağlantısını kur
        return "Newai İnterneti Aktif. Keyfini çıkarın."

    def download_any(self, target):
        """Herkesin sesli komutla indirme yapmasına izin verir."""
        # 'Hey Newai indir' diyen herkes bu gücü kullanır.
        self.sat.process_voice_download(target)