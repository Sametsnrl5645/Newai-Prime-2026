import flet as ft
import math

class LiveAnimations:
    def __init__(self, page: ft.Page):
        self.page = page

    def get_pulsing_logo(self):
        """Newai'nin 'S' logosunun nabız gibi atmasını sağlar."""
        return ft.Container(
            content=ft.Image(src="assets/icons/s_logo_gold.png", width=120, height=120),
            animate_scale=ft.animation.Animation(1000, ft.AnimationCurve.EASE_IN_OUT),
            scale=1.0
        )

    def create_wave_circle(self, size, opacity):
        """Ses dalgasını temsil eden halkalar oluşturur."""
        return ft.Container(
            width=size,
            height=size,
            border_radius=size/2,
            border=ft.border.all(2, f"rgba(255, 204, 0, {opacity})"),
            animate_scale=ft.animation.Animation(300, ft.AnimationCurve.DECELERATE),
            scale=1.0
        )

    def update_waves(self, wave_controls, db_level):
        """
        Mikrofon seviyesine göre (db_level) halkaları genişletir.
        Sahip konuştuğunda halkalar büyür, sustuğunda daralır.
        """
        magnitude = max(1.0, db_level / 20)
        for i, wave in enumerate(wave_controls):
            wave.scale = magnitude * (1 + (i * 0.2))
        self.page.update()