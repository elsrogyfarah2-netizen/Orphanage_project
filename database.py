
import sqlite3

def create_database():
    conn = sqlite3.connect("orphanage.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Children (
        Child_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Child_Name TEXT NOT NULL,
        Birth_Date TEXT,
        Gender TEXT,
        Health_Status TEXT,
        Supervisor_ID INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Supervisors (
        Supervisor_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Phone TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Education (
        Education_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Grade TEXT,
        Academic_Year TEXT,
        Result TEXT,
        Child_ID INTEGER,
        FOREIGN KEY (Child_ID) REFERENCES Children(Child_ID)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Medical_Records (
        Medical_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Diagnosis TEXT,
        Treatment TEXT,
        Record_Date TEXT,
        Child_ID INTEGER,
        FOREIGN KEY (Child_ID) REFERENCES Children(Child_ID)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Donors (
        Donor_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Phone TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Donations (
        Donation_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Amount REAL,
        Donation_Date TEXT,
        Donor_ID INTEGER,
        FOREIGN KEY (Donor_ID) REFERENCES Donors(Donor_ID)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Visitors (
        Visitor_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Phone TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Visits (
        Visit_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Visit_Date TEXT,
        Notes TEXT,
        Visitor_ID INTEGER,
        Child_ID INTEGER,
        FOREIGN KEY (Visitor_ID) REFERENCES Visitors(Visitor_ID),
        FOREIGN KEY (Child_ID) REFERENCES Children(Child_ID)
    )
    """)

    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == "__main__":
    create_database()
