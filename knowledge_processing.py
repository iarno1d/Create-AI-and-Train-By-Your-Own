from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class KnowledgeProcessor:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def find_answer(self, question):
        """
        Matches the user's question with the knowledge base.
        Returns the best matching answer or None if no match is found.
        """
        questions = list(self.knowledge_base.keys())
        if not questions:
            return None
        
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(questions + [question])
        
        similarities = cosine_similarity(vectors[-1], vectors[:-1])
        max_similarity = similarities.max()
        
        if max_similarity > 0.7:  # Adjustable similarity threshold
            best_match = questions[similarities.argmax()]
            return self.knowledge_base[best_match]
        return None
