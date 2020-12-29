cars = 100
space_in_a_car = 3.2
space_in_a_car_int = 3
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#Test flotantes y enteros

proInt = cars_driven * space_in_a_car_int
proFlo = cars_driven * space_in_a_car

print(f'Este es mi producto de un entero con un flotante: {proFlo}, este e mi producto con un entero y otro entero {proInt}')

divFlo = cars_driven / space_in_a_car
divInt = cars_driven / space_in_a_car_int
print(f'Este es mi residuo de un entero sobre un flotante: {divFlo}, y esto mi división entre dos enteros:  {divInt} \n')

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")




