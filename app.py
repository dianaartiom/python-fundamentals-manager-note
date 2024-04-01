
import streamlit as st
from manager_nota import ManagerNota

# Inițializăm managerul de note
manager = ManagerNota()

st.title('Aplicație de Note')

# Formular pentru adăugarea unei noi note
with st.form("add_note"):
    st.write("Adaugă o nouă notă")
    titlu = st.text_input("Titlu")
    continut = st.text_area("Conținut")
    submit_button = st.form_submit_button("Adaugă Nota")

    if submit_button:
        st.session_state.clicked_buttons.append("Create_new_note")
        manager.adauga_nota(titlu, continut)
        st.success("Nota adăugată cu succes!")

col_todo, col_in_progress, col_done = st.columns(3)

if 'clicked_buttons' not in st.session_state:
    st.session_state.clicked_buttons = []

with col_todo:
    st.header("ToDo")
    for nota in [n for n in manager.note if n.status == "în curs"]:
        with st.expander(f"{nota.titlu}"):
            st.write(f"Conținut: {nota.continut}")
            key = "progress_" + str(nota.id)[-12:]
            if st.button("Muta în In Progress", key=key):
                st.session_state.clicked_buttons.append(key)
                manager.schimba_status_nota(nota.id, "în progres")
                st.rerun()

with col_in_progress:

    st.header("In Progress")
    for nota in [n for n in manager.note if n.status == "în progres"]:
        with st.expander(f"{nota.titlu}"):
            st.write(f"Conținut: {nota.continut}")
            key = "done_" + nota.id[-12:]
            if st.button("Muta în Done", key=key):
                st.session_state.clicked_buttons.append(key)
                manager.schimba_status_nota(nota.id, "finalizat")
                st.rerun()

with col_done:
    st.header("Done")
    for nota in [n for n in manager.note if n.status == "finalizat"]:
        with st.expander(f"{nota.titlu}"):
            st.write(f"Conținut: {nota.continut}")
            key = "delete_" + nota.id[-12:]
            if st.button("Șterge", key=key):
                st.session_state.clicked_buttons.append(key)
                manager.sterge_nota(nota.id)
                st.rerun()


# Display the IDs of clicked buttons
st.write("Clicked button IDs:", st.session_state.clicked_buttons)
