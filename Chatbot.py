# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 11:33:29 2025

@author: User
"""

def chatbot():
    print("Welcome to the chatbot!")
    print("You can type: 'hello', 'how are you', or 'bye'.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()
