from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data["_id"])
        self.username = user_data["username"]
        self.email = user_data["email"]
        self.avatar_url = user_data.get("avatar_url")  # New line

    @staticmethod
    def get_user_by_email(db, email):
        return db.users.find_one({"email": email})

    @staticmethod
    def get_user_by_id(db, user_id):
        from bson.objectid import ObjectId
        return db.users.find_one({"_id": ObjectId(user_id)})


class Entry:
    @staticmethod
    def create_entry(db, user_id, title, content):
        entry = {
            "user_id": user_id,
            "title": title,
            "content": content,
            "timestamp": Entry.current_time()
        }
        db.entries.insert_one(entry)

    @staticmethod
    def get_entries_by_user(db, user_id):
        return db.entries.find({"user_id": user_id}).sort("timestamp", -1)

    @staticmethod
    def current_time():
        from datetime import datetime
        return datetime.utcnow()
