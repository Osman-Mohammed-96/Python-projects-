import tkinter as tk
import webbrowser
import requests
import openai
import speech_recognition as sr
import pyttsx3
import smtplib

# Initialize Tkinter window
window = tk.Tk()
window.title("Virtual AI Assistant")
window.geometry("400x500")

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize OpenAI GPT-3 API
openai.api_key = "your_gpt3_api_key"

# Weather API endpoint and API key
weather_api_key = "your_weather_api_key"
weather_endpoint = "https://api.openweathermap.org/data/2.5/weather"

# Location API endpoint and API key
location_api_key = "your_location_api_key"
location_endpoint = "https://your-location-api-endpoint.com"

# Function to display AI responses in the chat area
def display_response(response):
    chat_text.insert(tk.END, "AI: " + response + "\n")

# Function to process user commands
def process_command(user_input):
    if "open YouTube" in user_input:
        webbrowser.open("https://www.youtube.com")
    elif "open Chrome" in user_input:
        webbrowser.open("https://www.google.com")
    elif "weather" in user_input:
        city = "your_city_name"
        weather_params = {"q": city, "appid": weather_api_key}
        response = requests.get(weather_endpoint, params=weather_params).json()
        weather_info = response.get("weather")[0].get("description")
        display_response(f"The weather in {city} is {weather_info}.")
    elif "location" in user_input:
        location_params = {"apikey": location_api_key}
        response = requests.get(location_endpoint, params=location_params).json()
        location_info = response.get("location_info")
        display_response(f"Your location: {location_info}")
    else:
        # Use OpenAI GPT-3 for general conversation
        gpt_response = openai.Completion.create(
            engine="text-davinci-003", prompt=user_input, max_tokens=50
        )
        display_response(gpt_response.choices[0].text.strip())

# Function to process voice commands
def process_voice_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            display_response("You: " + user_input)
            process_command(user_input)
        except sr.UnknownValueError:
            display_response("AI: Sorry, I couldn't understand you.")
        except sr.RequestError:
            display_response("AI: There was an issue connecting to the service.")

# GUI Elements
chat_text = tk.Text(window)
chat_text.pack(padx=10, pady=10)

voice_button = tk.Button(window, text="Voice Command", command=process_voice_command)
voice_button.pack(pady=5)

window.mainloop()
