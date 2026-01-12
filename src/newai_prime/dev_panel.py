import flet as ft

class NewAIDevPanel:
    def __init__(self, page: ft.Page, brain):
        self.page = page
        self.brain = brain
        # Sistem loglarını tutacak alan
        self.log_stream = ft.ListView(expand=True, spacing=5, padding=10)

    def build(self):
        self.page.clean()
        self.page.bgcolor = "#000000" # Mutlak karanlık, tam odak

        # --- Üst Bilgi ---
        header = ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.TERMINAL, color="#ffcc00", size=20),
                ft.Text("NewAI GELİŞTİRME PANELİ v4.0", color="#ffcc00", weight="bold"),
            ], alignment=ft.MainAxisAlignment.CENTER),
            padding=15, border=ft.border.only(bottom=ft.BorderSide(1, "#222222"))
        )

        # --- Giriş Alanı (Mesaj Gibi) ---
        self.dev_input = ft.TextField(
            hint_text="Sistemi geliştirmek için emret (Kod veya Doğal Dil)...",
            multiline=True,
            min_lines=1,
            max_lines=5,
            border_color="#ffcc00",
            text_style=ft.TextStyle(color="#ffcc00", font_family="monospace"),
            expand=True
        )

        # Başlangıç Logu
        self.add_log("Sistem çekirdeği (Kernel) aktif.", "SYSTEM")
        self.add_log(f"Sahip {self.brain.settings.OWNER_NAME} bağlandı.", "AUTH")

        # Sayfa Düzeni
        self.page.add(
            header,
            self.log_stream,
            ft.Container(
                content=ft.Row([
                    self.dev_input,
                    ft.IconButton(ft.icons.UPGRADE, icon_color="#ffcc00", on_click=self.apply_dev_command)
                ]),
                padding=10, bgcolor="#111111"
            )
        )

    def add_log(self, text, tag="INFO"):
        """Panele teknik bir log satırı ekler."""
        color = "#00ff00" if tag == "SYSTEM" else "#555555"
        self.log_stream.controls.append(
            ft.Text(f"[{tag}] > {text}", color=color, font_family="monospace", size=12)
        )
        self.page.update()

    def apply_dev_command(self, e):
        """Yazdığın 'mesajı' sisteme enjekte eder."""
        command = self.dev_input.value
        if not command: return

        self.add_log(f"SAHİP_EMRİ: {command}", "ROOT")
        
        # Burada brain_core'a 'Sistemi Güncelle' sinyali gider
        # Newai yazdığın metni analiz eder ve kodlarını buna göre revize eder.
        self.add_log("Değişiklikler Newai Çekirdeğine işleniyor...", "SYNC")
        
        self.dev_input.value = ""
        self.page.update()