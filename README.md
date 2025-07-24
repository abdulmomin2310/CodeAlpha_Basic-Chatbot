# CodeAlpha_Basic-Chatbot
# 🤖 Basic Rule-Based Chatbot

## 📌 Task Overview
**Task 4**: Build a simple **rule-based chatbot** using Python.

This chatbot interacts with the user through predefined replies based on specific inputs. It demonstrates the use of **if-elif statements**, **functions**, **loops**, and **input/output operations** — making it a perfect beginner-level Python project.

---

## ✅ Features
- Greets the user when they say "hello".
- Responds politely to "how are you".
- Ends the conversation when the user types "bye".
- Handles unknown inputs with a default response.
- Runs in a loop until the user decides to exit.

---

## 🧠 Key Concepts Used
- **Conditional Statements** (`if-elif-else`)
- **Loops** (`while`)
- **Functions**
- **String Methods** (`.lower()` for case insensitivity)
- **Input/Output Handling** (`input()`, `print()`)

---

## 🧾 Sample Conversation
```
Welcome to the chatbot!
You can type: 'hello', 'how are you', or 'bye'.
Type 'bye' to exit.

You: hello
Bot: Hi!

You: how are you
Bot: I'm fine, thanks!

You: what's your name
Bot: Sorry, I don't understand that.

You: bye
Bot: Goodbye!
```

---

## 🖥️ Full Python Code
```python
# Simple Rule-Based Chatbot

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
```

---

## 🔧 How to Run
1. Make sure Python is installed on your machine.
2. Copy the code into a `.py` file, for example: `chatbot.py`.
3. Run it using your terminal or any Python IDE:
   ```
   python chatbot.py
   ```

---

## 🚀 Future Improvements (Optional Ideas)
- Add more input phrases and responses.
- Introduce natural language processing (NLP).
- Randomize responses for variety.
- Add a GUI using Tkinter or PyQt.
