# Excersise 1:
print("--- Excersise 1: Build the list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Excersise 2

print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2
print(inventory[middle]) # middle item


# Excersise 3
print(inventory[:3]) # first 3 items
print(inventory[:-2]) # last two
print(inventory[::2]) # every second item



# #xcersise 4
inventory.append("envelope") # added tape to the end
print(inventory) # output: ['pen','notebook', ]
inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# excersise 5
coords = (40.7128, -784.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")


# Excersisee 6
sales = 2 [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

# Excersise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discout = []
for prices in prices:
    discount.append(round(price * .9, 2))

print("original prices:", price)
print("Discounts:", discount)

# Excersise 8
sales = [340, 127, 589, 240, 467, 88, 731, 315, 62, 490]
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High Sales:", high_sales)
print(f"Count: {len(high_sales(}")
print(f"Average: {sum(high_sales) / len(high_sales:.2f))}")
