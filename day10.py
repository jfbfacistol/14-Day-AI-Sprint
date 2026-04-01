# Day 10: The Export Engine
# Scenario: Extracting filtered CRE data from the SQLite vault 
# and automatically generating a stakeholder-ready CSV report.

import sqlite3
import csv

def export_large_properties(min_size: float):
    """Fetches large properties from the vault and exports them to a CSV report."""
    
    # --- PHASE 1: THE EXTRACTION (Day 9 Logic) ---
    connection = sqlite3.connect("cre_vault.db")
    cursor = connection.cursor()
    
    query_sql = """
    SELECT building_name, gla
    FROM properties
    WHERE gla > ?
    """
    
    cursor.execute(query_sql, (min_size,))
    large_buildings = cursor.fetchall()
    
    # --- PHASE 2: THE EXPORT ENGINE (Your Turn) ---
    
    # Step 1: Open a new file called 'large_properties_report.csv' in write ('w') mode.
    # Use the 'with open(...) as file:' syntax.
    with open("large_properties_report.csv", mode="w", newline="") as file:

        # Step 2: Inside the 'with' block, create a CSV writer object.
        # Example: writer = csv.writer(file)
        writer = csv.writer(file)

        # Step 3: Write the header row using writer.writerow()
        # Pass it a list of strings: ["Building Name", "GLA (sqm)"]
        writer.writerow(["Building Name", "GLA(sqm)"])

        # Step 4: Write the data. 
        # Since large_buildings is already a list of tuples, you can write them all 
        # at once using writer.writerows(large_buildings)
        writer.writerows(large_buildings)

    print(f"\nSUCCESS: Exported {len(large_buildings)} properties to CSV.")
    
    # --- PHASE 3: SECURE THE VAULT ---
    connection.close()


# --- EXECUTION PHASE ---
export_large_properties(2000.0)