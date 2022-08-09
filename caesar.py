key = 0
def shift():
    global key
    key = input("key: ")
    try:
        key = int(key)
        if key > 26:
            key = key % 26
    except:
        print("Key must be an integer")
        shift()

def encrypt(msg):
    global key
    ct = []
    for i in msg:
        if i.isidentifier():
            if i.isupper():
                ct.append((ord(i) - 65 + key) % 26 + 65)
            elif i.islower():
                ct.append((ord(i) - 97 + key) % 26 + 97)
        else:
            ct.append(ord(i))
    for i in ct:
        print(chr(i), end="")

usrin = input("plaintext: ")
shift()
encrypt(usrin)