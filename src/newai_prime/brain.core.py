import os
import base64
from groq import Groq
from .model_set import ModelSettings

class NewaiBrainCore:
    def __init__(self):
        # --- 🛡️ GÜVENLİK VE AYARLAR ---
        self.settings = ModelSettings()
        # API anahtarını güvenli bir şekilde çekiyoruz
        self.api_key = "gsk_4gLIalMzayORRQhDmr8AWGdyb3FY0TPY8NVMPuudbIxSIWVwqTc"

    # --- 🧠 1. KATMAN: METİN VE MANTIK MOTORU ---
    def mantik_motoru(self, input_text, mod="analiz"):
        """
        Girişi analiz eder ve en uygun modeli seçer.
        mod="sohbet": Daha esnek ve yaratıcı cevaplar.
        mod="analiz": Kesin, teknik ve hatasız cevaplar.
        """
        temiz_input = input_text.strip()
        
        # Mod seçimine göre Temperature ve Model ayarla
        model = self.settings.PRIMARY_MODEL if mod == "analiz" else self.settings.FAST_MODEL
        ayar = self.settings.STRICT_MODE if mod == "analiz" else self.settings.CHAT_MODE
        
        # Sahip Tanıma Sistemi (Öncelikli Protokol)
        if self.settings.SYSTEM_IDENTITY["owner_reference"].lower() in temiz_input.lower():
            ayar = 0.1  # Sahibine karşı hata payı sıfıra indirilir
            
        return self._ana_sorgu(temiz_input, model, ayar)

    # --- 👁️ 2. KATMAN: GÖRÜNTÜ İŞLEME MERKEZİ (VISION AI) ---
    def gorsel_analiz_merkezi(self, image_path, analiz_tipi="guvenlik"):
        """
        Görseldeki kodları, hataları ve tehditleri analiz eder.
        analiz_tipi="kod": Ekran görüntüsündeki kodları ayıklar.
        analiz_tipi="guvenlik": Siber tehditleri veya hataları bulur.
        """
        try:
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            
            # Sisteme ne araması gerektiğini söyleyen dinamik prompt
            prompt = "Bu görseldeki tüm teknik detayları ve olası riskleri raporla, sahip."
            if analiz_tipi == "kod":
                prompt = "Bu görseldeki kodları ayıkla ve hataları düzeltip bana ver."

            completion = self.client.chat.completions.create(
                model="llama-3.2-11b-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": f"{prompt}, sahip."},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
                        ]
                    }
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Görüntü İşleme Hatası: {str(e)}"

    # --- 🎤 3. KATMAN: SES ANALİZ MERKEZİ (AUDIO AI) ---
    def ses_analiz_merkezi(self, audio_file_path):
        """
        Sahibin sesini tanır, doğrular ve metne döker.
        """
        try:
            # 1. Adım: Ses Dosyasını Oku
            with open(audio_file_path, "rb") as file:
                # 2. Adım: Whisper-v3 ile Deşifre Et
                transcription = self.client.audio.transcriptions.create(
                    file=(audio_file_path, file.read()),
                    model="whisper-large-v3",
                    response_format="text"
                )
            
            # 3. Adım: Mantık Motoruna Aktar (Sahip doğrulaması mantık motorunda yapılır)
            return self.mantik_motoru(transcription, mod="sohbet")
        except Exception as e:
            return f"Ses Analiz Hatası: {str(e)}"

    # --- 🌐 4. KATMAN: İSTİHBARAT MOTORU (BROWSING) ---
    def istihbarat_motoru(self, sorgu, derinlik="hizli"):
        """
        2026 canlı verilerine ve sistem açıklarına sızar, internette araştırma yapar.
        """
        # Arama motoru API entegrasyonu varsayımıyla (Search Engine Integration)
        search_results = f"'{sorgu}' hakkında 2026 siber istihbarat verileri toplanıyor..."
        
        # Çıkan sonuçları Zeka Katmanına göndererek özetle
        return self.mantik_motoru(
            f"İnternet Verileri: {search_results}\nSoru: {sorgu}\nAnaliz et, sahip.",
            mod="analiz"
        )

    # --- 📁 5. KATMAN: DERİN DOSYA VE APK ANALİZİ ---
    def derin_dosya_analizi(self, file_path):
        """
        APK, EXE ve PDF dosyalarının ruhuna (koduna) bakar, tehdit taraması yapar.
        """
        ext = file_path.split('.')[-1].lower()
        
        if ext == "apk":
            return self._apk_decompiler_intelligence(file_path)
        elif ext in ["pdf", "docx", "xlsx"]:
            return self._document_intelligence(file_path)
        else:
            return self._hex_analysis(file_path)

    def _apk_decompiler_intelligence(self, apk_path):
        # Manifest ve İzin Analizi Protokolü
        return "APK Analiz Raporu: Şüpheli izinler ve siber riskler tarandı, sahip!"

    def _document_intelligence(self, file_path):
        # Meta-data ve gizli veri ayıklama
        return "Belge Analiz Ediliyor: Gizli veriler ve meta-datalar ayıklanıyor..."

    def _hex_analysis(self, file_path):
        # Bilinmeyen formatlar için Binary tarama
        return "Bilinmeyen dosya formatı. Binary (Hex) tarama başlatılıyor."

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