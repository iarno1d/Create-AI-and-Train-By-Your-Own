from command_handler import handle_command

def handle_question(voice_recognizer, knowledge_manager, knowledge_processor, speak):
    """Main logic for handling a user's question or command."""
    print("Choose an input method:")
    print("1. Speak your question.")
    print("2. Type your question.")
    choice = input("Your choice (1/2): ").strip()

    if choice == '1':
        print("Listening...")
        question = voice_recognizer.recognize_voice().strip()
    elif choice == '2':
        question = input("Type your question: ").strip()
    else:
        print("Invalid choice. Please try again.")
        speak("Invalid choice. Please try again.")
        return

    if not question:
        print("No input received. Please try again.")
        speak("No input received. Please try again.")
        return

    print(f"You said: {question}")

    # First check for known commands
    response = handle_command(question, speak)
    if response:
        return

    # Process as a general question
    answer = knowledge_processor.find_answer(question)
    if answer:
        print(f"Answer: {answer}")
        speak(answer)
    else:
        print("I don't know the answer to that. Please choose an option:")
        speak("I don't know the answer to that. Please choose an option.")
        while True:
            print("\nOptions:")
            print("1. Teach me the answer.")
            print("2. Ask another question.")
            print("3. Exit.")
            print("4. Provide text input.")
            choice = input("Your choice (1/2/3/4): ").strip()

            if choice == '1':
                provide_answer(question, knowledge_manager, speak)
                break
            elif choice == '2':
                print("Ask your next question.")
                speak("Ask your next question.")
                return
            elif choice == '3':
                print("Goodbye!")
                speak("Goodbye!")
                exit(0)
            elif choice == '4':
                print("You can now provide input as text:")
                handle_question(voice_recognizer, knowledge_manager, knowledge_processor, speak)
                break
            else:
                print("Invalid choice. Please try again.")
                speak("Invalid choice. Please try again.")

def provide_answer(question, knowledge_manager, speak):
    """Prompts the user to provide an answer for a question."""
    print("Please provide the answer:")
    speak("Please provide the answer.")
    new_answer = input("Your answer: ").strip()
    if new_answer:
        knowledge_manager.update_knowledge_base(question, new_answer)
        print("Thank you! I've learned something new.")
        speak("Thank you! I've learned something new.")
    else:
        print("No answer provided.")
        speak("No answer provided.")
