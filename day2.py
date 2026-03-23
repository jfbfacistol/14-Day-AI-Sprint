#  Day 2: String Cleaning
raw_price = " PHP 125,000,000.00 "

# 1. .strip() removes the invisible spaces at the very beginning and end
step_1 = raw_price.strip()

# 2. .replace() swaps the "PHP " text with absolutely nothing ("")
step_2 = step_1.replace("PHP ", "")

# 3. .replace() removes the commas
final_clean_price = step_2.replace(",","")

# Print the visual proof
print(f"Original messy data: '{raw_price}'")
print(f"Machine-ready data: '{final_clean_price}'")

# 4. Convert the text into a decimal number (float)
numeric_price = float(final_clean_price)

# 5. Now we can do math! Let's calculate a 5% broker commission
commission = numeric_price * 0.05

print(f"Mathematical Float: {numeric_price}")
print(f"5% Broker Comission: {commission}")

# Exercise
# A manager just handed you a completely unfformatted, garbage list of property price extracted from a broken PDF.
# They need to know exactly how many of these properties are Premium (valued at exactly or over 50,000,000).

# --- THE BOSS FIGHT ---
messy_portfolio = [
    "  PHP 85,000,000.00 ",
    "PHP 12,500,000.00",
    "   PHP 60,000,000.00",
    "PHP 30,000,000.00  "
]

# Start with counter in zero
counter = 0

# for loop for each prices
for raw_price in messy_portfolio:
        # 1. CLEAN IT FIRST (Bring it into the machine-readable state)
        clean_price =  raw_price.strip().replace("PHP ", "").replace(",","")
        # 2. CAST IT (Turn it into a real number)
        new_price = float(clean_price)
        # 3. NOW CHECK IT (Now that it's a number, we can do math)        
        if new_price >= 50000000:
            print(f"Premium property found!: {new_price}")
            counter = counter + 1
        
print(f"Final total count: {counter}")         
