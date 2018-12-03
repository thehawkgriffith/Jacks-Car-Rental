import numpy as np
import matplotlib.pyplot as plt
from env import Company
from env import Location

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


def generate(lam):
	n = np.random.randint(0, 21)
	done = False
	while not done and n > 0:
		prob_n = (np.e**(-lam))*(lam**n)*(1/np.math.factorial(n))
		if np.random.random() < prob_n:
			return n
		else:
			n -= 1
	return np.random.randint(0, 21)

def move(company, day):
	print("Day {} has come to an end, choose the number of vehices you want to move, and from what location.".format(day))
	print("Your current balance is ${}".format(company.balance))
	print("Current distribution is: Location 1 has {} cars and Location 2 has {} cars.".format(company.locations[0].n_cars, company.locations[1].n_cars))
	print("Enter number of vehices to move: ")
	num = int(input())
	print("From what location must the vehices be moved from? (A/B)")
	loc = input()
	if loc == 'A':
		loc = 0
	else:
		loc = 1
	return (num, loc)

def run_human(rent_lambda_1, return_lambda_1, rent_lambda_2, return_lambda_2, thresh,
	    company):
	game_over = False
	earning = []
	day = 0
	while not game_over:
		earning_today = company.balance
		company.rent(generate(rent_lambda_1), 0)
		company.rent(generate(rent_lambda_2), 1)
		company.return_cars(generate(return_lambda_1), 0)
		company.return_cars(generate(return_lambda_2), 1)
		num, loc = move(company, day)
		if loc == 0:
			company.move_a_to_b(num)
		else:
			company.move_b_to_a(num)
		earning_today = company.balance - earning_today
		earning.append(earning_today)
		day += 1
		if company.balance < thresh or day > 10:
			game_over = True
	return earning

def agent_action(loc, num, company):
	print("Current distribution is: Location 1 has {} cars and Location 2 has {} cars.".format(company.locations[0].n_cars, company.locations[1].n_cars))
	print("The agent is moving {} number of vehicles from location {}.".format(num, loc))

def run_ai(rent_lambda_1, return_lambda_1, rent_lambda_2, return_lambda_2, thresh,
	    company, agent, alpha, gamma):
	game_over = False
	earning = []
	day = 0
	s = (10, 10)
	a = (0, 0)
	while not game_over:
		earning_today = company.balance
		r = 0
		r += company.rent(generate(rent_lambda_1), 0)
		r += company.rent(generate(rent_lambda_2), 1)
		company.return_cars(generate(return_lambda_1), 0)
		company.return_cars(generate(return_lambda_2), 1)
		s_prime = (company.locations[0].n_cars, company.locations[1].n_cars)
		agent.Qtable[s][a] += alpha * (r + gamma * (np.max([agent.Qtable[s_prime][action] for action in agent.Qtable[s_prime]]) - agent.Qtable[s][a]))
		s = s_prime
		a_prime = agent.move(s_prime)
		a = a_prime
		loc, num = a_prime
		agent_action(loc, num, company)
		if loc == 0:
			company.move_a_to_b(num)
		else:
			company.move_b_to_a(num)
		earning_today = company.balance - earning_today
		earning.append(earning_today)
		day += 1
		if r < thresh or day > 100:
			game_over = True
	return earning

def plot(earning):
	x = np.arange(0, len(earning))
	plt.plot(x, earning, 2.0)
	plt.show()

company = Company()
agent = Agent()
rent_lambda_1 = 3
rent_lambda_2 = 4
return_lambda_1 = 3
return_lambda_2 = 2
thresh = -20
for _ in range(1000):
	earning = run_ai(rent_lambda_1, return_lambda_1, rent_lambda_2, return_lambda_2, thresh, company, agent, 0.1, 0.9)
#earning = run_human(rent_lambda_1, return_lambda_1, rent_lambda_2, return_lambda_2, thresh, company)
plot(earning)