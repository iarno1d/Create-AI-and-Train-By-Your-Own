import os
import webbrowser

def handle_command(command, speak):
    """Handles specific commands like opening applications or websites."""
    command = command.lower()

    if "open music" in command:
        music_path = "C:/Users/YourUsername/Music"  # Update to your music folder or player path
        os.startfile(music_path)
        response = "Opening music."
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube."
    elif "open browser" in command:
        webbrowser.open("https://www.google.com")
        response = "Opening browser."
    elif "shutdown" in command:
        os.system("shutdown /s /t 1")
        response = "Shutting down the system."
    else:
        response = None

    if response:
        print(response)
        speak(response)
    return response
