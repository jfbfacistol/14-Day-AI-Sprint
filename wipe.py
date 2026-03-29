import sqlite3

# 1. Connect to the vault
connection = sqlite3.connect("cre_vault.db")
cursor = connection.cursor()

# 2. The SQL Wipe Command: Delete every row inside the properties table
cursor.execute("DELETE FROM properties")

# 3. Lock the vault
connection.commit()
connection.close()

print("--- Vault successfully wiped clean ---")