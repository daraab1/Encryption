from cryptography.fernet import Fernet
from Secret import KEY

def main():
    print("Enter a string to encrypt: ", end="")
    user_input = input()

    if not valid_input(user_input):
        print("Invalid input")
        return

    enc_text = encrypt(user_input)

    print(f"Encrypted text: {enc_text}")

    write_file(enc_text)

    print("Encrypted text written to file")

    file_text = read_file()

    decrypted_text = decrypt(file_text)

    print(f"Decrypted text: {decrypted_text}")



def valid_input(user_input):
    if not user_input:
        return False
    
    if len(user_input) < 1 or len(user_input) > 20:
        return False
    
    return True

def encrypt(user_input):
    fernet = Fernet(KEY)
    enc_text = fernet.encrypt(user_input.encode())

    return enc_text.decode()

def decrypt(enc_text):
    fernet = Fernet(KEY)
    dec_text = fernet.decrypt(enc_text.encode())

    return dec_text.decode()

def write_file(text):
    with open("encrypted.txt", "w") as file:
        file.write(text)

def read_file():
    with open("encrypted.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    main()