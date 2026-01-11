import flet as ft
import asyncio

# --- 1. CANLI SES KATMANI (LIVE OVERLAY) ---
class NewaiLiveOverlay:
    def __init__(self, page):
        self.page = page
        self.panel = None
        
    def open_live_session(self, e=None):
        self.panel = ft.BottomSheet(
            ft.Container(
                content=ft.Column([
                    ft.Image(src="assets/waves_gold.gif", height=150), 
                    ft.Text("Newai Live Dinliyor...", size=20, color="#ffcc00"),
                    ft.Row([
                        ft.IconButton(ft.icons.VIDEOCAM_OUTLINED, tooltip="Canlı Göz"),
                        ft.FloatingActionButton(icon=ft.icons.STOP, bgcolor="#ffcc00", on_click=self.stop_session),
                        ft.IconButton(ft.icons.MIC_OFF, tooltip="Sustur"),
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=30),
                    ft.TextButton("Oturumu Kapat", on_click=lambda _: self.close_panel())
                ], tight=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER, padding=20),
                bgcolor="#111111",
                border_radius=ft.border_radius.only(top_left=30, top_right=30)
            ),
            open=True
        )
        self.page.overlay.append(self.panel)
        self.page.update()

    def stop_session(self, e):
        self.close_panel()

    def close_panel(self):
        if self.panel:
            self.panel.open = False
            self.page.update()

# --- 2. AYARLAR VE OTORİTE KONTROLÜ ---
def open_settings_screen(page: ft.Page, user_type="Sahip"):
    page.clean()
    
    # Kimlik Kartı (Samet can 88 / Sametsnrl5645@gmail.com)
    user_card = ft.Container(
        content=ft.ListTile(
            leading=ft.Icon(ft.icons.PERSON_PIN, color="#ffcc00", size=40),
            title=ft.Text(f"KİMLİK: {user_type.upper()}", weight="bold", size=20),
            subtitle=ft.Text("Sametsnrl5645@gmail.com" if user_type == "Sahip" else "Standart Erişim"),
        ),
        bgcolor="#1a1a1a", border_radius=15, padding=10
    )

    settings_list = ft.ListView(
        expand=True, spacing=15,
        controls=[
            user_card,
            ft.Text("SES VE OTORİTE", color="#ffcc00", weight="bold"),
            ft.ListTile(leading=ft.Icon(ft.icons.VOLUME_UP), title=ft.Text("Akıllı Ses Komutları"), subtitle=ft.Text("'Ver bakayım' aktif")),
            ft.Text("HAFIZA VE BULUT", color="#ffcc00", weight="bold"),
            ft.ListTile(leading=ft.Icon(ft.icons.CLOUD_DONE), title=ft.Text("Sonsuz Bulut Depolama"), subtitle=ft.Text("Newai Cloud Aktif")),
        ]
    )

    if user_type == "Sahip":
        settings_list.controls.append(ft.Divider(color="#333333"))
        settings_list.controls.append(
            ft.Container(
                content=ft.ElevatedButton(
                    "SAHİP MODU: NEWAI GELİŞTİRME", bgcolor="#ffcc00", color="black",
                    on_click=lambda _: open_newai_dev_panel(page)
                ), padding=10
            )
        )

    page.add(ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: back_to_home(page)), settings_list)
    page.update()

# --- 3. GELİŞTİRME PANELİ (ROOT ACCESS) ---
def open_newai_dev_panel(page: ft.Page):
    page.clean()
    page.bgcolor = "#000000"
    
    dev_log = ft.ListView(expand=True, spacing=8, padding=20, auto_scroll=True)
    dev_log.controls.append(ft.Text(">> ROOT ACCESS: SAMET CAN 88 GRANTED.", color="#00ff00", font_family="monospace"))

    dev_input = ft.TextField(hint_text="Çekirdek komutu yaz...", expand=True, border_color="#333333", text_style=ft.TextStyle(color="#ffcc00", font_family="monospace"))

    def process_command(e):
        dev_log.controls.append(ft.Text(f"SAHİP_KOMUT: {dev_input.value}", color="#ffffff", weight="bold"))
        dev_log.controls.append(ft.Text(f"SİSTEM: Çekirdek yapılandırılıyor...", color="#ffcc00", italic=True))
        dev_input.value = ""
        page.update()

    page.add(
        ft.Text("NEWAI CORE DEV", color="#ffcc00", weight="bold", size=20),
        dev_log,
        ft.Row([dev_input, ft.IconButton(ft.icons.REPLY_ALL_ROUNDED, icon_color="#ffcc00", on_click=process_command)], padding=10)
    )
    page.update()

# --- 4. ANA ARAYÜZ MOTORU (DASHBOARD) ---
class NewaiInterface:
    def __init__(self, page: ft.Page):
        self.page = page
        self.symbol = "⫸Ｎ⫷"
        self.gold = "#FFD700"
        self.live = NewaiLiveOverlay(page)

    def build(self):
        header = ft.Container(
            content=ft.Column([
                ft.Text(self.symbol, size=45, color=self.gold, weight="bold"),
                ft.Text("NEWAI PRIME 2026", size=14, color="white60", letter_spacing=4),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=self.page.width, padding=20
        )

        status_cards = ft.ResponsiveRow([
            self._card("UYDU HATTI", "4.2 GB/s", ft.icons.SATELLITE_ALT, "cyan"),
            self._card("ZEKA DURUMU", "AKTİF", ft.icons.PSYCHOLOGY, "purple"),
            self._card("BULUT DEPO", "SONSUZ", ft.icons.CLOUD_DONE, self.gold),
            self._card("GÜVENLİK", "MÜHÜRLÜ", ft.icons.SHIELD_ROUNDED, "green"),
        ])

        self.chat_history = ft.Column(expand=True, scroll=ft.ScrollMode.ADAPTIVE)
        self.command_input = ft.TextField(hint_text="Komut verin...", expand=True, border_color=self.gold, on_submit=lambda e: self._handle(e.control.value))

        return ft.Stack([
            ft.Column([header, ft.Container(status_cards, padding=10), self.chat_history], expand=True),
            ft.Container(content=ft.Row([self.command_input, ft.IconButton(ft.icons.MIC, on_click=self.live.open_live_session)]), bottom=0, bgcolor="#0a0a0a", padding=10)
        ], expand=True)

    def _card(self, t, v, i, c):
        return ft.Container(content=ft.Column([ft.Icon(i, color=c), ft.Text(t, size=9), ft.Text(v, size=12, weight="bold")], horizontal_alignment="center"), col={"sm": 6, "md": 3}, bgcolor="#111111", padding=10, border_radius=10)

    def _handle(self, cmd):
        self.chat_history.controls.append(ft.Text(f"Siz: {cmd}", color="white70"))
        self.chat_history.controls.append(ft.Text(f"{self.symbol}: Algılandı sahip.", color=self.gold))
        self.command_input.value = ""
        self.page.update()

# --- 5. ANA AKIŞ ---
def back_to_home(page):
    page.clean()
    ui = NewaiInterface(page)
    page.add(ui.build())

async def main(page: ft.Page):
    page.title = "Newai Prime"
    page.bgcolor = "#000000"
    page.padding = 0
    
    # Navigasyon Çekmecesi
    page.drawer = ft.NavigationDrawer(controls=[
        ft.Text("   AYARLAR", size=20, weight="bold", color="#ffcc00"),
        ft.NavigationDrawerDestination(icon=ft.icons.SETTINGS, label="Sistem Ayarları"),
    ], on_change=lambda _: open_settings_screen(page))
    
    page.app_bar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=lambda _: page.show_drawer()),
        title=ft.Text("Newai Prime", color="#ffcc00"),
        actions=[ft.IconButton(ft.CircleAvatar(content=ft.Text("S")), on_click=lambda _: open_settings_screen(page, "Sahip"))],
        bgcolor="#111111"
    )
    
    back_to_home(page)

if __name__ == "__main__":
    ft.app(target=main)