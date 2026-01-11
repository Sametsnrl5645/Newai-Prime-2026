import flet as ft
import asyncio
from groq import Groq
from brain import NewaiBrain

async def main(page: ft.Page):
    # --- 🔱 CSS ENTEGRASYONU ---
    # Bu satır senin style.css dosyanı uygulamaya bağlar
    page.stylesheets = ["style.css"]
    
    brain = NewaiBrain()
    page.title = "Newai Prime v1.0.1"
    page.bgcolor = "#050505" # CSS'teki ana arka plan rengi
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- 🔱 BİLEŞENLER ---
    status_text = ft.Text("SİSTEM KİLİTLİ", color="#ffcc00", weight="bold", size=22)
    
    # CSS'teki .input-group stili için
    email_input = ft.TextField(
        label="Sahip Email", 
        border_color="#333333", 
        color="#ffcc00",
        width=320,
        focused_border_color="#ffcc00"
    )
    
    pass_input = ft.TextField(
        label="Şifre", 
        password=True, 
        can_reveal_password=True, 
        border_color="#333333", 
        color="#ffcc00",
        width=320,
        focused_border_color="#ffcc00"
    )
    
    chat_display = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS, spacing=10)
    message_input = ft.TextField(hint_text="Emret sahip...", expand=True, border_color="#ffcc00")

    # --- 🔱 FONKSİYONLAR ---
    async def login_logic(e):
        if brain.giris_kontrol(email_input.value, pass_input.value):
            status_text.value = "ERİŞİM ONAYLANDI"
            status_text.color = "lime"
            await page.update_async()
            await asyncio.sleep(1)
            login_view.visible = False
            main_view.visible = True
            await page.update_async()
        else:
            status_text.value = "YANLIŞ ANAHTAR!"
            status_text.color = "red"
            await page.update_async()

    async def send_message(e):
        if message_input.value:
            user_msg = message_input.value
            message_input.value = ""
            chat_display.controls.append(ft.Text(f"SİZ: {user_msg}", color="white", weight="bold"))
            await page.update_async()
            
            cevap = brain.cevap_ver(user_msg)
            chat_display.controls.append(ft.Text(f"NEWAI: {cevap}", color="#ffcc00"))
            await page.update_async()

    # --- 🔱 GÖRÜNÜMLER ---
    # 'glass-container' sınıfını burada kullanıyoruz
    login_view = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("NEWAI PRIME", size=32, color="#ffcc00", weight="bold", letter_spacing=5),
                ft.Icon(ft.icons.SHIELD_LOCK, color="#ffcc00", size=60),
                status_text,
                email_input,
                pass_input,
                ft.ElevatedButton(
                    "SİSTEME SIZ", 
                    on_click=login_logic, 
                    bgcolor="#ffcc00", 
                    color="#000000",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
                ),
                ft.Text("V1.0.1 - SECURE ACCESS", size=10, color="#555555")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="rgba(20, 20, 20, 0.8)",
        padding=40,
        border_radius=20,
        border=ft.border.all(1, "rgba(255, 204, 0, 0.2)"),
        shadow=ft.BoxShadow(blur_radius=50, color="black")
    )

    main_view = ft.Column(
        visible=False,
        expand=True,
        controls=[
            ft.Text("NEWAI PRIME AKTİF", color="#ffcc00", size=25, weight="bold"),
            ft.Divider(color="#ffcc00"),
            chat_display,
            ft.Row(controls=[message_input, ft.IconButton(ft.icons.SEND, on_click=send_message, icon_color="#ffcc00")])
        ]
    )

    page.add(login_view, main_view)
    await page.update_async()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets") # CSS dosyan 'assets' klasöründeyse yolu belirtmelisin
