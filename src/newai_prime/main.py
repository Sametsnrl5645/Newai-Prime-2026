import flet as ft
import asyncio
import os
from .brain import NewaiBrain, siber_guvenlik_taramasi

async def main(page: ft.Page):
    # 🔱 1. BEYİN BAĞLANTISI
    brain = NewaiBrain()

    # 🔱 2. EKRAN AYARLARI
    page.title = "Newai Prime v1.0.1"
    page.bgcolor = "#050505"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 🔱 3. BİLEŞENLER
    status_text = ft.Text("SİSTEM KİLİTLİ", color="#ffcc00", weight="bold", size=20)
    email_input = ft.TextField(label="Sahip Email", width=300, border_color="#ffcc00")
    pass_input = ft.TextField(label="Şifre", password=True, width=300, border_color="#ffcc00")
    chat_display = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    message_input = ft.TextField(hint_text="Emret sahip...", expand=True, border_color="#ffcc00")

    # 🔱 4. FONKSİYONLAR (Async uyumlu)
    async def login_logic(e):
        if brain.giris_kontrol(email_input.value, pass_input.value):
            status_text.value = "ERİŞİM ONAYLANDI"
            status_text.color = "lime"
            await page.update_async()
            await asyncio.sleep(0.8)
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
            
            # Beyinden cevap al (Burayı await ile sarmalayabiliriz eğer async ise)
            cevap = brain.cevap_ver(user_msg)
            chat_display.controls.append(ft.Text(f"NEWAI: {cevap}", color="#ffcc00"))
            await page.update_async()

    # 🔱 5. GÖRÜNÜMLER
    login_view = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("NEWAI PRIME", size=30, color="#ffcc00", weight="bold"),
                ft.Icon(ft.icons.SECURITY, color="#ffcc00", size=50),
                status_text,
                email_input,
                pass_input,
                ft.ElevatedButton("SİSTEME SIZ", on_click=login_logic, bgcolor="#ffcc00", color="black")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    main_view = ft.Column(
        visible=False, expand=True,
        controls=[
            ft.Text("NEWAI AKTİF", color="#ffcc00", size=22, weight="bold"),
            chat_display,
            ft.Row([message_input, ft.IconButton(ft.icons.SEND, on_click=send_message, icon_color="#ffcc00")])
        ]
    )

    await page.add_async(login_view, main_view)

# 🔱 BeeWare/Android için standart başlatıcı
def start():
    ft.app(target=main)

if __name__ == "__main__":
    start()
