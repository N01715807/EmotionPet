from datetime import datetime

class pet:
    def __init__(self, name = "Starting_name"):
        self.name = "Starting_name"
        self.level = 1
        self.mood = "neutral"
        self.exp = 0
        self.created_at = datetime.now().isoformat()

    def get_status(self):
        return{
            "name":self.name
            
        }