# Branch 2 - Data Models
# Data models specific to branch 2

class Branch2User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.branch_origin = "branch-2"
    
    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "branch_origin": self.branch_origin
        }

class Branch2Data:
    def __init__(self):
        self.data_source = "branch2_database"
        self.version = "2.0.0"
    
    def process_data(self, raw_data):
        processed = f"[BRANCH2] Processed: {raw_data}"
        return processed
    
    def validate_data(self, data):
        return len(data) > 0 and "branch2" in str(data).lower()