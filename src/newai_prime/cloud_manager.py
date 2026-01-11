import sqlite3
import os
from datetime import datetime

class NewaiCloudManager:
    def __init__(self, owner_email):
        self.owner_email = owner_email
        self.db_path = "database/newai_memory.db"
        self._initialize_db()

    def _initialize_db(self):
        """Sonsuz bulutun yerel iskeletini oluşturur."""
        if not os.path.exists('database'):
            os.makedirs('database')
            
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Dosyaların ve bilgilerin saklandığı ana tablo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS eternal_storage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT,
                file_type TEXT,
                cloud_link TEXT,
                upload_date TIMESTAMP,
                summary TEXT,
                owner_tag TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def save_to_cloud(self, file_path, summary=""):
        """Bir dosyayı unutmamak üzere sisteme işler."""
        file_name = os.path.basename(file_path)
        file_type = os.path.splitext(file_name)[1]
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO eternal_storage (file_name, file_type, upload_date, summary, owner_tag)
            VALUES (?, ?, ?, ?, ?)
        ''', (file_name, file_type, datetime.now(), summary, self.owner_email))
        
        conn.commit()
        conn.close()
        return f">>> {file_name} sonsuz bulut sistemine mühürlendi, sahip."

    def search_memory(self, query):
        """Geçmişteki dosyalar veya bilgiler arasında arama yapar."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Akıllı arama: Özetlerde veya dosya isimlerinde ara
        cursor.execute("SELECT file_name, summary FROM eternal_storage WHERE summary LIKE ?", ('%' + query + '%',))
        results = cursor.fetchall()
        conn.close()
        return results