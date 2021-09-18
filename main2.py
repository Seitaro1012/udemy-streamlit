
# インタラクティブなウィジェット

from typing import Optional
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image


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

'あなたの趣味は:', option2

option3 = st.slider('あなたの今日の調子は？', 0, 100, 50)
'コンディション:', option3
