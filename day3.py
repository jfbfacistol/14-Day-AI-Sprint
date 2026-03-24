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

# --- THE INTEGRATION CHALLENGE ---
# Scenario: A manager needs a batch of unformatted property prices cleaned automatically.
# Goal: Synthesize Day 1 (Loops) and Day 3 (Functions) to process an array of messy data 
# without rewriting the .replace() and .strip() logic.

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

# --- THE DEFENSIVE CHALLENGE ---
# Scenario: A broken PDF scraper returns "TBA" instead of a price.
# Goal: Prevent a float() conversion error from crashing the whole pipeline.

broken_data = [
    "PHP 50,000,000.00",
    "TBA",  # This will cause a crash!
    "PHP 25,000,000.00"
]

def clean_property_price(raw_price):
    # 1. Basic cleaning to remove whitespace
    clean_text = raw_price.strip()
    
    # 2. THE ESCAPE HATCH (Defensive Check)
    # If data is missing or non-numeric, return 0.0 to keep the loop alive.
    if clean_text == "TBA" or clean_text == "":
        print(f"DEBUG: Found broken data '{clean_text}'. Defaulting to 0.0")
        return 0.0
    
    # 3. Standard Transformation
    clean_text = clean_text.replace("PHP ", "").replace(",", "")
    
    # 4. Final Casting
    return float(clean_text)

# --- TESTING THE DEFENSE ---
broken_data = [
    "PHP 50,000,000.00",
    "TBA", 
    "PHP 25,000,000.00"
]

print("--- Starting Defensive Batch Process ---")
for item in broken_data:
    price = clean_property_price(item)
    print(f"Final Validated Price: {price}")