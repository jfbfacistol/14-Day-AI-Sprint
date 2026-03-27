# Day 6: The Master Database (ETL Pipeline)
# Scenario: Extracting local CSV data, transforming messy CRE strings into mathematical floats, 
# and loading them into structured dictionary payloads for downstream database ingestion.

def clean_price(raw_price):
    # Business Logic: CRE PDFs often export with inconsistent currency prefixes and commas.
    clean_number = raw_price.strip().replace("PHP", "").replace(",", "")
    
    # Defensive check: Unpriced listings default to "TBA". Catch to prevent pipeline crash.
    if clean_number == "TBA":
        return 0.0
        
    return float(clean_number)

def clean_size(raw_size):
    # Format normalization: Strip standard "sqm" text to allow mathematical operations
    clean_area = raw_size.strip().replace("sqm", "")
    return float(clean_area)

# Initialize the master payload container
master_database = []

# --- EXTRACT PHASE ---
with open('properties.csv', 'r') as file_object:
    content = file_object.readlines()
    # Skip index 0 to drop the CSV header row
    data_rows = content[1:]
    
print("--- Initiating CRE Data Pipeline ---")

# --- TRANSFORM & LOAD PHASE ---
for row in data_rows:
    split_row = row.strip().split(",")
    
    building_name = split_row[0]
    raw_price = split_row[1]
    raw_size = split_row[2]
    
    # Pass raw data through cleaning engines
    final_price = clean_price(raw_price)
    final_size = clean_size(raw_size)
    
    print(f"Building profile for: {building_name}")

    # Structure the payload
    property_profile = {
        "name": building_name,
        "price": final_price,
        "gla": final_size
    }

    # Load into master database
    master_database.append(property_profile)
            
print("--- Pipeline Complete ---\n")
print(f"[System Payload Database]:\n{master_database}")