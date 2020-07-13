# Excercise 1
# print("Carpool Report")
# total_cars = 100
# total_drivers = 100
# today_drivers = 30
# today_passengers = 90
# empty_cars = total_cars-today_drivers
# today_seats = today_drivers*4
# average_pas_car = today_passengers/(today_drivers)


# def report():
#     print(f"Number of cars available: {total_cars}")
#     print(f"Number of drivers registered: {total_drivers}")
#     print(f"Number of empty cars: {empty_cars}")
#     print(f"Number of today´s available seats: {today_seats}")
#     print(f"Averga passengers per car: {average_pas_car}")


# report()

# Excercise 2
import re

while True:
    password = input("please insert a new password: ")
    pattern = re.compile(r"([a-z])([A-Z])([0-9])([$  # @])")
    x = pattern.findall(password)
    if len(password) < 6 or len(password) > 12:
        print("password must have between 6 and 12 characters.")
    elif x:
        break
