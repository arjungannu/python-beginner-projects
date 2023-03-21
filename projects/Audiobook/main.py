import pyttsx3
import PyPDF2


def play(pdfReader):
    speaker = pyttsx3.init()

    for page_num in range(len(pdfReader.pages)):
        text = pdfReader.pages[page_num].extract_text()
        speaker.say(text)
        speaker.runAndWait()

    speaker.stop()


file = input("Enter your PDF file name : ")  # Enter your own PDF file path

while True:
    try:
        book = open(file, "rb")
        break

    except Exception as e:
        print("An error occured:\n", e)
        print("\nEnter again\n")

pdfReader = PyPDF2.PdfReader(book)
play(pdfReader)
