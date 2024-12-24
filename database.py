import mysql.connector

    # Set up the database connection
    cnx = mysql.connector.connect(
        user="username",
        password="password",
        host="host",
        database="database"
    )

    # Create a cursor object
    cursor = cnx.cursor()

    # Create a table for lead information
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INT AUTO_INCREMENT,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255),
            national_id VARCHAR(255),
            country VARCHAR(255),
            phone_number VARCHAR(255),
            PRIMARY KEY (id)
        );
    """)

    # Create a table for superadmin information
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS superadmins (
            id INT AUTO_INCREMENT,
            username VARCHAR(255),
            password VARCHAR(255),
            PRIMARY KEY (id)
        );
    """)

    # Insert lead information into the table
    def insert_lead_info(lead_info):
        cursor.execute("""
            INSERT INTO leads (first_name, last_name, email, national_id, country, phone_number)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (lead_info["first_name"], lead_info["last_name"], lead_info["email"], lead_info["national_id"], lead_info["country"], lead_info["phone_number"]))
        cnx.commit()

    # Insert superadmin information into the table
    def insert_superadmin_info(superadmin_info):
        cursor.execute("""
            INSERT INTO superadmins (username, password)
            VALUES (%s, %s);
        """, (superadmin_info["username"], superadmin_info["password"]))
        cnx.commit()

    # Close the cursor and connection
    cursor.close()
    cnx.close()
