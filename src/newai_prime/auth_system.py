import flet as ft

class AuthSystem:
    def __init__(self, page: ft.Page, on_login_success):
        self.page = page
        self.on_success = on_login_success # Başarılı girişte ui_display'e geçiş için
        self.gold = "#FFD700"

    def show_login(self):
        self.page.clean()
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        logo = ft.Text("⫸Ｎ⫷", size=80, color=self.gold, weight="bold")
        email = ft.TextField(label="E-posta", width=300, border_color=self.gold, value="Sametsnrl5645@gmail.com")
        password = ft.TextField(label="Şifre", width=300, border_color=self.gold, password=True)
        
        login_btn = ft.FilledButton(
            content=ft.Text("SİSTEME GİRİŞ YAP", weight="bold", color="black"),
            width=300, style=ft.ButtonStyle(bgcolor=self.gold),
            on_click=lambda _: self.on_success()
        )
        
        register_link = ft.TextButton("Hesabınız yok mu? Üye Ol", on_click=lambda _: self.show_register())

        self.page.add(logo, ft.Text("NEWAI PRIME LOGIN", color="white60"), ft.Container(height=20), email, password, login_btn, register_link)
        self.page.update()

    def show_register(self):
        self.page.clean()
        logo = ft.Text("⫸Ｎ⫷", size=60, color=self.gold, weight="bold")
        
        new_email = ft.TextField(label="Yeni E-posta", width=300, border_color=self.gold)
        new_pass = ft.TextField(label="Yeni Şifre", width=300, border_color=self.gold, password=True)
        
        reg_btn = ft.FilledButton(
            content=ft.Text("KAYIT OL VE BAŞLAT", weight="bold", color="black"),
            width=300, style=ft.ButtonStyle(bgcolor=self.gold),
            on_click=lambda _: self.show_login() # Kayıt sonrası girişe atar
        )

        back_btn = ft.TextButton("Giriş Ekranına Dön", on_click=lambda _: self.show_login())

        self.page.add(logo, ft.Text("ÜYE KAYIT PANELİ", color="white60"), ft.Container(height=20), new_email, new_pass, reg_btn, back_btn)
        self.page.update()