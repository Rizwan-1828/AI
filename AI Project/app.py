import streamlit as st
from PIL import Image
from rembg import remove


def main():
    st.title("Alpha matting")
    uploaded_files = st.file_uploader("Upload an image")
    if st.button("Generate"):
        if uploaded_files:
            img = Image.open(uploaded_files)
            res = bg_remove(img)
            col1, col2 = st.columns(2, gap="Wide")
            with col1:
                st.write("## Original Image")
                st.image(img)
            with col2:
                st.write("## Result Image")
                st.image(res)

        else:
            st.error('Please upload a image')


def bg_remove(image):
    return remove(image)


if __name__ == "__main__":
    main()
