from imagem import imagem
import cv2
import streamlit as st
from pages import page_criar_prova, page_corrigir_provas, page_processar_dados


def main():
    with open("style/style.css") as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html= True)


     
    menu, opcoes = st.columns([2, 5])
    
    with menu:
        menu_select = st.selectbox('selecione a página', ('Criar Prova', 'Corrigir Prova', 'Dados'))

    with opcoes:
        st.title('Corretor de provas')

        if menu_select == 'Criar Prova':
            page_criar_prova()

        elif menu_select == 'Corrigir Prova':
            page_corrigir_provas()

        elif menu_select == 'Dados':
            page_processar_dados()
        
    

if(__name__ == "__main__"):
    main()