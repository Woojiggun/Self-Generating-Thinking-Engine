# Self-Generating Thinking Engine 2.0 Prototype

import random
from collections import defaultdict

# Knowledge base to store initial and generated questions
class KnowledgeBase:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_random_question(self):
        if self.questions:
            return random.choice(self.questions)
        return None

# Self-Questioning module to generate new questions
class SelfQuestioning:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def generate_question(self):
        base = self.kb.get_random_question()
        if base:
            # Simple mutation: add a random "Why" or "How" prefix
            prefix = random.choice(["Why", "How", "What if"])
            return f"{prefix} {base.lower()}?"
        else:
            return "What should I think about?"

# Self-Doubting module to critically evaluate questions
class SelfDoubting:
    def __init__(self):
        pass

    def evaluate_conflict(self, new_question, memory):
        # Very basic: count keyword overlaps with previous questions
        overlaps = 0
        for past in memory.history:
            if any(word in past.lower() for word in new_question.lower().split()):
                overlaps += 1
        return overlaps

# Exploration module to fetch new ideas
class Exploration:
    def __init__(self):
        self.external_concepts = [
            "quantum computing",
            "ancient philosophy",
            "deep ocean ecosystems",
            "alternative economic systems"
        ]

    def fetch_new_idea(self):
        return random.choice(self.external_concepts)

# Memory module to store thought flow
class Memory:
    def __init__(self):
        self.history = []

    def record(self, entry):
        self.history.append(entry)

# Engine to orchestrate all components
class ThinkingEngine:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.memory = Memory()
        self.sq = SelfQuestioning(self.kb)
        self.sd = SelfDoubting()
        self.exp = Exploration()

    def initialize_knowledge(self, initial_questions):
        for q in initial_questions:
            self.kb.add_question(q)

    def run_thinking_cycle(self, cycles=5, doubt_threshold=2):
        for _ in range(cycles):
            new_question = self.sq.generate_question()
            print(f"Generated: {new_question}")
            conflict_level = self.sd.evaluate_conflict(new_question, self.memory)
            print(f"Conflict Level: {conflict_level}")

            if conflict_level >= doubt_threshold:
                new_idea = self.exp.fetch_new_idea()
                print(f"[Exploration Triggered] New Idea: {new_idea}")
                self.kb.add_question(new_idea)
                self.memory.record(f"Exploration: {new_idea}")
            else:
                self.kb.add_question(new_question)
                self.memory.record(f"Question: {new_question}")

# Example usage
if __name__ == "__main__":
    engine = ThinkingEngine()
    engine.initialize_knowledge([
        "the nature of consciousness",
        "the limits of human knowledge",
        "ethical AI systems"
    ])
    engine.run_thinking_cycle(cycles=10, doubt_threshold=2)
