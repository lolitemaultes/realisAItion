# agent.py

import random
import time

class AutonomousAgent:
    def __init__(self, agent_id, memory, ethics):
        self.agent_id = agent_id
        self.memory = memory
        self.ethics = ethics
        self.task = None

    def assign_task(self, task):
        self.task = task
        print(f"[Agent-{self.agent_id}] Assigned task: {task}")

    def run(self):
        if not self.task:
            print(f"[Agent-{self.agent_id}] No task assigned.")
            return None

        print(f"[Agent-{self.agent_id}] Working on task...")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate processing

        # Placeholder for actual AI logic
        result = {
            "agent_id": self.agent_id,
            "task": self.task,
            "result": f"Findings on {self.task}",
            "ethics_check": self.ethics.validate(self.task)
        }

        self.memory.add_discovery(result)
        return result
