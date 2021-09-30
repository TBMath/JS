import streamlit as st
from PIL import Image
nft = Image.open("Base Horse.png")
st.image(nft, use_column_width=True)