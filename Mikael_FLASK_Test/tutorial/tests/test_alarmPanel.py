import pytest
import sqlite3

def test_insert_data():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(':memory:')  # Use in-memory database for testing
    cursor = conn.cursor()

    # Create a dummy table for testing
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS testTable (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Alarms TEXT NOT NULL,
            Date TEXT NOT NULL,
            Priority TEXT NOT NULL,
            Location TEXT NOT NULL
        );
    """)

    # Define the function to insert data into the specified table
    def insert_data(table_name, data):
        cursor.execute(f"INSERT INTO {table_name} (Alarms, Date, Priority, Location) VALUES (?, ?, ?, ?)", data)

    # Insert dummy data into the test table
    data = ("Test Alarm", "2024-04-08", "High", "Test Location")
    insert_data('testTable', data)

    # Fetch the data from the test table
    cursor.execute("SELECT * FROM testTable")
    rows = cursor.fetchall()

    # Check that the data was inserted correctly
    assert len(rows) == 1
    assert rows[0] == (1, "Test Alarm", "2024-04-08", "High", "Test Location")

    # Close the database connection
    conn.close()
