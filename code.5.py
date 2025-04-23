prices = {"rice": 60, "wheat": 40, "oil": 100}
quantities = {"rice": 2, "wheat": 3, "oil": 1}

total_bill = 0
for item in prices:
    total_bill += prices[item] * quantities.get(item, 0)

print("Total bill:", total_bill)
