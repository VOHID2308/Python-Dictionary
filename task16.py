data = {"name": "Ali", "age": 25, "city": "Tashkent"}
key = input("Kalit nomini kiriting: ")

if key in data:
    del data[key]
    print(f"{key} ochirildi")
else:
    print("Bunday kalit yoq")

print(data)
