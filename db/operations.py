class OpsForMongo:
    def __init__(self, db, collection) -> None:
        self.__db = db
        self.__collection = self.__db[collection]

    async def get_random_one(self):
        return await self.__collection.aggregate([{ '$sample': { 'size': 1 } }]).to_list(length=1)

    async def get_random(self, count: int):
        return await self.__collection.aggregate([{ '$sample': { 'size': count } }]).to_list(length=count)