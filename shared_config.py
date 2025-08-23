# Shared Configuration File - Branch 1 Version
# This file will have different content in each branch to cause merge conflicts

APP_SETTINGS = {
    "name": "MergeTestApp",
    "version": "1.0.0-branch1", 
    "author": "Branch 1 Developer",
    "description": "This is the branch 1 version of the application",
    "features": [
        "user_authentication",
        "data_processing", 
        "branch1_special_feature"
    ],
    "database_config": {
        "type": "postgresql",
        "connection_string": "postgresql://branch1:password@localhost/branch1_db"
    },
    "api_endpoints": [
        "/api/v1/users",
        "/api/v1/auth", 
        "/api/v1/branch1-data"
    ]
}

# Branch 1 specific function
def initialize_branch1_features():
    print("Initializing Branch 1 specific features...")
    return "Branch 1 initialization complete"