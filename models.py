# models.py

class GuruChat:
    def __init__(self, session_id, user_id, message, timestamp=None):
        self.session_id = session_id
        self.user_id = user_id
        self.message = message
        self.timestamp = timestamp

class SiswaChat:
    def __init__(self, session_id, user_id, message, timestamp=None):
        self.session_id = session_id
        self.user_id = user_id
        self.message = message
        self.timestamp = timestamp

class GenerateSoal:
    def __init__(self, topik, jumlah, tingkat, hasil=None):
        self.topik = topik
        self.jumlah = jumlah
        self.tingkat = tingkat
        self.hasil = hasil
