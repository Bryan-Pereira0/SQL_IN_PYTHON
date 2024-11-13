import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        database='Fitness_Center',
        user='root',
        password='password_here'
        )

#task1 add member
def add_member(id, name, age):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)", (id, name, age))
        conn.commit()
        print("Member added successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

#task2 add workout
def add_workout_session(session_id, member_id, session_date, session_time, activity):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s, %s)", (session_id, member_id, session_date, session_time, activity))
        conn.commit()
        print("Workout session added successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

#task3 update age
def update_member_age(member_id, new_age):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Members SET age = %s WHERE id = %s", (new_age, member_id))
        if cursor.rowcount > 0:
            conn.commit()
            print("Member age updated successfully.")
        else:
            print("Error: Member not found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

#task4 delete workout
def delete_workout_session(session_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM WorkoutSessions WHERE session_id = %s", (session_id, ))
        if cursor.rowcount > 0:
            conn.commit()
            print("Workout session deleted successfully.")
        else:
            print("Error: Session ID not found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
