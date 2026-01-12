import flet as ft
import time

class BootScreen:
    def __init__(self, page: ft.Page, on_complete):
        self.page = page
        self.on_complete = on_complete # Animasyon bitince ana ekrana geçiş fonksiyonu

    def build(self):
        self.page.clean()
        self.page.bgcolor = "#000000"

        # --- 🔱 MERKEZİ LOGO (PARLAYAN S) ---
        self.logo = ft.Image(
            src="assets/icons/newai_logo_gold.png", 
            width=150,
            height=150,
            opacity=0,
            animate_opacity=ft.animation.Animation(2000, ft.AnimationCurve.EASE_IN_OUT),
            scale=0.8,
            animate_scale=ft.animation.Animation(2500, ft.AnimationCurve.DECELERATE),
        )

        # --- 🔱 YÜKLENME METNİ ---
        self.status_text = ft.Text(
            "NEWAI CORE LOADING...",
            color="#ffcc00",
            size=12,
            weight="bold",
            opacity=0,
            animate_opacity=ft.animation.Animation(1000, ft.AnimationCurve.EASE_IN),
            letter_spacing=2
        )

        # Düzen
        container = ft.Container(
            content=ft.Column([
                self.logo,
                ft.Container(height=20),
                self.status_text
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            expand=True,
            alignment=ft.alignment.center
        )

        self.page.add(container)
        self.run_animation()

    def run_animation(self):
        """Açılış animasyon protokolü."""
        self.page.update()
        time.sleep(0.5)
        
        # Logo parlayarak ve büyüyerek belirir
        self.logo.opacity = 1
        self.logo.scale = 1.1
        self.page.update()
        time.sleep(1.5)

        # Alt yazı belirir
        self.status_text.opacity = 1
        self.status_text.value = "SİSTEM DOĞRULANIYOR: SAMET CAN 88"
        self.page.update()
        time.sleep(1.5)

        # Ana ekrana geçiş
        self.on_complete()