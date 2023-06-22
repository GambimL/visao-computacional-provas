from imagem import imagem
import cv2
import streamlit as st
import pandas as pd
import numpy as np


class resultado():
    def __init__(self, peso, acertos):
        self.peso = peso
        self.acertos = acertos
    
    def calcula_total(self):
        for i in self.peso:
            resultado = self.peso * self.acertos
    
        return resultado
