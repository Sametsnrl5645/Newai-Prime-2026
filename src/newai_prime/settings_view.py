import flet as ft

class SettingsView:
    def __init__(self, page: ft.Page, brain):
        self.page = page
        self.brain = brain
        self.is_owner = (self.brain.settings.OWNER_EMAIL == "Sametsnrl5645@gmail.com")

    def build(self):
        self.page.clean()
        
        # --- Üst Bilgi: Kimlik Kartı ---
        identity_card = ft.Container(
            content=ft.ListTile(
                leading=ft.Icon(ft.icons.VERIFIED_USER, color="#ffcc00"),
                title=ft.Text("KULLANICI KİMLİĞİ", size=12, color="#555555"),
                subtitle=ft.Text(
                    f"{self.brain.settings.OWNER_NAME} (SAHİP)" if self.is_owner else "STANDART KULLANICI",
                    color="white", weight="bold"
                ),
            ),
            bgcolor="#111111", border_radius=10, padding=10
        )

        # --- Genel Ayarlar ---
        general_settings = ft.Column([
            ft.ListTile(leading=ft.Icon(ft.icons.LANGUAGE), title=ft.Text("Dil / Language")),
            ft.ListTile(leading=ft.Icon(ft.icons.NOTIFICATIONS), title=ft.Text("Bildirimler")),
            ft.ListTile(leading=ft.Icon(ft.icons.CLOUD_QUEUE), title=ft.Text("Bulut Senkronizasyonu")),
        ])

        # --- 🔱 ÖZEL: NEWAI GELİŞTİRME PANELİ (Sadece Sahip İçin) ---
        dev_section = ft.Container()
        if self.is_owner:
            dev_section = ft.Container(
                content=ft.Column([
                    ft.Divider(color="#333333"),
                    ft.Text("YÜKSEK YETKİ ALANI", color="red", size=12, weight="bold"),
                    ft.ElevatedButton(
                        content=ft.Row([
                            ft.Icon(ft.icons.TERMINAL, color="black"),
                            ft.Text("NEWAI GELİŞTİRME PANELİ", color="black", weight="bold"),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        bgcolor="#ffcc00",
                        height=50,
                        on_click=self.open_dev_panel
                    )
                ]),
                padding=20
            )

        self.page.add(
            ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: self.page.go("/")),
            identity_card,
            general_settings,
            dev_section
        )

    def open_dev_panel(self, e):
        """Mesaj yazar gibi sistemi geliştirdiğin o özel ekranı açar."""
        # Burada dev_panel.py modülüne geçiş yapılacak
        print(">> NewAI Geliştirme Paneli Açılıyor, Sahip.")