from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
language_learning_bot = ChatBot("LanguageLearningBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(language_learning_bot)

# Train the chatbot on the language learning corpus
trainer.train("chatterbot.corpus.english")

# You can add additional training data specific to language learning
# trainer.train("path/to/your/language_learning_corpus.yml")

# Main interaction loop
print("Language Learning Bot: Hi! I'm here to help you with language learning. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        print("Language Learning Bot: Goodbye!")
        break
    
    # Get the chatbot's response
    bot_response = language_learning_bot.get_response(user_input)
    print("Language Learning Bot:", bot_response)
