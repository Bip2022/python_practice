# accessing single dicionary values
# person = {
#     "name": ["Bipin", "Aryan", "Sanjay"],
#     "age": 20,
#     "city": "Kathmandu"
# }

# print(person["name"])
# print(person["age"]) 
# print(person["city"])


# person = {
#     "name": ["Bipin"],
#     "age": 20,
# }
# person["city"] = "Kathmandu" 
# person["name"].append("Hari")# Adding a new key-value pair
# person["name"].pop(0)
# print(person)
# check key in dictionary
# if "name" in person:
#     print("name exists")

# accessing multiple dictionary values
# person = {
#     "name": ["Bipin", "Aryan", "Sanjay"],
#     "age": [20, 22, 25],
#     "city": ["Kathmandu", "Pokhara", "Biratnagar"]
# }

# print(person["name"][0], person["age"][0], person["city"][0])  # ✅ Correct
# print(person["age"][0])      # Output: 20
# print(person["city"][0])     # Output: Kathmandu
# print(person["name"][1], person["age"][1], person["city"][1])  # ✅ Correct
# print(person["name"][2], person["age"][2], person["city"][2])  # ✅ Correct


# fruits = ["apple", "banana", "mango"]
# # print(fruits[0])       # Output: apple
# # print(fruits[1:])      # Output: ['banana', 'mango']
# # print(fruits[1:2])  
# # fruits.append("guva" )
# # fruits.insert (0,"grapes")
# # print(fruits)   # Output: ['banana']

# # fruits.pop(1)
# print(fruits[0],fruits[1])  # Output: ['apple', 'banana', 'mango', 'guva', 'grapes']
# print(fruits[0:2])
# print(len(fruits))  # Output: 5

# tupple
fruits = ("apple", "banana", "mango")
print(fruits[0])  # Output: apple
