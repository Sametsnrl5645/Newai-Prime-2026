import flet as ft

class InternetDash:
    def __init__(self, page: ft.Page, satellite_core):
        self.page = page
        self.sat = satellite_core

    def build(self):
        self.page.clean()
        
        # --- 🛰️ UYDU RADARI ---
        radar_visual = ft.Container(
            content=ft.Column([
                ft.Icon(ft.icons.SATELLITE_ALT, color="#ffcc00", size=50),
                ft.Text("UYDU BAĞLANTISI: AKTİF", color="#ffcc00", weight="bold"),
                ft.ProgressBar(width=300, color="#ffcc00", bgcolor="#333333")
            ], alignment=ft.MainAxisAlignment.CENTER),
            padding=30, bgcolor="#111111", border_radius=20
        )

        # --- 🚀 HIZ GÖSTERGESİ ---
        speed_stats = ft.Row([
            self._stat_card("HIZ", "4.2 GB/s", ft.icons.SPEED),
            self._stat_card("GECİKME", "1 ms", ft.icons.TIMER_OUTLINED),
        ], alignment=ft.MainAxisAlignment.CENTER)

        # --- 🔒 BAĞIMLILIK KİLİDİ DURUMU ---
        status_footer = ft.Container(
            content=ft.Text(
                "NEWAI BAĞIMLILIK KİLİDİ: MÜHÜRLÜ (GÜVENLİ)",
                color="#00ff00", size=10, weight="bold"
            ),
            padding=10
        )

        self.page.add(
            ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: self.page.go("/")),
            ft.Text("NEWAI GLOBAL INTERNET", size=20, weight="bold", color="white"),
            radar_visual,
            speed_stats,
            status_footer
        )

    def _stat_card(self, title, value, icon):
        return ft.Container(
            content=ft.Column([
                ft.Icon(icon, color="#ffcc00"),
                ft.Text(title, size=10, color="#555555"),
                ft.Text(value, size=18, weight="bold", color="white")
            ]),
            padding=15, bgcolor="#1a1a1a", border_radius=10, width=150
        )