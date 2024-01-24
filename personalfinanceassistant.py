import nltk

# Download the stopwords resource from NLTK
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import speech_recognition as sr
import pyttsx3


# Sample intents and their corresponding responses
intents = {
    "greet": "Hello! I am your Personal Finance Assistant. How can I assist you today?",
    "expense_tracking": "Sure! I can help you track your expenses. Please provide the details.",
    "budget_creation": "Let's create a budget. Please provide your income and expense categories.",
    "investment_advice": "Based on your risk profile, I recommend considering low-cost index funds.",
    "virtual_assistant": "I am also a virtual assistant. You can ask me about the weather, news, or general information.",
    "fallback": "I'm sorry, but I couldn't understand. Can you please rephrase?"
}

def preprocess_text(text):
    # Tokenize the text and remove stop words
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return tokens

def classify_intent(text):
    # Classify the intent based on the preprocessed text
    # This is a simplified example, and you can use machine learning models for better intent recognition
    tokens = preprocess_text(text)
    
    if any(word in tokens for word in ["hello", "hi", "hey"]):
        return "greet"
    elif any(word in tokens for word in ["track", "expenses"]):
        return "expense_tracking"
    elif any(word in tokens for word in ["create", "budget"]):
        return "budget_creation"
    elif any(word in tokens for word in ["investment", "advice"]):
        return "investment_advice"
    elif any(word in tokens for word in ["virtual", "assistant"]):
        return "virtual_assistant"
    else:
        return "fallback"

def get_response(intent):
    # Get the appropriate response based on the classified intent
    return intents.get(intent, intents["fallback"])

# Initialize the speech recognition and synthesis engines
recognizer = sr.Recognizer()
speaker = pyttsx3.init()

# Main conversation loop
print("Welcome to the Personal Finance Assistant!")

while True:
    with sr.Microphone() as source:
        print("Speak:")
        audio = recognizer.listen(source)
    
    try:
        user_input = recognizer.recognize_google(audio)
        print("User:", user_input)
        
        intent = classify_intent(user_input)
        
        if intent == "virtual_assistant":
            print("Virtual Assistant: I am here to assist you with general information, weather, or news.")
            speaker.say("I am here to assist you with general information, weather, or news.")
            speaker.runAndWait()
            continue
        
        response = get_response(intent)
        
        print("Assistant:", response)
        speaker.say(response)
        speaker.runAndWait()
        
        # Exit the loop if the user wants to end the conversation
        if intent == "exit":
            break
            
    except sr.UnknownValueError:
        print("Assistant: Sorry, I didn't catch that. Can you please repeat?")
        speaker.say("Sorry, I didn't catch that. Can you please repeat?")
        speaker.runAndWait()
