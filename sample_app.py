
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit.proto.Button_pb2 import Button
import time

st.title('Streamlit超入門')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Itreation {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)


st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('sample.jpeg')
    st.image(img, caption='steve jobs', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です'

st.write('Text Input')

option2 = st.text_input('あなたの趣味はなんですか？')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合させ内容を書く')


'あなたの趣味は:', option2

option3 = st.slider('あなたの今日の調子は？', 0, 100, 50)
'コンディション:', option3
