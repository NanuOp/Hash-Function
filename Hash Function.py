# import hashlib

# def custom_hash(data):
#     return hashlib.sha256(data).hexdigest()

# # Example usage

# data_to_hash = input("Enter data to hash: ")
# data_to_hash= data_to_hash.encode("utf-8")
# hashed_data = custom_hash(data_to_hash)
# print("Hashed Data:", hashed_data)










# import hashlib

# def custom_hash(data):
#     return hashlib.sha256(data).hexdigest()

# data_to_hash = input("Enter What to Hash")
# data_to_hash = data_to_hash.encode("utf-8")
# hashed_data = custom_hash(data_to_hash)
# print("Hased Data:", hashed_data)


































import hashlib

def custom_hash(data):
    return hashlib.sha256(data).hexdigest()

datatohash = input("What do you want to hash: ")
datatohash = datatohash.encode("utf-8")
customhash = custom_hash(datatohash)

print("your hash: ", customhash)