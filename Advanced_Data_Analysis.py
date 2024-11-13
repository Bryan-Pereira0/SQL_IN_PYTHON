import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        database='Fitness_Center',
        user='root',
        password='password_here'
        )
def get_members_in_age_range(start_age, end_age):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s AND %s"
        cursor.execute(query, (start_age, end_age))
        results = cursor.fetchall()
        if results:
            for member in results:
                print(member)
        else:
            print("Nobody found in this age range.")
        return results
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


        
