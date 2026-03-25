# Day 4: Dictionary - navigating and creating dictionary

# --- THE RAW DATA ---
building_name = "Eastwood Global Plaza"
raw_price = "  PHP 150,000,000.00 "
raw_size = "2500 sqm"

def clean_price(raw_price):
    # Strip all leading and trailing whitespace. 
    # Remove the lowercase letters PHP
    clean_number = raw_price.strip().replace("PHP", "").replace(",","")
    return float(clean_number)

def clean_size(raw_size):
    # Strip all leading and trailing whitespace. 
    # Remove the lowercase letters "sqm"
    clean_area = raw_size.strip().replace("sqm", "")
    return float(clean_area)


property_profile = {
    "name" : building_name,
    "price" : clean_price(raw_price),
    "gla" : clean_size(raw_size)
}

print(f"--- System Payload ---\n {property_profile}")
print(f"Target Price Extraction: {property_profile['price']}")
