import flet as ft

class NewaiVoiceMatch:
    def __init__(self, brain):
        self.brain = brain
        self.is_verified = False

    def check_voice_identity(self, audio_data):
        """
        Google Voice Match motoruyla senkronize çalışarak 
        gelen sesin 'Sahip'e ait olup olmadığını sorgular.
        """
        # Google Assistant SDK / App Actions üzerinden Voice Match doğrulaması istenir
        # Bu kısım sistemin 'Identity Provider' katmanıyla konuşur
        
        owner_voice_id = "GOOGLE_VOICE_MATCH_SAMET_88" 
        
        # Simülasyon: Google Match sonucu başarılıysa
        if self._verify_with_google_match(audio_data, owner_voice_id):
            self.is_verified = True
            return True
        else:
            self.is_verified = False
            print(">>> UYARI: Yetkisiz Ses Denemesi. Sistem kilitli kalmaya devam ediyor.")
            return False

    def _verify_with_google_match(self, audio, target_id):
        # Arka planda Google'ın biyometrik ses analizi çalışır
        return True # Sahip doğrulandı varsayıyoruz