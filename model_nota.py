from datetime import datetime
import uuid

class Nota:
    def __init__(self, id,  titlu, continut, status="în curs", data_crearii=None):
        self.id = str(uuid.uuid4()) if id is None else id
        self.titlu = titlu
        self.continut = continut
        self.status = status
        if data_crearii:
            self.data_crearii = datetime.strptime(data_crearii, '%Y-%m-%d %H:%M:%S')
        else:
            self.data_crearii = datetime.now()

    def __str__(self):
        return f"Nota(id={self.id},titlu={self.titlu},continut={self.continut},status={self.status},data_crearii={self.data_crearii})"

    def editare(self, titlu=None, continut=None, status=None):
        if titlu:
            self.titlu = titlu
        if continut:
            self.continut = continut
        if status:
            self.status = status

    def as_dict(self):
        return {
            'id': self.id,
            'titlu': self.titlu,
            'continut': self.continut,
            'status': self.status,
            'data_crearii': self.data_crearii.strftime('%Y-%m-%d %H:%M:%S')
        }
