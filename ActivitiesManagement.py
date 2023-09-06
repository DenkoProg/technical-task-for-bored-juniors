import sqlite3


class Activity:
    def __init__(self, activity, type, participants, price, link, key, accessibility):
        self.activity = activity
        self.type = type
        self.participants = participants
        self.price = price
        self.link = link
        self.key = key
        self.accessibility = accessibility

    def __str__(self):
        return f'{self.activity} ({self.type})'


class ActivityDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('activities.db')
        self.cursor = self.connection.cursor()

    def create_activities_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity TEXT,
                type TEXT,
                participants INTEGER,
                price REAL,
                link TEXT,
                key TEXT,
                accessibility REAL
            )
        """)

        self.connection.commit()

    def save_activity(self, activity):
        self.cursor.execute("""
            INSERT INTO activities (activity, type, participants, price, link, key, accessibility)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            activity.activity,
            activity.type,
            activity.participants,
            activity.price,
            activity.link,
            activity.key,
            activity.accessibility,
        ))
        self.connection.commit()

    def get_latest_activities(self, number_of_activities):
        self.cursor.execute("""
            SELECT *
            FROM activities
            ORDER BY id DESC
            LIMIT ?
        """, (number_of_activities,))
        return [Activity(*row[1:]) for row in self.cursor.fetchall()]
