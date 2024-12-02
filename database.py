import sqlite3 as sq

class DBManeger:
    def __init__(self, db_file):
        self.db_file = db_file
    
    def search_film(self, film_id):
        with sq.connect(self.db_file) as db:
            cursor = db.cursor()
            cursor.execute('SELECT title, kinopoisk_url FROM movies WHERE id = ?', (film_id,))
            result = cursor.fetchone()
            if result:
                title, link = result
                return title, link
            else:
                return None, None