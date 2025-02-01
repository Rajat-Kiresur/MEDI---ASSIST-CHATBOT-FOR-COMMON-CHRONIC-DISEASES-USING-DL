import tkinter as tk
from tkinter import ttk
import random
import json
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import numpy as np
import speech_recognition as sr
import pyttsx3
import time

# Initialize nltk resources
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents data
with open("intents.json", 'r') as file:
    intents = json.load(file)

# Load pickled data
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')


# Define functions
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]

    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for intent in list_of_intents:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return ''


def speak(text):
    engine.say(text)
    engine.runAndWait()


def process_symptoms():
    text = symptoms_var.get()
    speak("You said {}".format(text))
    speak("Scanning our database for your selected data . Please wait.")
    time.sleep(1)
    response = get_response(predict_class(text), intents)
    speak("Found it " + response)
    result_text.set("Your Selected Data was: {}\nResult found in our Database: {}".format(text, response))


def on_exit():
    speak("Thank you for your trust . You're always welcome back. I'm available anytime to assist you. Signing off "
          "for now .")
    root.destroy()


recognizer = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()

# Configure engine properties
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')

print("Bot is officially online and eager to assist you in your quest for well-being! Let's dive into the realm of "
      "health together and unlock the secrets to vitality and happiness .")
# speak("Hey there! I'm medi-Assist, your virtual wellness companion equipped with the latest tools and knowledge to "
#       "guide you through the labyrinth of health choices . Together, we'll navigate through the twists and turns, "
#       "emerging victorious on the shores of vitality !")
# speak("For a personalized touch, please specify your desired voice type - male or female - to embark on a bespoke "
#       "health consultation .")

# with mic as source:
#     recognizer.adjust_for_ambient_noise(source, duration=0.2)
#     audio = recognizer.listen(source)
#
# audio = recognizer.recognize_google(audio).lower()
audio = input("female/male:\n")

if audio == "female":
    engine.setProperty('voice', voices[1].id)
    # speak("Wise decision ! Opting for the Female Voice ensures a compassionate and empathetic interaction , guiding you"
    #       "through your healthcare journey with care and understanding . lets start now")
else:
    engine.setProperty('voice', voices[0].id)
    # speak("Wise decision! Opting for the Male Voice ensures a compassionate and empathetic interaction, guiding you "
    #       "through your healthcare journey with care and understanding. lets start now")

# Create GUI
root = tk.Tk()
root.title("MediAssist Chatbot")

frame = ttk.Frame(root, padding="20", height=100)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

symptoms_label = ttk.Label(frame, text="Select Your Data:")
symptoms_label.grid(column=0, row=0, sticky=tk.W)

symptoms_options = []
for intent in intents['intents']:
    patterns = intent['patterns']
    for i in range(0, len(patterns), 3):
        symptom_line = ", ".join(patterns[i:i + 3])
        symptoms_options.append(symptom_line)

symptoms_var = tk.StringVar()
symptoms_dropdown = ttk.Combobox(frame, textvariable=symptoms_var, values=symptoms_options, width=100)
symptoms_dropdown.grid(column=0, row=1, sticky=(tk.W, tk.E))

process_button = ttk.Button(frame, text="Process", command=process_symptoms)
process_button.grid(column=0, row=2, sticky=tk.W)

result_text = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_text)
result_label.grid(column=0, row=3, sticky=tk.W)

exit_button = ttk.Button(frame, text="Exit", command=on_exit)
exit_button.grid(column=0, row=4, sticky=tk.W)
root.mainloop()
