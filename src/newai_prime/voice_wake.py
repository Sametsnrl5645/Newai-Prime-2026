import speech_recognition as sr
import os

class NewaiVoiceWake:
    def __init__(self, brain):
        self.brain = brain
        self.recognizer = sr.Recognizer()
        self.is_listening = True

    def start_passive_listening(self):
        """Ekran kapalıyken arka planda 'Hey Newai' komutunu bekler."""
        with sr.Microphone() as source:
            print(">>> Newai Pusuda... Sahibin sesini bekliyor.")
            while self.is_listening:
                try:
                    # Arka plan gürültüsünü filtrele
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=3)
                    
                    # Sesi analiz et
                    command = self.recognizer.recognize_google(audio, language="tr-TR").lower()
                    
                    if "hey newai" in command:
                        self.trigger_authority_mode(command)
                except:
                    continue

    def trigger_authority_mode(self, full_command):
        """Komut algılandığında sistemi uyandırır ve göreve başlar."""
        print(">>> Buyurun sahip, sizi dinliyorum.")
        # Eğer komut 'indir' içeriyorsa doğrudan Uydu Çekirdeğine gönder
        if "indir" in full_command:
            self.brain.satellite.process_voice_download(full_command)
        else:
            # Standart asistan modunu veya internet tünelini uyarır
            self.brain.live_mode.activate()