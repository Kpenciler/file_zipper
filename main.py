from typing import List
import os
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile

from zip import zip_files, generate_password, zip_files_v2

DARA_PATH = "data"
def upload_files(files: List[UploadedFile]):
    for file in files:
        with open(file.name, "wb") as f:
            f.write(file.read())

import base64
def get_binary_file_downloader_html(file_path, text="Download Link"):
    # ダウンロードリンクを作成する関数
    with open(file_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_path}">{text}</a>'
    return href

def main():
    st.title("File Zipper")

    # ファイルのアップロード
    files = st.file_uploader("Upload Files", accept_multiple_files=True)

    if files:
        os.chdir(DARA_PATH)
        upload_files(files)

        # zipファイルを作成するためのフォームを表示する
        form = st.form(key='zip_form')
        zip_file_name = form.text_input("Zip file name",
                                        value=f"{os.path.splitext(files[0].name)[0]}.zip")
        submit_button = form.form_submit_button("Create Zip File")

        if submit_button:
            # zipファイルを作成する
            password = generate_password()
            zip_files(src=[file.name for file in files],
                      dst=zip_file_name,
                      password=password)
            # ダウンロードリンクとパスワードの表示
            st.markdown(get_binary_file_downloader_html(zip_file_name,
                                                        text=f"Download {zip_file_name}"),
                        unsafe_allow_html=True)
            st.markdown(f"password: :orange[{password}]")

        os.chdir("../")

if __name__ == '__main__':
    main()
