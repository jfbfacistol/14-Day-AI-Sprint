# Day 3: Building the Cleaning Machine

def clean_property_price(raw_price):
    # The machine takes whatever 'raw_price' is given and cleans it
    step_1 = raw_price.strip()
    step_2 = step_1.replace("PHP ", "")
    clean_text = step_2.replace(",", "")
    
    # Cast it to a number
    final_number = float(clean_text)
    
    # The machine spits the final number back out
    return final_number

# --- TESTING THE MACHINE ---

# We don't have to write the logic again, we just use the tool!
test_string_1 = " PHP 150,000,000.00 "
test_string_2 = "PHP 8,500,000.00  "

print(f"Cleaned Data 1: {clean_property_price(test_string_1)}")
print(f"Cleaned Data 2: {clean_property_price(test_string_2)}")

# --- THE INTEGRATION BOSS FIGHT ---
monthly_report = [
    "PHP 45,000,000.00",
    "  PHP 12,500,000.00 ",
    "PHP 85,000,000.00",
    "   PHP 5,000,000.00  "
]

for raw_string in monthly_report:
    # Call the function to simply the cleaning
    clean_number = clean_property_price(raw_string)
    
    print(f"Machine processed: {clean_number}")
    
print("--- Monthly Report Complete ---")