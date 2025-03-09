import sqlite3

def setup_database():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY,
            title TEXT,
            link TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_news(news_list):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    for news in news_list:
        cursor.execute("INSERT INTO news (title, link, date) VALUES (?, ?, ?)", 
                       (news['title'], news['link'], news['date']))
    conn.commit()
    conn.close()

# Initialize the database
setup_database()
