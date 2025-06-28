import psycopg2
from dotenv import load_dotenv
import os

def create_table():
    """Create blood_test_results table if it doesn't exist"""
    load_dotenv()
    conn = None
    try:
        conn = psycopg2.connect(
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port"),
            dbname=os.getenv("dbname")
        )
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS blood_test_results (
                id SERIAL PRIMARY KEY,
                query TEXT NOT NULL,
                analysis TEXT NOT NULL,
                file_name TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        print("Table created successfully")
        
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_table()
