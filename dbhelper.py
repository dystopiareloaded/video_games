import sqlite3

class DB:
    def __init__(self, db_path="video_game_sales.db"):
        try:
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            print("✅ SQLite DB connected")
        except Exception as e:
            print("❌ Connection failed:", e)

    def fetch_genres(self):
        self.cursor.execute("SELECT DISTINCT genre FROM video_game_sales ORDER BY genre")
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_publishers(self):
        self.cursor.execute("SELECT DISTINCT publisher FROM video_game_sales ORDER BY publisher")
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_platforms(self):
        self.cursor.execute("SELECT DISTINCT platform FROM video_game_sales ORDER BY platform")
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_years(self):
        self.cursor.execute("SELECT DISTINCT year FROM video_game_sales WHERE year IS NOT NULL ORDER BY year")
        return [row[0] for row in self.cursor.fetchall()]

    def genre_sales_by_year(self, year):
        self.cursor.execute("""
            SELECT genre, SUM(global_sales)
            FROM video_game_sales
            WHERE year = ?
            GROUP BY genre
            ORDER BY SUM(global_sales) DESC
        """, (year,))
        data = self.cursor.fetchall()
        return [row[0] for row in data], [row[1] for row in data]

    def publisher_sales_by_year(self, year):
        self.cursor.execute("""
            SELECT publisher, SUM(global_sales)
            FROM video_game_sales
            WHERE year = ?
            GROUP BY publisher
            ORDER BY SUM(global_sales) DESC
            LIMIT 20
        """, (year,))
        data = self.cursor.fetchall()
        return [row[0] for row in data], [row[1] for row in data]

    def platform_sales_by_year(self, year):
        self.cursor.execute("""
            SELECT platform, SUM(global_sales)
            FROM video_game_sales
            WHERE year = ?
            GROUP BY platform
            ORDER BY SUM(global_sales) DESC
        """, (year,))
        data = self.cursor.fetchall()
        return [row[0] for row in data], [row[1] for row in data]

    def sales_over_time(self):
        self.cursor.execute("""
            SELECT year, SUM(global_sales)
            FROM video_game_sales
            WHERE year IS NOT NULL
            GROUP BY year
            ORDER BY year
        """)
        data = self.cursor.fetchall()
        return [row[0] for row in data], [row[1] for row in data]
