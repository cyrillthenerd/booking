# Simple python booking app
print("Starting lossless booking engine")

#Destinations
destination = {"1": "London",
                "2": "Paris",
                "3": "Amsterdam",
                "4": "New York",
                "5": "Los Angeles",
                "6": "Manila",
                "7": "Singapore"}

#Departure Times
departure_time = {"1": "8:00",
                "2": "12:00",
                "3": "16:00",
                "4": "20:00",}

#Flight Prices
flight_prices = {"1": "250",
                "2": "200",
                "3": "180",
                "4": "165",}


def departure_destination_list():
    for keys, values in destination.items():
        print(keys, values)

def departure_time_list():
    for keys, values in departure_time.items():
        print(keys, values)

def booking_departure_destination():
    destination: str = input("Where would you like to fly?")
    if int(destination) >= 1 and int(destination) <= 7:
        return destination
    else:
        print("You entered the wrong number")


def booking_departure_time():
    time: str = input("When would you like to fly?")
    if int(time) >= 1 and int(time) <= 4:
        return time
    else:
        print("You entered the wrong number")


departure_destination_list()
target_destination = booking_departure_destination()
departure_time_list()
target_departure = booking_departure_time()

username = str(input("Hi there! Please type in your name so we know who you are."))

if not username:
    print("False input...")

passport_number = str(input("Enter your passport number here:"))

print("You have chosen to fly to "+ destination[target_destination] + " and your flight leaves at " + departure_time[target_departure] + " and costs " + flight_prices[target_departure] + "$.")

f= open("Booking_Reference.txt","w+")

f.write("Hello " + username + " we are happy to give you confirmation that you booked a trip to " + destination[target_destination] + " at " + departure_time[target_departure])
f.write("\nBelow you will find a summary of your trip.")
f.write("\nYour name: " + username)
f.write("\nYour passport number: " + passport_number)
f.write("\nTravel destination: " + destination[target_destination])
f.write("\nDeparture flight time: " + departure_time[target_departure])
f.write("\nTotal cost of your trip: " + flight_prices[target_departure] + "$.")

print("Thank you for booking with Fuck You Airlines!")