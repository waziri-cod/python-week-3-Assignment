def calculate_discount(price, discount_percent):    
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


price = float(input("Enter the original price of the item (in TZS): "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"The final price after a {discount_percent}% discount is: {final_price:.2f} TZS")
else:
    print(f"No discount applied. The price remains: {final_price:.2f} TZS")

