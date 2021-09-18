import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('Streamlit超入門')
"""タイトルを作成する"""

st.write('Display Image')
"""テキストを挿入する時に使う"""

img = Image.open('sample.jpeg')
st.image(img, caption='steve jobs', use_column_width=True)

"""use_column_witdthは実際の横幅に合わせてくれる"""

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# df = pd.DataFrame(
#     np.random.randn(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )


# st.write(df)

# st.dataframe(df.style.highlight_max(axis=0), height=200, width=200)

"""writeとdataframeは取れる引数が違う"""


# st.table(df.style.highlight_max(axis=0))
"""静的なテーブルを作る時はtableを使用する"""

# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)

# st.map(df)]
