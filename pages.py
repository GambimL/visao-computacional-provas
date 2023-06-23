import streamlit as st
from imagem import imagem
import cv2


def page_criar_prova():
    st.text('aqui ira criar as provas')

def page_corrigir_provas():
    st.text('aqui pra aparecer o corretor das provas')

    picture = st.camera_input("Apote a camera para a folha ótpca")

    ANSWER_KEY = [{0: 1, 1: 0, 2: 0, 3: 3, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2}, 
                  {0: 1, 1: 0, 2: 0, 3: 3, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2}]
    img = cv2.imread('IMG_6841 (1).JPG')
    image = imagem(img)
    processadas, papers = image.pre_processa_imagem()
    pontuação, papers = image.processa_imagem(ANSWER_KEY, processadas, papers)
    imagem_pronta = cv2.hconcat(papers)
    #cv2.imshow('', imagem_pronta)
    #cv2.waitKey(0)

    st.image(imagem_pronta)

    
def page_processar_dados():
    st.text('aqui ira aparecer os dados processados')
