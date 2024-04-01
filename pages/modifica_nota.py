import streamlit as st
from manager_nota import ManagerNota

# Inițializăm managerul de note
manager = ManagerNota()

st.title('Listare, Căutare și Editare Note')

# Câmp de căutare pentru filtrarea notelor după nume
cuvant_cheie = st.text_input('Caută note după nume:', '')

# Filtrăm notele în funcție de cuvântul cheie introdus
note_filtrate = manager.cauta_nota(cuvant_cheie) if cuvant_cheie else manager.note

# Afișăm notele filtrate
for nota in note_filtrate:
    with st.expander(f"{nota.titlu}"):
        # Afisează detalii despre notă
        st.write(f"Conținut: {nota.continut}")

        # Formular pentru editarea notei
        with st.form(f"form_edit_{nota.id}"):
            new_titlu = st.text_input("Titlu", value=nota.titlu, key=f"titlu_{nota.id}")
            new_continut = st.text_area("Conținut", value=nota.continut, key=f"continut_{nota.id}")
            submit_edit = st.form_submit_button("Salvează Modificările")

            if submit_edit:
                # Apelăm o metodă care să actualizeze nota bazată pe ID
                manager.modifica_nota(nota.id, new_titlu, new_continut)
                st.success("Nota a fost actualizată cu succes!")
                # Reîncarcă pagina pentru a reflecta modificările
                st.rerun()
