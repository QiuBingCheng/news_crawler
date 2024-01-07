import sqlite3
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

conn = sqlite3.connect(config["result"]["db"])


def total_count():
    c = conn.cursor()
    result = c.execute("select count(*) from news_record")
    return result.fetchone()[0]


def select_records(limit=10, offset=2):
    c = conn.cursor()
    data = c.execute(
        "SELECT crawl_date, keyword, num_records  from news_record  LIMIT ? OFFSET ?", ((limit, offset)))
    return data


def select_filename(crawl_date):
    c = conn.cursor()
    result = c.execute(
        " SELECT filename FROM news_record WHERE crawl_date = ?", (crawl_date,))
    return result.fetchone()[0]
