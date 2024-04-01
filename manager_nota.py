import json
from model_nota import Nota

class ManagerNota:
    def __init__(self, fisier_json='note.json'):
        self.fisier_json = fisier_json
        self.note = []
        self.incarca_note()

    def incarca_note(self):
        try:
            with open(self.fisier_json, 'r') as f:
                note_json = json.load(f)
                for nota in note_json:
                    self.note.append(Nota(nota['id'], nota['titlu'], nota['continut'], nota['status'], nota['data_crearii']))
        except FileNotFoundError:
            with open(self.fisier_json, 'w') as f:
                json.dump([], f)

    def salveaza_note(self):
        with open(self.fisier_json, 'w') as f:
            note_json = [nota.as_dict() for nota in self.note]
            json.dump(note_json, f, ensure_ascii=False, indent=4)

    def schimba_status_nota(self, nota_id, status_nou):
        for nota in self.note:
            if nota.id == nota_id:
                nota.status = status_nou
                self.salveaza_note()
                break

    def sterge_nota(self, nota_id):
        self.note = [nota for nota in self.note if nota.id != nota_id]
        self.salveaza_note()

    def adauga_nota(self, titlu, continut):
        nota_noua = Nota(id=None, titlu=titlu, continut=continut)
        self.note.append(nota_noua)
        self.salveaza_note()

    # def editare_nota(self, index, titlu=None, continut=None, status=None):
    #     if 0 <= index < len(self.note):
    #         self.note[index].editare(titlu, continut, status)
    #         self.salveaza_note()

    def modifica_nota(self, nota_id, new_titlu, new_continut):
        for nota in self.note:
            if nota.id == nota_id:
                nota.titlu = new_titlu
                nota.continut = new_continut
                self.salveaza_note()  # Actualizează lista de note în sursa persistentă
                break

    def cauta_nota(self, cuvant_cheie):
        return [nota for nota in self.note if cuvant_cheie.lower() in nota.titlu.lower() or cuvant_cheie.lower() in nota.continut.lower()]
