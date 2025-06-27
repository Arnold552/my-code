# Add numbers entered by the user

total = 0
count = int(input("How many numbers do you want to add? "))

for i in range(count):
    num = float(input(f"Enter number {i+1}: "))
    total += num

print("The total sum is:", total)

