import hashlib

def hash_password(pw):
    data = pw.encode("utf-8")
    return hashlib.sha256(data).hexdigest()

print(hash_password("correctHorse"))
print(hash_password("correctHorse "))
