"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2


def read_csv():
    data = []
    with open(os.path.join('north_data', 'employees_data.csv'), 'r', encoding='utf-8') as file:
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
        for row in data[1:]:
            cursor.execute(f'INSERT INTO employees(first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s)',
                           (row[0], row[1], row[2], row[3], row[4]))


if __name__ == '__main__':
    main()