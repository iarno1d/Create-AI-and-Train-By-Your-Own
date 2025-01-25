import json
import os

class KnowledgeManager:
    def __init__(self, knowledge_file):
        self.knowledge_file = knowledge_file
        self.knowledge_base = self.load_knowledge_base()

    def load_knowledge_base(self):
        """Loads the knowledge base from a file, creating a new one if it doesn't exist."""
        if os.path.exists(self.knowledge_file):
            try:
                with open(self.knowledge_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Knowledge base file corrupted. Starting fresh.")
        return {}

    def update_knowledge_base(self, question, answer):
        """Adds a new question-answer pair and saves the knowledge base."""
        self.knowledge_base[question] = answer
        self.save_knowledge_base()

    def save_knowledge_base(self):
        """Saves the current knowledge base to a file."""
        with open(self.knowledge_file, "w") as file:
            json.dump(self.knowledge_base, file, indent=4)
