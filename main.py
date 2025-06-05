# Project LIBRA - main.py

import os
import json
import time
import threading
from memory import MemoryManager
from agent import AutonomousAgent
from leader import LeaderAgent
from ethics import EthicsEngine
from config import CONFIG


def initialize_system():
    print("[LIBRA] Initializing persistent memory...")
    memory = MemoryManager(CONFIG['memory_path'])

    print("[LIBRA] Loading ethical framework...")
    ethics = EthicsEngine(CONFIG['ethics_profile'])

    print("[LIBRA] Spawning leader agent...")
    leader = LeaderAgent(name="NOVA", memory=memory, ethics=ethics)

    print("[LIBRA] Deploying worker agents...")
    agents = []
    for i in range(CONFIG['num_agents']):
        agent = AutonomousAgent(agent_id=i, memory=memory, ethics=ethics)
        agents.append(agent)

    return leader, agents


def run_loop(leader, agents):
    while True:
        print("[LIBRA] Evaluating research goals...")
        goals = leader.generate_goals()

        print(f"[LIBRA] Distributing {len(goals)} tasks...")
        for i, goal in enumerate(goals):
            agent = agents[i % len(agents)]
            agent.assign_task(goal)

        print("[LIBRA] Collecting findings...")
        for agent in agents:
            result = agent.run()
            leader.evaluate_result(result)

        print("[LIBRA] Archiving state and sleeping...\n")
        leader.memory.save_state()
        time.sleep(CONFIG['loop_interval'])


if __name__ == "__main__":
    leader, agents = initialize_system()
    run_loop(leader, agents)
