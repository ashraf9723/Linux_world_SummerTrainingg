import tkinter as tk
import pywhatkit as pw
from bs4 import BeautifulSoup
from threading import Thread
import requests
import speech_recognition as sr
from PIL import Image, ImageTk

def button_click(button_number):
    if button_number == 1:
        recognize_speech()
    elif button_number == 2:
        send_whatsapp_message()
    elif button_number == 3:
        search_google()
    elif button_number == 4:
        create_python_menu()
    # Add more elif conditions for other buttons here

#code for speech  recognization
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        print("Recognized Text:", recognized_text)
        show_output_popup("Recognized Text:\n" + recognized_text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
        output = "Recognize Speech functionality."
        show_output_popup(output)
        
#send whatsapp massage       
def send_whatsapp_message():
    # The WhatsApp message sending code (same as before)
    number = "+919305905287"  # Replace this with the recipient's phone number
    message = "Hello, this is a test message sent via Python!"  # Replace this with your desired message
    time_hour = 12  # Replace this with the desired hour (24-hour format)
    time_minute = 21 # Replace this with the desired minute

    try:
        pw.sendwhatmsg(number, message, time_hour, time_minute)
        print("WhatsApp message sent successfully!")
    except Exception as e:
        print(f"Error occurred while sending the WhatsApp message: {e}")
        output = "Send WhatsApp Message functionality."
        show_output_popup(output)

#code for google search
def search_google():
    query = "Python tutorials"  # Replace this with your search query
    num_results = 5

    try:
        search_results = google_search(query, num_results)
        print("Top search results:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result}")
    except Exception as e:
        print(f"Error occurred while performing the Google search: {e}")
def google_search(query, num_results=10):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    search_results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.select(".kCrYT a")
        for link in links[:num_results]:
            search_results.append(link.get("href"))
    output = "Search Google functionality."
    show_output_popup(output)


def create_python_menu():
    python_menu = tk.Toplevel(root)
    python_menu.title("Python Menu")

    # Function to be called when the menu options are selected
    def on_menu_selected(choice):
        print(f"Selected: {choice}")

    # Create the menu with some options
    menu_options = ["Option 1", "Option 2", "Option 3", "Option 4"]
    for option in menu_options:
        tk.Button(python_menu, text=option, command=lambda o=option: on_menu_selected(o)).pack(pady=5)
        

def show_output_popup(output):
    popup_window = tk.Toplevel(root)
    popup_window.title("Output")
    popup_window.geometry("400x200")

    label = tk.Label(popup_window, text=output, padx=10, pady=10)
    label.pack()

# Create the main Tkinter window
root = tk.Tk()
root.title("Menu-Based Project")

# Load and resize the background image
image_path = r"C:\Users\MD Ashraf\Downloads\Screenshot (28).png"
background_image = Image.open(image_path)
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(background_image)

# Create a label to hold the image and set it as the background
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT)

# Create seven buttons and place them vertically on the left side with different names
buttons_info = [
    {"text": "Recognize Speech", "bg": "red"},
    {"text": "Send WhatsApp Message", "bg": "green"},
    {"text": "Search Google", "bg": "blue"},
    {"text": "Create Python Menu", "bg": "yellow"},
    # Add more buttons and their names here
]

buttons = []
for button_number, button_info in enumerate(buttons_info):
    button = tk.Button(button_frame, text=button_info["text"], command=lambda num=button_number+1: button_click(num))
    button.pack(side=tk.TOP, padx=10, pady=5, anchor=tk.W, fill=tk.X)
    button.configure(bg=button_info["bg"])
    buttons.append(button)

# Start the Tkinter event loop
root.mainloop()
