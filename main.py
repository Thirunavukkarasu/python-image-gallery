import streamlit as st
from os import listdir
from math import ceil

directory = r"images"
files = listdir(directory)

st.title("Image Browser")
st.write("This is a simple image browser built with Streamlit.")
st.write(f"There are {len(files)} images in the directory `{directory}`.")

## Controls
controls = st.columns(3)
with controls[0]:
    batch_size = st.select_slider("Batch size", range(1, len(files) + 1), len(files))
with controls[1]:
    row_size = st.select_slider("Row size", range(1, 6), value=2)
num_batches = ceil(len(files) // batch_size)
with controls[2]:
    page = st.selectbox("Page", range(1, num_batches + 1))

## Display
col = 0
batch = files[(page - 1) * batch_size : page * batch_size]
grid = st.columns(row_size)

for image in batch:
    with grid[col % row_size]:
        st.image(directory + "/" + image, use_column_width=True)
        st.caption(image.split(".")[0])
    col += 1
