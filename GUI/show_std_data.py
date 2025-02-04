from pymongo import MongoClient
try:
    MONGO_URI = ""# Your MongoDB URI
    client = MongoClient(MONGO_URI)

    client.admin.command("ping")
    print("Connected successfully")
    # other application code
    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
