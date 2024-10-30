import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np

# Set Tesseract OCR path (update this path according to your Tesseract installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred

def ocr_image(image):
    try:
        # Preprocess the image
        processed_image = preprocess_image(image)
        # Perform OCR on the preprocessed image
        text = pytesseract.image_to_string(processed_image)
        return text
    except Exception as e:
        st.error(f"Error during OCR: {e}")
        return None

def save_to_text_file(text, filename="output.txt"):
    try:
        # Save the text to a text file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        st.success(f"Text saved to {filename}")
    except Exception as e:
        st.error(f"Error saving text to file: {e}")

def main_page():
    st.title("Multi-Page Streamlit App")
    st.write("Select a page from the sidebar.")

def ocr_page():
    st.title("OCR with Streamlit")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform OCR on the image
        text_result = ocr_image(np.array(image))

        if text_result is not None:
            # Display the OCR result
            st.subheader("OCR Result:")
            st.text(text_result)

            # Add a button to save the text to a file
            if st.button("Download Text as File"):
                save_to_text_file(text_result)

# Define the app pages
app_pages = {
    "Main Page": main_page,
    "OCR Page": ocr_page,
}

def main():
    app_pages["OCR Page"]()

if __name__ == "__main__":
    main()
