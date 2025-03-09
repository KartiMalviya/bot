import sqlite3

def get_news_response(query):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, link FROM news WHERE title LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()

    if results:
        response = "Here are some news articles:\n"
        for title, link in results:
            response += f"- {title}: {link}\n"
    else:
        response = "No news found for your query."
    
    return response
