print("🤖 ChatBot: Hello! I'm a simple chatbot. Try saying 'hi', 'help', or 'bye'.\n")
commands = {
    'greetings': ["hi", "hello", "hey"],
    'feelings': ["how are you", "how's it going"],
    'identity': ["your name", "who are you"],
    'time': ["time", "what time is it"],
    'date': ["date", "today's date"],
    'help': ["help", "what can you do"],
    'exit': ["bye", "goodbye", "exit"]
}
current_hints = ["Try saying 'hi' to start!"]
while True:
    print(f"\n💡 Hint: {current_hints[0]}")
    user_input = input("You: ").lower()
    if any(word in user_input for word in commands['greetings']):
        print("🤖 ChatBot: Hello there!")
        current_hints = [
            "Ask 'how are you?'",
            "Try asking 'what's your name?'",
            "Say 'help' to see options"
        ]
    elif any(phrase in user_input for phrase in commands['feelings']):
        print("🤖 ChatBot: I'm just a program, but I'm functioning well!")
        current_hints = [
            "Ask 'what time is it?'",
            "Try asking 'today's date?'"
        ]
    elif any(phrase in user_input for phrase in commands['identity']):
        print("🤖 ChatBot: I'm SimpleBot, your rule-based assistant!")
        current_hints = [
            "Say 'help' to see what I can do",
            "Try asking about the time or date"
        ]
    elif any(word in user_input for word in commands['time']):
        from datetime import datetime
        print(f"🤖 ChatBot: The current time is {datetime.now().strftime('%H:%M')}")
        current_hints = ["Ask about today's date", "Say 'help' for options"]
    
    elif any(word in user_input for word in commands['date']):
        from datetime import datetime
        print(f"🤖 ChatBot: Today is {datetime.now().strftime('%Y-%m-%d')}")
        current_hints = ["Ask what time it is", "Say 'your name'"]
    
    elif any(word in user_input for word in commands['help']):
        print("🤖 ChatBot: I can respond to:")
        print("- Greetings (hi, hello)")
        print("- How you're feeling")
        print("- Tell you my name")
        print("- Give current time/date")
        current_hints = ["Try any of these commands now!"]
    
    elif any(word in user_input for word in commands['exit']):
        print("🤖 ChatBot: Goodbye! Have a nice day!")
        break

    else:
        print("🤖 ChatBot: I didn't understand that.")
        current_hints = [
            "Try saying 'help' to see options",
            "Basic commands: hi, time, date, bye"
        ]