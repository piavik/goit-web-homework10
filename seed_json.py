import psycopg2
import json
from psycopg2.extras import execute_values
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

post_user = config.get('DEFAULT', 'user')
post_pass = config.get('DEFAULT', 'pass')
post_host = config.get('DEFAULT', 'host')
post_port = config.get('DEFAULT', 'port')
post_db = config.get('DEFAULT', 'db_name')

print(f'database={post_db}, user={post_user}, password={post_pass}, host={post_host}, port={post_port}')

filename_quotes = "hw10/seed/quotes.json"
filename_authors = "hw10/seed/authors.json"

def read_json(file):
    with open(file, "r", encoding='utf-8') as f:
        return json.load(f)

authors = read_json(filename_authors)
quotes = read_json(filename_quotes)


with psycopg2.connect(database=post_db, user=post_user, password=post_pass, host=post_host, port=post_port) as conn:
    cur = conn.cursor()

    for author in authors:
        insert_query = """INSERT INTO authors_author VALUES (?, ?, ?, ?)"""
        cur.execute(insert_query, tuple(author.values()))


    for quote in quotes:
        author_name = Author.objects(fullname=quote['author']).first()
        quote['author'] = author_name
        # session.add(Quotes(**quote))

        insert_query = """INSERT INTO quotes_quote VALUES (?, ?, ?, ?)"""
        # cur.execute(insert_query, tuple({(**quotes)}.values))
        cur.execute(insert_query, tuple(quote.values()))

    conn.commit()
