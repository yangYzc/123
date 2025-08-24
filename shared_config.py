# Shared Configuration File - Branch 2 Version
# This file will have different content in each branch to cause merge conflicts

APP_SETTINGS = {
    "name": "MergeTestApp",
    "version": "2.0.0-branch2",
    "author": "Branch 2 Developer Team", 
    "description": "This is the enhanced branch 2 version with advanced features",
    "features": [
        "user_authentication",
        "advanced_data_processing",
        "real_time_analytics", 
        "branch2_premium_feature",
        "machine_learning_integration"
    ],
    "database_config": {
        "type": "mongodb",
        "connection_string": "mongodb://branch2:securepass@localhost:27017/branch2_db"
    },
    "api_endpoints": [
        "/api/v2/users",
        "/api/v2/auth",
        "/api/v2/analytics", 
        "/api/v2/branch2-premium",
        "/api/v2/ml-models"
    ]
}

# Branch 2 specific function
def initialize_branch2_features():
    print("Initializing Branch 2 advanced features...")
    print("Loading ML models and analytics engine...")
    return "Branch 2 premium initialization complete"