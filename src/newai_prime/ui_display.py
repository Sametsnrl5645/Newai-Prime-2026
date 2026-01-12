import flet as ft
import asyncio
import os
import sys
import glob

# 1. Adım: Klasörün tam yerini Android'e ezberletiyoruz
current_dir = os.path.dirname(os.path.realpath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# 2. Adım: Klasör ismini (newai_prime) doğrudan bir nesne gibi çağırıyoruz
try:
    # Bu satır, klasörün içindeki her şeyi Python'un 'görülebilir' listesine ekler
    import newai_prime
    print(f"{self.symbol} Çekirdek klasör Android katmanına sızdı.")
except ImportError as e:
    # Eğer BeeWare klasörü bulamazsa, paket ismini deniyoruz
    try:
        from com.sametcan88.newai import newai_prime
    except:
        print(f"🔱 Hata: Klasör yolu mühürlenemedi: {e}")

# Otorite Yolu: Çalışma anında modülleri bulmayı sağlar
base_path = os.path.dirname(os.path.abspath(__file__))
if base_path not in sys.path:
    sys.path.append(base_path)

class NewaiLiveOverlay:
    def __init__(self, page):
        self.page = page
        self.panel = None
        
    def open_live_session(self, e=None):
        self.panel = ft.BottomSheet(
            ft.Container(
                content=ft.Column([
                    ft.Icon("waves", size=100, color="#ffcc00"), 
                    ft.Text("Newai Live Dinliyor...", size=20, color="#ffcc00"),
                    ft.Row([
                        ft.IconButton("videocam_outlined", tooltip="Canlı Göz"),
                        ft.FloatingActionButton(icon="stop", bgcolor="#ffcc00", on_click=self.stop_session),
                        ft.IconButton("mic_off", tooltip="Sustur"),
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

class NewaiInterface:
    def __init__(self, page: ft.Page):
        self.page = page
        self.symbol = "⫸Ｎ⫷"
        self.gold = "#FFD700"
        self.core = {}
        self.live = NewaiLiveOverlay(page)
        self.chat_history = ft.Column(expand=True, scroll=ft.ScrollMode.ADAPTIVE)
        self.command_input = ft.TextField(
            hint_text="Komut verin...", expand=True, border_color=self.gold, 
            on_submit=lambda e: self._handle(e.control.value)
        )

    def initialize_github_modules(self):
        """Klasördeki tüm Newai modüllerini otomatik bulur ve mühürler"""
        # Bulunduğumuz klasördeki tüm .py dosyalarını tara
        module_files = glob.glob(os.path.join(base_path, "*.py"))
        
        for file in module_files:
            module_name = os.path.basename(file)[:-3] # .py uzantısını at
            
            # Ana dosyaları ve kendini atla
            if module_name in ["main", "ui_display", "__init__"]:
                continue
                
            try:
                # Modülü dinamik olarak uyanışa geçir
                module = __import__(module_name)
                self.core[module_name] = module
                print(f"{self.symbol} {module_name} başarıyla sisteme mühürlendi.")
            except Exception as e:
                print(f"{self.symbol} {module_name} uyarısı: {e}")

        print(f"{self.symbol} Toplam {len(self.core)} modül çekirdeğe bağlandı.")

    def _card(self, t, v, i, c):
        return ft.Container(
            content=ft.Column([
                ft.Icon(name=i, color=c, size=30),
                ft.Text(t, size=10, color="white70", weight="bold"),
                ft.Text(v, size=14, color="white", weight="black")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            col={"sm": 6, "md": 3},
            bgcolor="#1A1A1A",
            padding=15,
            border_radius=15,
            border=ft.border.all(0.5, "white24")
        )

    def _handle(self, cmd):
        if not cmd: return
        self.chat_history.controls.append(ft.Text(f"Siz: {cmd}", color="white70"))
        self.chat_history.controls.append(ft.Text(f"{self.symbol}: Algılandı sahip.", color=self.gold))
        self.command_input.value = ""
        self.page.update()

    def build(self):
        self.page.clean()
        self.initialize_github_modules()
        
        header = ft.Container(
            content=ft.Column([
                ft.Text(self.symbol, size=45, color=self.gold, weight="bold"),
                ft.Text("NEWAI PRIME 2026", size=14, color="white60"),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=self.page.width, padding=20
        )

        status_cards = ft.ResponsiveRow([
            self._card("UYDU HATTI", "4.2 GB/s", "satellite_alt", "cyan"),
            self._card("ZEKA DURUMU", "AKTİF", "psychology", "purple"),
            self._card("BULUT DEPO", "SONSUZ", "cloud_done", self.gold),
            self._card("GÜVENLİK", "MÜHÜRLÜ", "shield_rounded", "green"),
        ])

        self.page.add(
            ft.Column([
                header, 
                ft.Container(status_cards, padding=10), 
                self.chat_history,
                ft.Container(
                    content=ft.Row([
                        self.command_input, 
                        ft.IconButton("mic", on_click=self.live.open_live_session)
                    ]), bgcolor="#0a0a0a", padding=10
                )
            ], expand=True)
        )

        self.page.update()
