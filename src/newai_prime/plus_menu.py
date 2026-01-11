import flet as ft

class PlusMenu:
    def __init__(self, page: ft.Page, brain):
        self.page = page
        self.brain = brain

    def show(self):
        """Artı menüsünü bir BottomSheet (Alt Panel) olarak açar."""
        
        menu_content = ft.Container(
            padding=20,
            bgcolor="#111111",
            border_radius=ft.border_radius.only(top_left=20, top_right=20),
            content=ft.Column(
                main_axis_size=ft.MainAxisSize.MIN,
                children=[
                    ft.Text("GÜÇ PANELİ", color="#ffcc00", weight="bold", size=16),
                    ft.Divider(color="#333333"),
                    
                    # 🎤 SESLİ KOMUT (Standart Kayıt)
                    self._menu_item(ft.icons.MIC_ROUNDED, "Sesli Komut", self.start_voice),
                    
                    # 📸 FOTOĞRAF / SİBER GÖZ
                    self._menu_item(ft.icons.CAMERA_ALT_ROUNDED, "Fotoğraf / Siber Göz", self.open_camera),
                    
                    # 📄 DOSYA / APK ANALİZİ
                    self._menu_item(ft.icons.FILE_COPY_ROUNDED, "Dosya / APK Analizi", self.pick_file),
                    
                    # 🌐 İNTERNET İSTİHBARATI
                    self._menu_item(ft.icons.LANGUAGE_ROUNDED, "İnternet İstihbaratı", self.web_search),
                ]
            )
        )
        
        self.page.bottom_sheet = ft.BottomSheet(menu_content)
        self.page.bottom_sheet.open = True
        self.page.update()

    def _menu_item(self, icon, text, action):
        return ft.ListTile(
            leading=ft.Icon(icon, color="#ffcc00"),
            title=ft.Text(text, color="white", weight="w500"),
            on_click=action
        )

    # --- EYLEMLER ---
    def start_voice(self, e):
        print(">> Ses dinleniyor...")
        
    def open_camera(self, e):
        print(">> Siber Göz aktif...")
        
    def pick_file(self, e):
        print(">> Dosya seçiliyor...")
        
    def web_search(self, e):
        print(">> 2026 verileri taranıyor...")