import numpy as np

class Location():

	def __init__(self):
		self.n_cars = 10

	def retrieve(self, num):
		self.n_cars -= num

	def store(self, num):
		self.n_cars += num
		if self.n_cars > 20:
			self.n_cars = 20

class Company():

	def __init__(self):
		self.location_a = Location()
		self.location_b = Location()
		self.locations = [self.location_a, self.location_b]
		self.balance = 10
		self.rented = {0:0, 1:0}

	def move_a_to_b(self, num):
		if num > self.location_a.n_cars:
			return
		if num <= 5 and self.balance >= 2 * num:
			self.location_a.retrieve(num)
			self.location_b.store(num)
			self.balance -= 2 * num

	def move_b_to_a(self, num):
		if num > self.location_b.n_cars:
			return
		if num <= 5 and self.balance >= 2 * num:
			self.location_b.retrieve(num)
			self.location_a.store(num)
			self.balance -= 2 * num

	def rent(self, num, loc):
		if num > self.locations[loc].n_cars:
			self.rented[loc] += self.locations[loc].n_cars
			c = self.locations[loc].n_cars
			self.balance += 10 * self.locations[loc].n_cars
			self.locations[loc].n_cars = 0
			return -(num - c)
		else:
			self.rented[loc] += num
			self.balance += 10 * num
			self.locations[loc].retrieve(num)
			return num

	def return_cars(self, num, loc):
		self.locations[loc].store(num)
		self.rented[loc] -= num
