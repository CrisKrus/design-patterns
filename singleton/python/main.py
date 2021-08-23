class Database:
    __instance = None

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance is None:
            Database.__instance = self
        else:
            print("the singleton was initialized yet")


database1 = Database()
database2 = Database()
database3 = Database()

print(database1.get_instance())
print(database2.get_instance())
print(database3.get_instance())
