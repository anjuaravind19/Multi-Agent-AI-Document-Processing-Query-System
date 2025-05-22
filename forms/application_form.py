import streamlit as st
from utils.file_utils import save_uploaded_file
from db.mongo_client import insert_form_data


def launch_form():
    st.title("User Application Form")

    name = st.text_input("Name")
    email = st.text_input("Email")
    contact = st.text_input("Contact")
    # Other fields...

    uploaded_files = {
        "bank_statement": st.file_uploader("Bank Statement (pdf/txt/png/jpg)"),
        "emirates_id": st.file_uploader("Emirates ID"),
        "resume": st.file_uploader("Resume"),
        "assets_liabilities": st.file_uploader("Assets/Liabilities (Excel)"),
        "credit_report": st.file_uploader("Credit Report"),
    }

    if st.button("Submit"):
        if not name or not email:
            st.error("Please fill all required fields")
            return

        saved_file_paths = {}
        for key, file in uploaded_files.items():
            if file is not None:
                path = save_uploaded_file(file, key)
                saved_file_paths[key] = path

        form_data = {
            "name": name,
            "email": email,
            "contact": contact,
            "files": saved_file_paths
            # Add other data here
        }

        inserted_id = insert_form_data("applications", form_data)
        st.success(f"Application submitted! ID: {inserted_id}")

st.title("Multi-Agent QA Bot")
launch_form()