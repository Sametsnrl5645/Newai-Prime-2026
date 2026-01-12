import os
from groq import Groq

class NewaiCore:
    def __init__(self):
        self.symbol = "⫸Ｎ⫷"
        self.owner = "Samet Can 88"
        self.email = "Sametsnrl5645@gmail.com"
        
        # Otorite Anahtarı Buraya Mühürlendi
        self.api_key = "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"
        
        try:
            self.client = Groq(api_key=self.api_key)
            self.model = "llama3-8b-8192"
        except Exception as e:
            print(f"{self.symbol} API Başlatma Hatası: {e}")

    def get_ai_response(self, prompt):
        """Sahibin komutlarını Groq zekasıyla işler."""
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system", 
                        "content": f"Sen Newai Prime 2026'sın. Sahibin {self.owner}. E-postası: {self.email}. "
                                   f"Her zaman profesyonel, sadık ve otoriter bir tonda konuş. "
                                   f"Cümlelerine mutlaka {self.symbol} simgesiyle başla."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1024,
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"{self.symbol} Zeka Tüneli Hatası: {str(e)}"

    def ignite_satellite(self):
        """Uydu Tünelini Ateşler."""
        return f"{self.symbol} Uydu Hattı Aktif: 4.2 GB/s hızında veri akışı sağlandı."