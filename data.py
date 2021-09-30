import streamlit as st
from PIL import Image
nft = Image.open("Horse.png")
st.image(nft, use_column_width=True)