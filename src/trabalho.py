import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

st.header("1. Saturação")
foto = Image.open("imagens/foto3.png")
img = np.array(foto)[:, :, :3]
fator = st.slider("Saturação", 0.0, 2.0, 1.5)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
st.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="saturação")

st.header("3. Matiz girada")
foto = Image.open("imagens/foto3.png")
img = np.array(foto)[:, :, :3]
giro = st.slider("Giro (graus)", 0, 360, 120)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h = hsv[:, :, 0].astype(int)
h = h + giro // 2
h = h % 180
hsv2 = hsv.copy()
hsv2[:, :, 0] = h
st.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="matiz girada")

st.header("8. Negativo")
foto = Image.open("imagens/foto3.png")
img = np.array(foto)[:, :, :3]
negativo = 255 - img
st.image(negativo, caption="negativo")

st.header("15. Troca de cor")
foto = Image.open("imagens/foto3.png")
img = np.array(foto)[:, :, :3]
h_min, h_max = st.slider("Faixa de H do objeto", 0, 179, (0, 20))
giro_cor = st.slider("Giro da cor (graus)", 0, 360, 120)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
mascara = cv2.inRange(hsv, (h_min, 60, 40), (h_max, 255, 255))
h = hsv[:, :, 0].astype(int)
h = h + giro_cor // 2
h = h % 180
girada = hsv.copy()
girada[:, :, 0] = h
resultado = hsv.copy()
dentro = mascara == 255
resultado[dentro] = girada[dentro]
st.image(cv2.cvtColor(resultado, cv2.COLOR_HSV2RGB), caption="troca de cor")

st.header("20. Pixel art")
foto = Image.open("imagens/foto3.png")
img = np.array(foto)[:, :, :3]
passo = st.slider("Passo", 1, 50, 10)
pequena = img[::passo, ::passo]
grande = pequena.repeat(passo, axis=0).repeat(passo, axis=1)
st.image(grande, caption="pixel art")