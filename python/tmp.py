
if __name__ == '__main__':
    x = 10 / 3
    print('{:.2f}'.format(x))
    print(f'{x:.2f}')


"""
import pymongo

client = pymongo.MongoClient(host="localhost", port=27017)

# table_name = название таблицы
# collection_name = название коллекции внутри таблицы
result = client["table_name"]["collection_name"].insert_one({
    "test_name": "test_name"
})
row = client["table_name"]["collection_name"].find_one({"_id": result.inserted_id})
print(row)

"""