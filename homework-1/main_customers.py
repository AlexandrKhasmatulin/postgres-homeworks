"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2


def read_csv():
    data = []
    with open(os.path.join('north_data', 'customers_data.csv'), 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=',')
        for line in file_reader:
            data.append(line)
    #data = data.replace("'", "''")
    print(data)
    return data


def main():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='Alex030652')
    data = read_csv()
    with conn:
        cursor = conn.cursor()
        for item in data[1:]:
            cursor.execute(f"INSERT INTO customers(customer_id, company_name, contact_name) VALUES ('{item[0]}', '{item[1]}', '{item[2]}')")


if __name__ == '__main__':
    main()
