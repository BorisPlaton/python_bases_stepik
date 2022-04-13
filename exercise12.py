import simplecrypt


with open('passwords.txt') as p:
    passwords = p.readlines()

with open('encrypted.bin', mode='rb') as f:
    file = f.read()
    for password in passwords:
        try:
            print(simplecrypt.decrypt(password.strip(), file))
            break
        except simplecrypt.DecryptionException:
            continue

