class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5 if self.__speed >= 5 else 0

    def get_speed(self):
        return self.__speed


# Main program
my_car = Car(2022, "Toyota")

# Accelerate 5 times
print("Accelerating:")
for _ in range(5):
    my_car.accelerate()
    print(f"Current speed: {my_car.get_speed()} mph")

# Brake 5 times
print("\nBraking:")
for _ in range(5):
    my_car.brake()
    print(f"Current speed: {my_car.get_speed()} mph")
