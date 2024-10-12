import psycopg2
import time
import random

DB_URL = "dbname='postgres' user='postgres' host='localhost' password='postgres'"

def main():
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    try:
        while True:
            wait_time = random.randint(1, 10)  # Espera aleatoria entre 1 y 10 segundos
            time.sleep(wait_time)
            cursor.execute("SELECT id, name FROM dummy")
            results = cursor.fetchall()
            for row in results:
                print(f'Resultado: ID: {row[0]}, name: {row[1]}')  # Muestra tanto el id como el nombre
    except Exception as e:
        print(f'Error: {e}')
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()