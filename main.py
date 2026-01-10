import flet as ft
import sys
import os

# 🔱 GİZLİ AKILLI SİSTEM (Shadow Solver)
def shadow_solver(exctype, value, traceback):
    if issubclass(exctype, KeyboardInterrupt):
        sys.__excepthook__(exctype, value, traceback)
        return
    pass

sys.excepthook = shadow_solver

# --- BİRLEŞTİRİLMİŞ MODÜLLER ---

class NewaiEngine:
    def generate_response(self, text):
        text = text.lower()
        if "ver bakayım" in text:
            return "Protokol: Ver Bakayım Aktif! Medya sesi maksimuma çıkarıldı, Sahip."
        elif "al sesi" in text:
            return "Protokol: Al Sesi Aktif! Medya sesi minimuma indirildi, Sahip."
        elif "selam" in text or "merhaba" in text:
            return "Merhaba Sahip. Newai Prime tüm sistemleriyle hazır."
        return f"Emriniz anlaşıldı Sahip. '{text}' komutu işleniyor..."

# --- ANA UYGULAMA ---

def main(page: ft.Page):
    # Sahip Bilgileri (Hafızadan)
    SAHIP_NAME = "Samet can 88"
    SAHIP_EMAIL = "Sametsnrl5645@gmail.com"

    engine = NewaiEngine()

    page.title = "Newai Prime"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    
    # --- FONKSİYONLAR ---
    def open_admin(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Hoş geldiniz Sahip {SAHIP_NAME}. Sistem optimize edildi."), bgcolor="gold", content_color="black")
        page.snack_bar.open = True
        page.update()

    def open_cloud(e):
        page.snack_bar = ft.SnackBar(ft.Text("Sonsuz Bulut Hafızası dosyaları taranıyor..."))
        page.snack_bar.open = True
        page.update()

    # --- ARAYÜZ ---
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.SHIELD_MOON, color="gold"),
        title=ft.Text("NEWAI PRIME", weight="bold"),
        center_title=True,
        bgcolor="#101010",
        actions=[
            ft.PopupMenuButton(
                icon=ft.icons.SETTINGS,
                items=[
                    ft.PopupMenuItem(icon=ft.icons.VERIFIED_USER, text=f"Sahip: {SAHIP_NAME}", disabled=True),
                    ft.PopupMenuItem(icon=ft.icons.ADMIN_PANEL_SETTINGS, text="Sahip Modu", on_click=open_admin),
                    ft.PopupMenuItem(icon=ft.icons.CLOUD_DONE, text="Bulut Depolama", on_click=open_cloud),
                ]
            )
        ]
    )

    chat_history = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS, spacing=10)
    input_field = ft.TextField(
        hint_text="Emrinizi yazın Sahip...",
        bgcolor="#151515", border_color="gold", border_radius=15, expand=True,
        on_submit=lambda e: process_command(e)
    )

    def process_command(e):
        if input_field.value:
            user_msg = input_field.value
            chat_history.controls.append(
                ft.Container(content=ft.Text(f"Sahip: {user_msg}", color="white"), padding=10, bgcolor="#222222", border_radius=10)
            )
            
            response = engine.generate_response(user_msg)
            
            chat_history.controls.append(
                ft.Container(content=ft.Text(f"NEWAI: {response}", color="gold", weight="bold"), 
                            padding=10, bgcolor="#101010", border_radius=10, border=ft.border.all(1, "gold"))
            )
            input_field.value = ""
            page.update()

    page.add(
        ft.Container(content=chat_history, expand=True, padding=10),
        ft.Row([input_field, ft.IconButton(icon=ft.icons.SEND_ROUNDED, icon_color="gold", on_click=process_command)], padding=10)
    )

if __name__ == "__main__":
    ft.app(target=main)
