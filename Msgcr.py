def get_shift(key):
    return sum(ord(c) for c in key) % 25 + 1


def encrypt(text, shift):
    result = ""

    for char in text:
        if 'a' <= char <= 'z':
            base = ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)

        elif 'A' <= char <= 'Z':
            base = ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)

        elif '\u0600' <= char <= '\u06FF':
            new_char = chr(ord(char) + shift)

        else:
            new_char = char

        result += str(ord(new_char)) + " "

    return result.strip()


def decrypt(text, shift):
    chars = text.split()
    result = ""

    for num in chars:
        char = chr(int(num))

        if 'a' <= char <= 'z':
            base = ord('a')
            original = chr((ord(char) - base - shift) % 26 + base)

        elif 'A' <= char <= 'Z':
            base = ord('A')
            original = chr((ord(char) - base - shift) % 26 + base)

        elif '\u0600' <= char <= '\u06FF':
            original = chr(ord(char) - shift)

        else:
            original = char

        result += original

    return result


while(True):
    # ===== اختيار المستخدم =====
    print("1 - Encrypt")
    print("2 - Decrypt")

    choice = input("Choose option: ")
    key = "Samoray" # لتحكم في مقدار الإزاحة 
    shift = get_shift(key)



# ===== تشفير =====
    if choice == "1":
        with open("message.txt", "r", encoding="utf-8") as f:
            message = f.read()

        encrypted = encrypt(message, shift)

        with open("result.txt", "w", encoding="utf-8") as f:
            f.write(encrypted)

        print("Encrypted ✔ saved to encrypted.txt")


# ===== فك التشفير =====
    elif choice == "2":
        with open("message.txt", "r", encoding="utf-8") as f:
            encrypted_text = f.read()

        decrypted = decrypt(encrypted_text, shift)

        with open("result.txt", "w", encoding="utf-8") as f:
            f.write(decrypted)

        print("Decrypted ✔ saved to decrypted.txt")


    else:
        print("Invalid choice ❌")