import mysql.connector
from mysql.connector import Error

def create_connection():
    """
    Create a connection to MySQL database
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',          # Your MySQL host
            user='root',               # Your MySQL username
            password='your_password',  # Your MySQL password
            database='resume_builder'      # Your database name
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server version {db_info}")
        
        return connection
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
def create_table(connection):
    """
    Create a simple table in the database
    """
    try:
        cursor = connection.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(70) NOT NULL,
            email VARCHAR(70) NOT NULL,
            age INT,
            address VARCHAR(70) NOT NULL,
            phone INT,
            job title VARCHAR(70) NOT NULL,
            professional summary VARCHAR(70) NOT NULL,
            experience VARCHAR(70) NOT NULL,
            education VARCHAR(70) NOT NULL,
            Skills  VARCHAR(70) NOT NULL

        )
        """
        
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'users' created successfully")
        cursor.close()
    
    except Error as e:
        print(f"Error creating table: {e}")

def get_user_input():
    """
    Get user input from terminal
    """
    print("=" * 40)
    print("Enter User Information")
    print("=" * 40)
    
    name = input("Enter name:Bob Marley ").strip()
    
    # Validate age input
    while True:
        try:
            age = int(input("Enter age:30 "))
            break
        except ValueError:
            print("Please enter a valid number for age")
    
    address = input("Enter address:Manila City ").strip()
    
    return name, age, address


def insert_data(name, age, address, phone, email, job title, professional summary, experience, education, skills):
    """
    Insert data into the users table
    """
    try:
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO users (name, age, address, phone, email, job title, professional summary, experience, education, skills ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,  %s, %s)"
        user_data = (name, age, address, phone, email, job title, professional summary, experience, education, skills)
        
        cursor.execute(insert_query, user_data)
        connection.commit()
        print(f"Record inserted successfully for {name}")
        cursor.close()
    
    except Error as e:
        print(f"Error inserting data: {e}")
def retrieve_data(connection):
    # ... (execute query is the same) ...
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    
    if records:
        print("\n" + "=" * 60)
        print("All Users in Database")
        print("=" * 60)
        for record in records:
            print(f"ID: {record[0]}")
            print(f" Bob Marly Name: {record[1]}")
            print(f" 30 Age: {record[2]}")
            print(f" Manila City Address: {record[3]}")
            print("-" * 60)
    else:
        print("\nNo users found in database\n")
    
    cursor.close()
    # ... (try/except is the same) ...


def close_connection(connection):
    """
    Close the database connection
    """
    if connection.is_connected():
        connection.close()
        print("\nMySQL connection is closed")

def main_menu(connection):
    """
    Display menu and handle user choices
    """
    while True:
        print("\n" + "=" * 40)
        print("User Management System")
        # ... (more print statements for menu) ...
        print("3. Exit")
        print("=" * 40)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            name, age, address, phone, email, job title, professional summary, experience, education, skills = get_user_input()
            insert_user_data(name, age, address, phone, email, job title, professional summary, experience, education, skills)
        
        elif choice == "2":
            retrieve_data(connection)
        
        elif choice == "3":
            print("\nThank you for using the system!")
            break
        
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3")

if __name__ == "__main__":
    # Step 1: Create connection
    conn = create_connection()
    
    if conn:
        # Step 2: Create table
        create_table(conn)
        
        # Step 3: Show menu and handle user interactions
        main_menu(conn)
        
        # Step 4: Close connection
        close_connection(conn)

