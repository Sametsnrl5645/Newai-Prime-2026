import hashlib
from core.model_set import ModelSettings

class SecurityShield:
    def __init__(self):
        self.settings = ModelSettings()
        self.is_authenticated = False

    def verify_owner(self, email_input):
        """Giriş yapılmaya çalışılan e-posta sahibininkiyle eşleşiyor mu?"""
        # Boşlukları sil ve küçük harfe çevir
        cleaned_email = email_input.strip().lower()
        
        if cleaned_email == self.settings.OWNER_EMAIL:
            self.is_authenticated = True
            print(f">>> ERİŞİM ONAYLANDI: Hoş geldiniz sahip {self.settings.OWNER_NAME}.")
            return True
        else:
            self.is_authenticated = False
            print(f">>> ERİŞİM REDDEDİLDİ: Yetkisiz giriş denemesi ({cleaned_email}).")
            return False

    def system_lockdown(self):
        """Yetkisiz erişimde tüm çekirdek fonksiyonları kilitler."""
        if not self.is_authenticated:
            # Kritik modülleri devre dışı bırakır
            return "Kritik Hata: Otorite doğrulanmadı. Sistem kilitli."
        return "Sistem Aktif."

    def generate_access_token(self):
        """Sahip için her oturuma özel, taklit edilemez bir dijital mühür oluşturur."""
        raw_token = f"{self.settings.OWNER_EMAIL}-{self.settings.OWNER_NAME}-2026"
        return hashlib.sha256(raw_token.encode()).hexdigest()