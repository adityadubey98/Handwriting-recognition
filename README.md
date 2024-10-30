# 📄 Handwriting-recognition 
This code creates a multi-page Streamlit web app that allows users to upload an image and perform Optical Character Recognition (OCR) on it using the Tesseract OCR engine.<br>
1. Streamlit is used to create the web interface.<br>
2. PIL.Image for image handling.<br>
3. Pytesseract for OCR functionality.<br>
4. Cv2 (OpenCV) for image processing, specifically to preprocess images before OCR.<br>
5. Numpy for converting image data into a format compatible with OpenCV.<br>
The tesseract_cmd path is set to the Tesseract installation location on the system. Tesseract is the OCR engine used for text extraction from images.<br>
The preprocess_image function takes an image as input, converts it to grayscale, and applies a Gaussian blur to reduce noise, improving the OCR accuracy.<br>
## The ocr_image function handles the OCR process:<br>
The input image is preprocessed using preprocess_image.<br>
pytesseract.image_to_string then extracts text from the processed image.<br>
If an error occurs during OCR, an error message is displayed on the Streamlit app.<br>
main_page function: Displays a title and a simple message to prompt users to select a page.<br>
## ocr_page function: Displays the OCR functionality.<br>
Allows users to upload an image through a file uploader.<br>
Shows the uploaded image on the page.<br>
Performs OCR and displays the extracted text.<br>
Provides a "Download Text as File" button to save the OCR result as a .txt file.<br>
## Page Selector (app_pages Dictionary)<br>
Contains the two pages of the app: the main page and the OCR page.<br>
## Main Function (main function)<br>
Directly calls the OCR page function (app_pages["OCR Page"]()), displaying it as the active page.<br>
### Run the App<br>
Checks if the script is being run directly and calls main() to start the app.<br>
<br>
<br>
## Summary
The app primarily consists of an OCR feature where users can upload an image, view it, and extract text from it.
The extracted text can then be saved to a file if desired. The Streamlit UI makes it easy to interact with the functionality directly in a web browser.
