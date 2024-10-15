from pymongo import MongoClient

# Подключение к серверу MongoDB
client = MongoClient('localhost', 27017)

# Выбираем базу данных
db = client.my_database
print("Қосылу сәтті орындалды!")

# Создаем коллекцию
collection = db.my_collection
print("Коллекция құрылды.")

# Вставка одного документа
new_document = {
    "name": "Ali",
    "age": 25,
    "city": "Almaty"
}
collection.insert_one(new_document)
print("Құжат енгізілді.")

# Вставка нескольких документов
documents = [
    {"name": "Aigerim", "age": 28, "city": "Nur-Sultan"},
    {"name": "Dina", "age": 22, "city": "Shymkent"}
]
collection.insert_many(documents)
print("Көптеген құжаттар енгізілді.")

# Чтение всех документов
for document in collection.find():
    print(document)

# Чтение по критериям
person = collection.find_one({"name": "Ali"})
print("табылған құжат:", person)

# Обновление одного документа
query = {"name": "Ali"}
new_values = {"$set": {"age": 26}}
collection.update_one(query, new_values)
print("Құжат жаңартылды.")

# Обновление нескольких документов
query = {"city": "Almaty"}
new_values = {"$set": {"city": "Aktau"}}
collection.update_many(query, new_values)
print("Көптеген құжаттар жаңартылды.")

# Удаление одного документа
query = {"name": "Ali"}
collection.delete_one(query)
print("Құжат жойылды.")

# Удаление нескольких документов
query = {"city": "Aktau"}
collection.delete_many(query)
print("Көптеген құжаттар жойылды.")
