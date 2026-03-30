product = input("Enter the product (cone, cup, banana split): ").lower()
quantity = int(input("Enter the quantity: "))

price = 0

if product == "cone":
    price = 3000
elif product == "cup":
    price = 4000
elif product == "banana split":
    price = 9000
else:
    print("Invalid product")

total = price * quantity

print("Total to pay:", total)