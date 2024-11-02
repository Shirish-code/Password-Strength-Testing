import hashlib

# List of passwords
passwords = [
    "password123",
    "qwerty",
    "123456",
    "admin",
    "password",
    "Password@123",
    "qwerty123!",
    "letmein2023",
    "1234567890",
    "Password2023",
    "SuperSecurePass2023!",
    "S3cur3_P@ssword!",
    "MyP@ss2023#",
    "Secure!Pass2023",
    "Welcome123#",
    "G7h$!3qPz*2K@9m",
    "XyB4!v1sR$z9L%k&",
    "P@ssw0rd#2023!Secure",
    "1aZ5@pQ!d$X8jY4#",
    "Q!5uP@7kzZ9L4c&m",
]

# Open a file to save hashes
with open("hashes.txt", "w") as hash_file:
    for password in passwords:
        # Generate MD5 hash value
        hash_object = hashlib.md5(password.encode())
        hash_hex = hash_object.hexdigest()

        # Write to file in the format: hash # password
        hash_file.write(f"{hash_hex}  # {password}\n")
        print(f"{password} -> {hash_hex}")

print("Hashes saved to hashes.txt")
