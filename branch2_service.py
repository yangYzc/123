# Branch 2 - Service Configuration
# Service configuration for branch 2

SERVICE_CONFIG = {
    "service_name": "Branch2Service",
    "port": 8080,
    "environment": "development",
    "logging": {
        "level": "DEBUG",
        "format": "[BRANCH2] %(asctime)s - %(name)s - %(levelname)s - %(message)s"
    },
    "cache": {
        "type": "redis",
        "host": "redis-branch2",
        "port": 6379,
        "db": 2
    },
    "external_apis": [
        "https://api.branch2.example.com/v1",
        "https://auth.branch2.example.com"
    ]
}