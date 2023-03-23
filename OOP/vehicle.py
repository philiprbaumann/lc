# Small OOP exercise to get used to class structuring and the power of super() and __init__.
class Vehicle:

	def __init__(self, max_speed, mileage, capacity):
		self.max_speed = max_speed
		self.mileage = mileage
		self.color = "Yellow"
		self.capacity = capacity

	def print(self):
		print(f"This {self.color} vehicle goes {self.max_speed} miles an hour for {self.mileage} per gallon.")

	def fare(self):
		return int(self.capacity) * 100

class Bus(Vehicle):
	def __init__(self, max_speed, mileage):
		super().__init__(max_speed, mileage, 50)

	def fare(self):
		return (super().fare() * 1.1)

class Car(Vehicle):
	pass


v = Vehicle(120, 15, 100)
v.print()
b = Bus(50, 15)
b.print()
print(f"The bus costs {b.fare()} and all other vehicles cost {v.fare()}.")
print(isinstance(b,Vehicle))