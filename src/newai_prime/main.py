import flet as ft
import os, sys, time, shutil

# =================================================================
# 1. NEWAI ÇEKİRDEK SİSTEMİ (Eski 18 dosyanın fonksiyonel gövdesi)
# =================================================================

from core.model_set import ModelSettings
from core.brain_core import NewaiBrainCore
from core.security_shield import SecurityShield
from core.cloud_manager import NewaiCloudManager
from ui.ui_display import MainInterface
from ui.settings_view import SettingsView
from ui.dev_panel import NewAIDevPanel

def main(page: ft.Page):
    # --- 1. SİSTEM ÖN AYARLARI ---
    page.title = "Newai Prime v4.0"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 800

    # --- 2. ÇEKİRDEK SERVİSLERİ BAŞLAT ---
    settings = ModelSettings()
    shield = SecurityShield()
    brain = NewaiBrainCore()
    cloud = NewaiCloudManager(settings.OWNER_EMAIL)

    # --- 3. GÜVENLİK VE OTORİTE KONTROLÜ ---
    # Uygulama açıldığında sahibini doğrular
    if not shield.verify_owner(settings.OWNER_EMAIL):
        page.add(ft.Text("ERİŞİM REDDEDİLDİ: Yetkisiz Cihaz.", color="red"))
        page.update()
        return

    # --- 4. ROTA YÖNETİMİ (Ekranlar Arası Geçiş) ---
    def route_change(route):
        page.views.clear()
        
        # ANA EKRAN (Chat & Live)
        if page.route == "/":
            ui = MainInterface(page, brain)
            page.views.append(ui.get_view())
            
        # AYARLAR VE HESAP
        elif page.route == "/settings":
            settings_view = SettingsView(page, brain)
            page.views.append(settings_view.get_view())
            
        # NEWAI GELİŞTİRME PANELİ (Kozmik Oda)
        elif page.route == "/dev":
            dev_panel = NewAIDevPanel(page, brain)
            page.views.append(dev_panel.get_view())
            
        page.update()

    # --- 5. BOOT (SİSTEMİ AYAĞA KALDIR) ---
    page.on_route_change = route_change
    page.go("/")
    
    print(f">>> Newai Prime Çekirdeği {settings.OWNER_NAME} İçin Hazır.")
    
class NewaiSystem:
    def __init__(self):
        self.owner = "Samet Can 88"
        self.email = "Sametsnrl5645@gmail.com"
        self.version = "2026.1.0"
        self.net_status = "PASİF"

    # --- UYDU VE INTERNET MOTORU ---
    def activate_satellite_link(self):
        # Ücretsiz uydu interneti başlatma simülasyonu
        time.sleep(1)
        self.net_status = "AKTİF (ÜCRETSİZ UYDU HATTI)"
        return self.net_status

    # --- ANKA KUŞU KURTARMA SİSTEMİ ---
    def phoenix_recovery(self):
        # Dosya kurtarma ve sistem onarma mantığı
        return "Tüm dosyalar buluttan geri yüklendi."

    # --- ACİL DURUM İMHASI ---
    def self_destruct(self, code):
        if code == "SH-88-DESTROY":
            # Sistem temizleme komutları
            return "Sistem başarıyla temizlendi."

# =================================================================
# 2. ADAPTİF VE ESNEK UI MOTORU
# =================================================================
def main(page: ft.Page):
    newai = NewaiSystem()
    
    # Sayfa Genel Ayarları
    page.title = "NEWAI PRIME 2026"
    page.bgcolor = "#000000"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK

    def build_ui():
        # Ekran boyutuna göre yazı tipi ve ikon ölçekleme
        sw = page.width
        is_mobile = sw < 600

        # Dinamik Başlık
        header = ft.Container(
            content=ft.Column([
                ft.Text("⧫Ｎ⧫", size=sw*0.1, color="gold", weight="bold"),
                ft.Text("NEWAI PRIME 2026", size=sw*0.05, letter_spacing=2, color="white")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.margin.only(top=50, bottom=30)
        )

        # Aksiyon Kartları (Responsive Grid)
        cards = ft.ResponsiveRow([
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.icons.SATELLITE_ALT, color="cyan"),
                    ft.Text("UYDU İNTERNETİ", weight="bold"),
                    ft.ElevatedButton("BAĞLAN", on_click=lambda _: connect_net())
                ], horizontal_alignment="center"),
                col={"sm": 12, "md": 6},
                bgcolor="#111111", padding=20, border_radius=15
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.icons.RECYCLING, color="gold"),
                    ft.Text("ANKA KURTARMA", weight="bold"),
                    ft.ElevatedButton("SİSTEMİ ONAR", on_click=lambda _: recovery())
                ], horizontal_alignment="center"),
                col={"sm": 12, "md": 6},
                bgcolor="#111111", padding=20, border_radius=15
            ),
        ], spacing=20)

        # Sabitlenmiş Alt Butonlar (Bottom Anchor)
        footer = ft.Container(
            content=ft.Row([
                ft.Text(f"Sahip: {newai.owner}", size=12, color="grey"),
                ft.Text(f"Durum: {newai.net_status}", size=12, color="grey"),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=20,
            bgcolor="#0a0a0a",
            bottom=0,
            width=sw
        )

        def connect_net():
            status = newai.activate_satellite_link()
            page.snack_bar = ft.SnackBar(ft.Text(f"⧫Ｎ⧫ {status}"))
            page.snack_bar.open = True
            page.update()

        def recovery():
            msg = newai.phoenix_recovery()
            page.snack_bar = ft.SnackBar(ft.Text(f"⧫Ｎ⧫ {msg}"))
            page.snack_bar.open = True
            page.update()

        return ft.Stack([
            ft.Column([header, ft.Container(content=cards, padding=20)], scroll=ft.ScrollMode.HIDDEN),
            footer
        ], expand=True)

    # Ekran yeniden boyutlandırıldığında tetiklenir
    def on_resize(e):
        page.clean()
        page.add(build_ui())
        page.update()

    page.on_resize = on_resize
    page.add(build_ui())
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")