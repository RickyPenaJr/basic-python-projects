while True:
    msg = input("You: ").lower()
    if "hello" in msg:
        print("Bot: Hi there!")
    elif "how are you" in msg:
        print("Bot: I'm good! How about you?")
    elif "bye" in msg:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")
