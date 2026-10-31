#reflection questions 
#1.I was suprised about how I can access specific items using their positions in the lists using positive and negative indexing. I didn't expect the first item to be listed as 0, the second as 1, and so on. 
#2.I've actually never had to use excel so I don't have an experience with that to talk about. However, maybe a time using a python list  could save time is when I need to organize information for a school project. I could store all the topics I need to research in one list and easily add or remove topics as I work instead of keeping track of them one by one.

print("---Exercise 1---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("---Exercise 2---")
print(inventory[0]) #first item
print(inventory[-1]) #last item
middle = len(inventory) // 2 #calculate the index of the middle
print(inventory[middle]) #middle item

print("---Exercise 3---")
print(inventory[:3]) #first 3 items
print(inventory[-2:]) #last 2 items
print(inventory[::2]) #every second item

print("---Exercise 4---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("---Exercise 5---")
coords = (40.7128, -784.0060)
try:
    coords[0]=99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident")
print(coords)

print("---Exercise 6---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("---Exercise 7---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price* .9, 2))
print("Original prices:", prices)
print("Discounts:", discount)

print("---Exercise 8---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)
print("High sales:", high_sales)
print(f"Count:", {len(high_sales)})
print(f"Average:, {sum(high_sales) / len(high_sales):.2f}")
