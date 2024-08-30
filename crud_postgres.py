import psycopg2

cur = None  # Initialize cur to handle NameError in finally block

try:
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",  # Ensure this is the correct username
        password="1234567890",  # Ensure this is the correct password
        host="localhost",
        port="5432"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Create the interns table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS interns (
            id INT PRIMARY KEY,
            name VARCHAR(100),
            address VARCHAR(100)
        )
    ''')
    conn.commit()
    print("Table created successfully (if it didn't exist)")

    # Create (Insert) two records
    cur.execute("INSERT INTO interns (name, address) VALUES (%s, %s)", ('Archana SApkota', 'Kapan'))
    cur.execute("INSERT INTO interns (name, address) VALUES (%s, %s)", ('Ashmita Basnet', 'Kapan'))
    conn.commit()
    print("Records inserted successfully")

    # Read (Select)
    cur.execute("SELECT name, address FROM interns")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Update a record
    cur.execute("UPDATE interns SET address = %s WHERE name = %s", ('Chunatal', 'Archana SApkota'))
    conn.commit()
    print("Record updated successfully")

    # Delete a record
    cur.execute("DELETE FROM interns WHERE name = %s", ('Ashmita Basnet',))
    conn.commit()
    print("Record deleted successfully")

except Exception as error:
    print(f"Error: {error}")
finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
    print("Database connection closed")
