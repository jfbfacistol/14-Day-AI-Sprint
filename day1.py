# Create the list of dummy CRE prices
cre_prices = [45000000, 12000000, 85000000, 30000000, 60000000]
# Start  the counter at zero
budget_count = 0

# Loop through every price in the list
for price in cre_prices:
    # Check if the price is a premium property
    if price < 40000000:
        print(f"Budget Property found: {price}")
        # Add 1 to the counter every time we find a match
        budget_count = budget_count + 1

print(f"Total budget properties: {budget_count}")