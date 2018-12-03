import numpy as np
class Agent():

	def __init__(self):
		self.policy = {}
		self.actions = []
		states = []
		for i in range(2):
			for j in range(6):
				self.actions.append((i, j))
		for i in range(21):
			for j in range(21):
				states.append((i, j))
		self.Qtable = {}
		for state in states:
			self.Qtable[state] = {}
			for action in self.actions:
				self.Qtable[state][action] = 0

	def move(self, state, epsilon = 0.1):
		if np.random.random() < epsilon:
			return agent.actions[np.random.randint(0, len(agent.actions))]
		else:
			action_value = 0
			best_action = (0, 0)
			for action in self.Qtable[state]:
				if self.Qtable[state][action] >= action_value:
					action_value = self.Qtable[state][action]
					best_action = action
			return best_action


