import configparser
import psycopg2 

def sql_command(sql: str, data: tuple):
    """ Helper function to execute a SQL command with Postgres"""
    config = configparser.ConfigParser()
    config.read("database.ini")
    dbini = config["POSTGRES"]

    conn = psycopg2.connect(dbname=dbini["dbname"],
                            user=dbini["user"],
                            password=dbini["password"])
    cursor = conn.cursor()

    try:
        cursor.execute(sql, data)
        conn.commit()
        print("Success!!")
    except:
        print("Something wrong happened. Look at psql logs.")

    return

