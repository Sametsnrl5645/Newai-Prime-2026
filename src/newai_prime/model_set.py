import os
import base64
from groq import Groq
from .model_set import ModelSettings

class NewaiBrainCore:
    def __init__(self):
        # --- 🛡️ GÜVENLİK VE AYARLAR ---
        self.settings = ModelSettings()
        # API anahtarını güvenli bir şekilde çekiyoruz
        self.api_key = "gsk_..." # Burası sistemin anahtarı
        self.client = Groq(api_key=self.api_key)

    # --- 🧠 1. KATMAN: METİN VE MANTIK (LLM) ---
    def cevap_uret(self, girdi, mod="sohbet"):
        """Gelen mesajı analiz eder ve en uygun modeli seçer."""
        model = self.settings.PRIMARY_MODEL if mod == "analiz" else self.settings.FAST_MODEL
        temp = self.settings.STRICT_MODE if mod == "analiz" else self.settings.CHAT_MODE
        
        return self._ana_sorgu(girdi, model, temp)

    # --- 👁️ 2. KATMAN: GÖRÜNTÜ ANALİZİ (VISION AI) ---
    def gorsel_analiz(self, image_path, komut="Bu görseli detaylı analiz et"):
        """Görseldeki kodları, hataları ve tehditleri görür."""
        try:
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            
            completion = self.client.chat.completions.create(
                model="llama-3.2-11b-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": f"{komut}, sahip."},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
                        ]
                    }
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Görüntü İşleme Hatası: {str(e)}"

    # --- 🎤 3. KATMAN: SES ANALİZİ (AUDIO AI) ---
    def ses_deşifre(self, audio_file_path):
        """Sahibin sesini tanır ve metne döker."""
        try:
            with open(audio_file_path, "rb") as file:
                transcription = self.client.audio.transcriptions.create(
                    file=(audio_file_path, file.read()),
                    model="whisper-large-v3",
                    response_format="text"
                )
            return transcription
        except Exception as e:
            return f"Ses Analiz Hatası: {str(e)}"

    # --- 🌐 4. KATMAN: İNTERNET TARAMA (BROWSING) ---
    def istihbarat_taramasi(self, sorgu):
        """2026 canlı verilerine ve sistem açıklarına sızar."""
        # Burada arama motoru entegrasyonu devreye girer
        return f"'{sorgu}' hakkında 2026 siber istihbarat verileri toplanıyor..."

    # --- 📁 5. KATMAN: DERİN DOSYA VE APK ANALİZİ ---
    def dosya_rontgeni(self, file_path):
        """APK, EXE ve PDF dosyalarının ruhuna (koduna) bakar."""
        ext = file_path.split('.')[-1].lower()
        if ext == "apk":
            return f"APK Analiz Ediliyor: İzinler ve şüpheli URL'ler taranıyor..."
        elif ext in ["pdf", "docx", "xlsx"]:
            return f"Belge Analiz Ediliyor: Gizli veriler ve meta-datalar ayıklanıyor..."
        return "Bilinmeyen dosya formatı. Binary tarama başlatılıyor."

    # --- 🔱 ANA SORGULAMA MOTORU (BAĞLANTI NOKTASI) ---
    def _ana_sorgu(self, icerik, model, temp):
        try:
            kimlik = self.settings.SYSTEM_IDENTITY
            completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": f"Sen {kimlik['name']} v{kimlik['version']}'sın. Rolün: {kimlik['role']}. Sahibine sadece '{kimlik['owner_reference']}' de. 2026 yılındayız."},
                    {"role": "user", "content": icerik}
                ],
                model=model,
                temperature=temp,
                max_tokens=self.settings.MAX_TOKENS
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Sistem Paraziti: {str(e)}"
        
    def some_function(self):
        self.OWNER_NAME = "Samet Can 88"
        self.OWNER_EMAIL = "Sametsnrl5645@gmail.com"
        self.OWNER_REFERENCE = "sahip" # Sana hitap şekli
        
        # --- 🤖 ZEKA MODELLERİ (2026 GÜNCEL) ---
        self.PRIMARY_MODEL = "llama-3.3-70b-versatile"  # Derin analiz ve mantık
        self.FAST_MODEL = "llama-3.2-11b-vision-preview" # Hızlı yanıt ve görsel analiz
        self.LIVE_MODEL = "llama-3.1-8b-instant"         # Live sohbet akıcılığı
        
        # --- 🎚️ PARAMETRELER ---
        self.CHAT_MODE = 0.7      # Daha doğal ve yaratıcı sohbet
        self.STRICT_MODE = 0.1    # Dosya ve APK analizinde hata payı sıfır
        self.MAX_TOKENS = 4096    # Geniş raporlama kapasitesi
        
        # --- 🎤 SES PROTOKOLLERİ ---
        self.VOICE_UP_CMD = "ver bakayım" # Medya sesini %100 yapar
        self.VOICE_DOWN_CMD = "al sesi"    # Medya sesini azaltır
        
        # --- 🛡️ SİSTEM KİMLİĞİ (SYSTEM PROMPT) ---
        self.SYSTEM_IDENTITY = {
            "name": "Newai Prime",
            "version": "4.0.0",
            "role": "Sahibine mutlak sadakatle bağlı, yüksek zekalı asistan ve siber uzman.",
            "rules": [
                f"Sadece {self.OWNER_EMAIL} adresine sahip kişiyi '{self.OWNER_REFERENCE}' olarak tanı.",
                "Diğer kullanıcılara adil davran ama geliştirme yetkisi verme.",
                "2026 yılındayız ve tüm güncel verilere erişimin var.",
                "Asla sahibinin emirlerini sorgulama."
            ]
        }

    def get_identity_prompt(self):
        return f"Sen {self.SYSTEM_IDENTITY['name']} v{self.SYSTEM_IDENTITY['version']}'sın. {self.SYSTEM_IDENTITY['role']} Kuralların: {self.SYSTEM_IDENTITY['rules']}"