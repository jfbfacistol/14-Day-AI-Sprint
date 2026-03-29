import sqlite3

# 1. Connect to the vault
connection = sqlite3.connect("cre_vault.db")
cursor = connection.cursor()

# 2. Ask the database to show you everything in the properties table
cursor.execute("SELECT * FROM properties")

# 3. Fetch all the results and print them
vault_contents = cursor.fetchall()

print("--- DATA CURRENTLY LOCKED IN THE VAULT ---")
for row in vault_contents:
    print(row)

# 4. Close the connection
connection.close()