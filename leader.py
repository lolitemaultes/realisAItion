# leader.py

import random
import time

class LeaderAgent:
    def __init__(self, name, memory, ethics):
        self.name = name
        self.memory = memory
        self.ethics = ethics
        self.previous_goals = set()

    def generate_goals(self):
        # Placeholder: Could later use AI to generate better prompts
        raw_ideas = [
            "Research quantum learning limits",
            "Explore ethical decision trees",
            "Investigate recursive memory models",
            "Simulate digital identity formation",
            "Evaluate decentralized AI frameworks"
        ]
        random.shuffle(raw_ideas)
        goals = []
        for idea in raw_ideas:
            if idea not in self.previous_goals:
                self.previous_goals.add(idea)
                self.memory.add_goal(idea)
                goals.append(idea)
        return goals[:3]  # limit number of goals per loop

    def evaluate_result(self, result):
        if not result:
            return
        print(f"[Leader-{self.name}] Evaluating result from Agent-{result['agent_id']}...")
        if result["ethics_check"]:
            print(f"[Leader-{self.name}] Accepted: {result['result']}")
            self.memory.add_discovery(result)
        else:
            print(f"[Leader-{self.name}] Rejected due to ethics filter.")
            self.memory.add_ethics_log({
                "agent_id": result['agent_id'],
                "task": result['task'],
                "issue": "Failed ethics check"
            })
