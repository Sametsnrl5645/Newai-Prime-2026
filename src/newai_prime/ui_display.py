import flet as ft
import asyncio
import os
import sys
import glob

# 1. Adım: Klasörün tam yerini Android'e ezberletiyoruz
current_dir = os.path.dirname(os.path.realpath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

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
                    ft.Icon("waves", size=100, color="#FFD700"), 
                    ft.Text("Newai Live Dinliyor...", size=20, color="#FFD700", weight="bold"),
                    ft.Row([
                        ft.IconButton("videocam_outlined", tooltip="Canlı Göz", icon_color="white"),
                        ft.FloatingActionButton(icon="stop", bgcolor="#FFD700", on_click=self.stop_session),
                        ft.IconButton("mic_off", tooltip="Sustur", icon_color="white"),
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=30),
                    ft.TextButton("Oturumu Kapat", on_click=lambda _: self.close_panel(), style=ft.ButtonStyle(color="white70"))
                ], tight=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER, padding=20),
                bgcolor="#0A0A0B",
                border_radius=ft.border_radius.only(top_left=30, top_right=30),
                border=ft.border.all(0.5, "#FFD700")
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
        
        # 🔱 Devrimci Görsel Öğeler
        self.chat_history = ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=True)
        self.command_input = ft.TextField(
            hint_text="Emriniz nedir sahip?", 
            expand=True, 
            border_radius=25,
            bgcolor="#1C1C1E",
            color="white",
            border_color=self.gold, 
            on_submit=lambda e: self._handle(e.control.value)
        )

    def initialize_github_modules(self):
        """Klasördeki tüm Newai modüllerini otomatik bulur ve mühürler"""
        module_files = glob.glob(os.path.join(base_path, "*.py"))
        for file in module_files:
            module_name = os.path.basename(file)[:-3]
            if module_name in ["main", "ui_display", "__init__"]:
                continue
            try:
                module = __import__(module_name)
                self.core[module_name] = module
                print(f"{self.symbol} {module_name} başarıyla sisteme mühürlendi.")
            except Exception as e:
                print(f"{self.symbol} {module_name} uyarısı: {e}")

    def _card(self, t, v, i, c):
        # 🔱 Yenilenmiş Siber Kart Tasarımı
        return ft.Container(
            content=ft.Column([
                ft.Icon(name=i, color=c, size=28),
                ft.Text(t, size=10, color="white60", weight="bold"),
                ft.Text(v, size=13, color="white", weight="black")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            col={"sm": 6, "md": 3},
            bgcolor="#1C1C1E",
            padding=12,
            border_radius=18,
            border=ft.border.all(0.8, "white10"),
            shadow=ft.BoxShadow(blur_radius=10, color="black26")
        )

    def _handle(self, cmd):
        if not cmd: return
        self.chat_history.controls.append(
            ft.Container(
                content=ft.Text(f"Siz: {cmd}", color="white70"),
                padding=10, bgcolor="white05", border_radius=10
            )
        )
        
        # Brain Core entegrasyonu (Varsa kullan, yoksa varsayılan dön)
        response = "Algılandı sahip."
        if 'brain_core' in self.core:
             # Eğer brain_core modülünde think fonksiyonu varsa onu çağır
             try:
                 response = self.core['brain_core'].NewaiBrainCore().think(cmd)
             except:
                 pass

        self.chat_history.controls.append(
            ft.Container(
                content=ft.Text(f"{self.symbol}: {response}", color=self.gold, weight="bold"),
                padding=10, bgcolor="white05", border_radius=10, border=ft.border.all(0.5, "white10")
            )
        )
        self.command_input.value = ""
        self.page.update()

    def build(self):
        self.page.clean()
        self.page.bgcolor = "#0A0A0B" # Uzay Siyahı
        self.initialize_github_modules()
        
        header = ft.Container(
            content=ft.Column([
                ft.Text(self.symbol, size=50, color=self.gold, weight="black"),
                ft.Text("NEWAI PRIME v2.0", size=12, color="white38", letter_spacing=2),
                ft.Text(f"Sahip: Samet Can 88", size=14, color="white70"),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=self.page.width, padding=ft.padding.only(top=30, bottom=20)
        )

        status_cards = ft.ResponsiveRow([
            self._card("ZEKA", "LLAMA-3", "psychology", "purple"),
            self._card("GÜVENLİK", "MÜHÜRLÜ", "shield_rounded", "#00FF00"),
            self._card("SİSTEM", "STABİL", "bolt", "cyan"),
            self._card("ERİŞİM", "TAM YETKİ", "verified_user", self.gold),
        ], spacing=10)

        # 🔱 Ana Arayüz Düzeni
        self.page.add(
            ft.Column([
                header, 
                ft.Container(status_cards, padding=10), 
                ft.Container(
                    content=self.chat_history,
                    expand=True,
                    margin=ft.margin.only(top=10, bottom=10),
                    bgcolor="#111112",
                    border_radius=25,
                    border=ft.border.all(0.5, "white10")
                ),
                ft.Container(
                    content=ft.Row([
                        self.command_input, 
                        ft.IconButton("mic", icon_color=self.gold, icon_size=30, on_click=self.live.open_live_session)
                    ]), 
                    bgcolor="#1C1C1E", 
                    padding=12,
                    border_radius=30,
                    margin=ft.margin.only(bottom=10)
                )
            ], expand=True)
        )

        self.page.update()
