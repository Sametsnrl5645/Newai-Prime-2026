import flet as ft
import time

# --- AKILLI ÇEKİRDEK ---
class NewaiCore:
    def __init__(self):
        self.sahip_name = "Samet can 88"
        self.sahip_email = "Sametsnrl5645@gmail.com"

    def process_intelligence(self, text):
        cmd = text.lower()
        if "ver bakayım" in cmd:
            return "🔊 PROTOKOL: VER BAKAYIM AKTİF!\nSes %100."
        elif "al sesi" in cmd:
            return "🔈 PROTOKOL: AL SESİ AKTİF!\nSes %0."
        return f"Emriniz işleniyor Sahip: {text}"

def main(page: ft.Page):
    core = NewaiCore()

    # 🔱 MOBİL UYUMLULUK AYARLARI
    page.title = "Newai Prime"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    
    # Pencere boyutlarını sildik, yerine sayfa hizalaması getirdik
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 10 
    page.expand = True # Sayfayı tamamen kapla

    # --- ARAYÜZ BİLEŞENLERİ ---
    chat_history = ft.Column(
        expand=True, 
        scroll=ft.ScrollMode.HIDDEN, # Mobilde daha akıcı kaydırma
        spacing=10
    )

    def process_command(e):
        if input_field.value:
            user_text = input_field.value
            input_field.value = ""
            
            # Sahip Mesajı
            chat_history.controls.append(
                ft.Container(
                    content=ft.Text(f"S: {user_text}", color="white"),
                    padding=10, bgcolor="#1e1e1e", border_radius=10
                )
            )
            
            # AI Yanıtı
            response = core.process_intelligence(user_text)
            chat_history.controls.append(
                ft.Container(
                    content=ft.Text(f"N: {response}", color="gold", weight="bold"),
                    padding=10, bgcolor="#0a0a0a", border_radius=10, border=ft.border.all(1, "gold")
                )
            )
            page.update()

    input_field = ft.TextField(
        hint_text="Emrinizi yazın...",
        bgcolor="#151515", border_color="gold", border_radius=15, expand=True,
        on_submit=process_command
    )

    # --- ÜST PANEL ---
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.SHIELD_MOON, color="gold"),
        title=ft.Text("NEWAI PRIME"),
        center_title=True,
        bgcolor="#101010"
    )

    # --- SAYFA DÜZENİ ---
    page.add(
        ft.Container(content=chat_history, expand=True),
        ft.Row([input_field, ft.IconButton(ft.icons.SEND_ROUNDED, icon_color="gold", on_click=process_command)])
    )

if __name__ == "__main__":
    ft.app(target=main)
