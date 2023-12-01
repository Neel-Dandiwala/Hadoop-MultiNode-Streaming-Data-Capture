import psycopg2
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

def create_postgres_connection():
    return psycopg2.connect(
        host='localhost',
        database='bigdata_db',
        user='postgres',
        password='postgres',
        port=5432
    )

def create_mongo_connection():
    return MongoClient('mongodb+srv://mongodb:mongodb@bigdata.j77wrns.mongodb.net/')


def fetch_postgres_data():
    conn = create_postgres_connection()
    query = "SELECT * FROM transactions;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def fetch_mongo_data():
    client = create_mongo_connection()
    db = client['bigdatadb']
    collection = db['transactions']
    cursor = collection.find()
    df = pd.DataFrame(list(cursor))
    client.close()
    return df


postgres_df = fetch_postgres_data()
mongo_df = fetch_mongo_data()

print(postgres_df.head())


print(mongo_df.head())


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
postgres_df['amount'].plot(kind='bar', title='Transaction Amounts')

plt.subplot(1, 2, 2)
mongo_df['paymentMethod'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Payment Methods')


plt.tight_layout()
plt.show()
