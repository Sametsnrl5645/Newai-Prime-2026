class AccessController:
    def __init__(self, brain):
        self.brain = brain
        self.owner_voice_id = "Samet_Can_88"

    def authorize_user(self, session_voice_id):
        """Kullanıcının hangi seviyede internete erişeceğine karar verir."""
        
        if session_voice_id == self.owner_voice_id:
            # Sahip Girişi: Sınırsız Uydu, Tam Hız (4.2 GB/s), Geliştirme Yetkisi
            return "OWNER_FULL_ACCESS"
        
        elif self.is_guest_allowed():
            # Diğer Kullanıcılar: Standart Uydu İnterneti, Sınırlı Hız
            # Onlar da ücretsiz interneti kullanır ama sistemi değiştiremezler.
            return "USER_GUEST_ACCESS"
        
        else:
            return "ACCESS_DENIED"

    def is_guest_allowed(self):
        """Sahip, başkalarının interneti kullanmasına izin verdi mi?"""
        # Bu ayarı sadece sen Geliştirme Paneli'nden açıp kapatabilirsin.
        return self.brain.settings.get("GUEST_NET_ACCESS", True)