# Day 7: The Relational Data Vault (Database Architecture)
# Scenario: Establishing a secure, permanent SQLite storage solution to house 
# the transformed Commercial Real Estate property data and our broker network.

import sqlite3

# --- DATABASE CONNECTION PHASE ---
# Initialize connection to the local vault (creates the .db file if it does not exist)
connection = sqlite3.connect("cre_vault.db")
cursor = connection.cursor()

# --- SCHEMA DEFINITION PHASE ---

# Blueprint 1: The Properties Table
vault_sql = """
CREATE TABLE IF NOT EXISTS properties (
    id INTEGER PRIMARY KEY,
    building_name TEXT,
    price REAL,
    gla REAL
)
"""

# Blueprint 2: The Brokers Table
broker_sql = """
CREATE TABLE IF NOT EXISTS brokers (
    broker_id INTEGER PRIMARY KEY,
    full_name TEXT,
    agency_name TEXT,
    years_active INTEGER
)
"""

# --- EXECUTION & SECURITY PHASE ---

# Execute both blueprints sequentially
cursor.execute(vault_sql)
cursor.execute(broker_sql)

# Commit the schemas to the hard drive and lock the connection
connection.commit()
connection.close()