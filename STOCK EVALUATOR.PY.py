total_profit_loss = 0
num_stocks = int(input("How many different stocks did you trade? "))
for i in range(num_stocks):
    print(f"\n--- Stock {i+1} ---")
    stock_name = input("Enter stock name: ")
    buying_price = float(input("Enter buying price per stock: "))
    selling_price = float(input("Enter selling price per stock: "))
    quantity = int(input("Enter quantity: "))
    total_cost = buying_price * quantity
    total_revenue = selling_price * quantity
    profit_or_loss = total_revenue - total_cost
    total_profit_loss += profit_or_loss
    print(f"\nResult for {stock_name}:")
    if profit_or_loss > 0:
        print(f"Profit: {profit_or_loss}")
    elif profit_or_loss < 0:
        print(f"Loss: {abs(profit_or_loss)}")
    else:
        print("No profit, no loss")
print("\n====== FINAL SUMMARY ======")
if total_profit_loss > 0:
    print(f"Total Profit: {total_profit_loss}")
elif total_profit_loss < 0:
    print(f"Total Loss: {abs(total_profit_loss)}")
else:
    print("Overall: No profit, no loss")
