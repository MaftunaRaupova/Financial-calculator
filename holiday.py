""" The code will calculate total holiday cost which includes flight, hotel and car rental. 
It will ask the user to choose the city, the lenght of stay and the car rental days. """

user_input_city = input("Please choose the city you would like to travel (London, Amsterdam, Egypt, New York, Dubai, Jordan): ")

num_nights = int(input("Please enter the number of days you would like to stay: "))

rental_days = int(input("Please enter the days you would like to rent a car: "))

#print(user_input, num_nights, rental_days)

""" the function below is for hotel_cost, which takes num_nights as an argument,
and return a total cost for the hotel stay. The different for each city. """

def hotel_cost(total_nights: int, city: str) -> int:
    city_cost_map = {"LONDON": 250, "AMSTERDAM": 200, "EGYPT": 150, "NEW YORK": 300, "Dubai": 500, "Jordan": 450}
    city_cost = city_cost_map[city.upper()]
    stay_cost = city_cost * total_nights
    return stay_cost

total_hotel_cost = hotel_cost(num_nights, user_input_city)

#print(total_hotel_cost)

"""the function below is for plane_cost, which takes city_flight as an argument
and return a cost for the flight. In function match case was used to calculate. 
"""
def plane_cost(city_flight: str) ->int:
    match city_flight.upper():
        case "LONDON":
            return 300
        case "AMSTERDAM": 
            return 350
        case "EGYPT": 
            return 250
        case "NEW YORK": 
            return 400
        case "Dubai": 
            return 500
        case "Jordan": 
            return 450
    
total_flight_cost = plane_cost(user_input_city)

#print(total_flight_cost)

"""this function is for car_rental, which takes rental_days as an argument
and return the total cost of the car rental. Fixed rate was given for daily rental cost. 
"""

def car_rental(rental_days):
    day_rental_cost = 50
    rental_cost = rental_days * day_rental_cost
    return rental_cost

total_car_rental = car_rental(rental_days)

#print(total_car_rental)

"""this function is for to calculate total holiday_cost, which takes three arguments
hotel_cost, plane_cost, car_rental. Using these three
arguments it returns a total cost for holiday."""

def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost

total_holiday_cost = holiday_cost(total_hotel_cost, total_flight_cost, total_car_rental)

print(f"Your total holiday cost is £{total_holiday_cost}")