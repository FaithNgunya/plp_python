def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# Prompt the user for the original price and discount percentage
try:
    price = float(input("Enter the original price of the item (e.g., 100.00): KSH "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price after applying the discount
    final_price = calculate_discount(price, discount_percent)

    # Print the final price
    if final_price != price:
        print(f"The final price after applying the discount is: KSH {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: KSH {price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
