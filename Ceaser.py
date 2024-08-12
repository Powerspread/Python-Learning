import sys
shift = 1

def main():
    if sys.argv[1].lower() == "e":
        encrypt()
    elif sys.argv[1].lower() == "d":
        decrypt()

def encrypt():
    plain_text_message = input("Message to be Encrypted: ")
    encrypted_message = ""
    for char in plain_text_message:
        if char.isalpha() == True:
            if char.islower() == True:
                alpha = ord("a")
            else:
                alpha = ord("A")
            encrypted_message += chr((ord(char) - alpha + shift) % 26 + alpha)
        else:
            encrypted_message += char
    print(encrypted_message)         

def decrypt():
    encrypted_message = input("Message to be Decrpyted: ")
    plain_text_message = ""
    for char in encrypted_message:
        if char.isalpha() == True:
            if char.islower() == True:
                alpha = ord("a")
            else:
                alpha = ord("A")
            plain_text_message += chr((ord(char) - alpha - shift) % 26 + alpha)
        else:
            plain_text_message += char 
    print(plain_text_message)

if __name__ == "__main__":
    main()