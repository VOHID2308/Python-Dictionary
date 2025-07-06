config = {}

for i in range(3):
    key = input(f"{i+1}-Kalit nomi: ")
    value = input(f"{key} qiymati: ")
    config[key] = value

print(config)
