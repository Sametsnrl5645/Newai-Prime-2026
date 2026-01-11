import threading
import time
from core.brain_core import NewaiBrainCore

class NewaiLiveEngine:
    def __init__(self, brain: NewaiBrainCore):
        self.brain = brain
        self.is_running = False
        self.interrupted = False # Senin araya girip girmediğini kontrol eder

    def start_session(self):
        """Canlı oturumu başlatır."""
        print(">> Newai Live Aktif. Sahip, seni dinliyorum.")
        self.is_running = True
        # Dinleme ve konuşma döngüsünü ayrı bir thread'de başlatıyoruz
        threading.Thread(target=self._live_loop, daemon=True).start()

    def _live_loop(self):
        while self.is_running:
            # 1. SESİ YAKALA (Sessizlik algılanana kadar dinle)
            # Burada sistemin mikrofonu aktif edilir
            user_speech = self._listen_mic() 
            
            if user_speech:
                # 2. GROQ İLE ANALİZ ET (En hızlı Llama-3-8B modeli ile)
                # Live modunda gecikme olmaması için model_set'teki LIVE_MODEL kullanılır
                response = self.brain.cevap_uret(user_speech, mod="hizli")
                
                # 3. SESLİ CEVAP VER (Konuşurken senin sesini duyarsa anında susar)
                self._speak(response)
            
            time.sleep(0.1)

    def _listen_mic(self):
        """Mikrofonu dinler ve sesi metne çevirir (Whisper-Groq)."""
        # Burada Groq'un whisper-large-v3 modeli ile ses deşifre edilir
        pass

    def _speak(self, text):
        """Newai'nin sesi. Senin sesini duyduğu an 'self.interrupted' True olur ve susar."""
        # TTS (Text-to-Speech) motoru burada devreye girer
        pass

    def stop_session(self):
        """Oturumu sonlandırır."""
        self.is_running = False
        print(">> Newai Live Kapatıldı.")