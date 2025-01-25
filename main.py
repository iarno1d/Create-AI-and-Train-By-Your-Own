import pyttsx3
from voice_recognition import VoiceRecognizer
from knowledge_management import KnowledgeManager
from knowledge_processing import KnowledgeProcessor
from question_handler import handle_question

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Initialize modules
    engine = pyttsx3.init()
    voice_recognizer = VoiceRecognizer(model_path="AR AI Project/vosk-model-small-en-us-0.15")     #US Model
    knowledge_manager = KnowledgeManager(knowledge_file="AR AI Project/knowledge_base.json")
    knowledge_processor = KnowledgeProcessor(knowledge_manager.knowledge_base)

    print("AI Assistant is ready. Speak your question!")
    try:
        while True:
            handle_question(voice_recognizer, knowledge_manager, knowledge_processor, speak)
    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")
        speak("Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("An error occurred. Please try again.")
