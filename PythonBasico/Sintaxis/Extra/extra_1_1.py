product_price = float(input("Enter the product price: "))
final_price = 0
if product_price < 100:
    final_price = product_price - (product_price * 0.02)
else:
    final_price = product_price - (product_price * 0.1)

print(f"The final price of the product is: {final_price}")