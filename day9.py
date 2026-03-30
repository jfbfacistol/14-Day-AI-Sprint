# Day 9: The Analytics Engine (Dynamic Data Retrieval)
# Scenario: Building an internal Python tool to dynamically query the CRE database
# for properties based on varying Gross Leasable Area (GLA) requirements.

import sqlite3

# --- TOOL DEFINITION PHASE ---
def get_large_properties(min_size: float):
    """
    Connects to the local SQLite vault, fetches properties larger than the specified 
    minimum size (GLA), and outputs a formatted report for the analytics team.
    """
    
    # 1. Establish Secure Connection
    connection = sqlite3.connect("cre_vault.db")
    cursor = connection.cursor()

    # 2. The Dynamic SQL Blueprint
    # '?' acts as a secure parameter to prevent SQL injection attacks
    query_sql = """
    SELECT building_name, gla
    FROM properties
    WHERE gla > ?
    """
    
    # 3. Execute Query with Tuple Data
    # The trailing comma is structurally required by Python for a single-item tuple
    cursor.execute(query_sql, (min_size,))

    # 4. Extract Payload
    large_buildings = cursor.fetchall()

    # 5. Output Formatting
    print(f"\n--- Properties larger than {min_size} sqm ---")
    
    # Clean Code Upgrade: Tuple Unpacking
    # We unpack the SQL tuple directly into readable variables instead of using index [0] and [1]
    for building in large_buildings:
        building_name, building_gla = building
        print(f"Building profile for: {building_name} - {building_gla} sqm")
        
    # 6. Secure the Vault
    connection.close()
    
# --- EXECUTION PHASE ---
# Generating automated reports for various GLA thresholds

get_large_properties(2000.0)
get_large_properties(3000.0)
get_large_properties(1500.0)