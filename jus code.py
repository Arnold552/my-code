
standard_price = 12000
vegetarian_price = 10000
deluxe_price = 15000

current_hour = int(input("Enter current hour (0-23): "))
if current_hour < 7 or current_hour > 19:
    print("Cafeteria is closed. Orders accepted from 7:00 to 19:00.")
else:
    print("Welcome to the Campus Cafeteria!")
    print("1. Standard Meal - 12000 UGX")
    print("2. Vegetarian Meal - 10000 UGX")
    print("3. Deluxe Meal - 15000 UGX")

    s = int(input("Enter number of Standard Meals: "))
    v = int(input("Enter number of Vegetarian Meals: "))
    d = int(input("Enter number of Deluxe Meals: "))

    total_meals = s + v + d
    total_price = (s * standard_price) + (v * vegetarian_price) + (d * deluxe_price)

    if total_meals > 3:
        discount = total_price * 0.1
    else:
        discount = 0

    final_price = total_price - discount

    print("\nOrder Summary:")
    print("Standard Meals:", s)
    print("Vegetarian Meals:", v)
    print("Deluxe Meals:", d)
    print("Total meals:", total_meals)
    print("Discount:", int(discount), "UGX")
    print("Total to pay:", int(final_price), "UGX")