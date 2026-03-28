# The Scenario: Constructing the Data Vault
# Your manager needs a secure, permanent storage solution for the transformed property data. 
# You must use Python's built-in database library to generate a local SQLite database and construct an empty table with the correct schema to hold your dictionaries.

import sqlite3

connection = sqlite3.connect("cre_vault.db")

cursor = connection.cursor()

vault_sql = """
CREATE TABLE IF NOT EXISTS properties  (
    id INTEGER PRIMARY KEY,
    building_name TEXT,
    price REAL,
    gla REAL
)
"""

cursor.execute(vault_sql)
connection.commit()
connection.close()