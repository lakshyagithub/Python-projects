class the_2_and_only_cars:
	car_0 = input("Tell me your car name:")
	car_1 = "honda city vx"
	car_2 = "honda amaze sv"

	def main(self):
		print("I have:", self.car_1)
		print("I have:", self.car_2)

the_only_2_cars = the_2_and_only_cars()
print("Your car:", the_only_2_cars.car_0)
the_only_2_cars.main()