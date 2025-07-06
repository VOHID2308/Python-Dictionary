permissions = {"read": True, "write": False, "delete": True}
per = []

for permission in permissions:
    if permissions[permission] == True:
        per.append(permission)
        

print(per)