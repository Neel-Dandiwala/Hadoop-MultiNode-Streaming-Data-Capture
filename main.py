import faker
from datetime import datetime
import psycopg2
from pymongo import MongoClient
import random
import signal

fake = faker.Faker()

def generate_transaction():
    user = fake.simple_profile()
    return {
        "transactionId": fake.uuid4(),
        "userId": user['username'],
        "timestamp": datetime.utcnow(),
        "amount": round(random.uniform(10, 1000), 2),
        "currency": random.choice(['USD', 'CAD']),
        "city": fake.city(),
        "country": fake.country(),
        "merchantName": fake.company(),
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transfer']),
        "ipAddress": fake.ipv4(),
        "voucherCode": random.choice(['', 'DISCOUNT10', '']),
        "affiliateId": fake.uuid4(),
    }

def create_postgres_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id VARCHAR(255) PRIMARY KEY,
            user_id VARCHAR(255),
            timestamp TIMESTAMP,
            amount DECIMAL,
            currency VARCHAR(255),
            city VARCHAR(255),
            country VARCHAR(255),
            merchant_name VARCHAR(255),
            payment_method VARCHAR(255),
            ip_address VARCHAR(255),
            voucher_code VARCHAR(255),
            affiliateId VARCHAR(255)
        )
        """
    )
    cursor.close()
    conn.commit()

def insert_postgres_transaction(conn, transaction):
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO transactions(transaction_id, user_id, timestamp, amount, currency, city, country, merchant_name, payment_method, ip_address, affiliateId, voucher_code)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (transaction["transactionId"], transaction["userId"], transaction["timestamp"],
              transaction["amount"], transaction["currency"], transaction["city"], transaction["country"],
              transaction["merchantName"], transaction["paymentMethod"], transaction["ipAddress"],
              transaction["affiliateId"], transaction["voucherCode"])
    )
    cur.close()
    conn.commit()

def create_mongodb_collection(db):
    transactions_collection = db['transactions']
    transactions_collection.create_index("transactionId", unique=True)
    return transactions_collection

def insert_mongodb_transaction(collection, transaction):
    collection.insert_one(transaction)

if __name__ == "__main__":
    # PostgreSQL connection
    postgres_conn = psycopg2.connect(
        host='localhost',
        database='bigdata_db',
        user='postgres',
        password='postgres',
        port=5432
    )
    create_postgres_table(postgres_conn)

    # MongoDB connection
    mongo_client = MongoClient('mongodb+srv://mongodb:mongodb@bigdata.j77wrns.mongodb.net/')
    mongo_db = mongo_client['bigdatadb']
    mongo_transactions_collection = create_mongodb_collection(mongo_db)
    try:
        while True:
            # Generate and insert a sample transaction for PostgreSQL
            transaction = generate_transaction()
            print("PostgreSQL Transaction:")
            print(transaction)
            insert_postgres_transaction(postgres_conn, transaction)

            # Generate and insert a sample transaction for MongoDB
            transaction = generate_transaction()
            print("\nMongoDB Transaction:")
            print(transaction)
            insert_mongodb_transaction(mongo_transactions_collection, transaction)
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting...")

    finally:
        # Close connections
        postgres_conn.close()
        mongo_client.close()
