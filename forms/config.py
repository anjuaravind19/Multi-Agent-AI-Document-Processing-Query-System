import os

# MongoDB Configuration
#MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_URI = "mongodb://adminUser:yourStrongPassword@localhost:27017/"
#MONGO_URI = "mongodb://<adminUser>:<yourStrongPassword>@localhost:27017/<application_db>?authSource=admin"

DB_NAME = "application_db"
COLLECTION_NAME = "applications"
#MONGO_URI = "mongodb://<username>:<password>@localhost:27017/application_db?authSource=admin"


# Upload Directory
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
