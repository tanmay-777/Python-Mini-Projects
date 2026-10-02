#Ask user if he wants to encrypt or decrypt
#Ask User to write the size of the KEY
#Ask user to write the sentence
#give user translated sentece back
try:
    import pyperclip
except:
    pass


SYMBOLS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
polling = True
print("Welcome to Caser Cipher Encryption/Decryption")
while polling:

    while True:
        print("Do you wanna (E)ncrypt or (D)crypt using Caser Cipher?")
        reponse = input("> ")
        if reponse.upper().startswith("E"):
            mode = "Encrypt"
            break
        elif reponse.upper().startswith("D"):
            mode = "Decrypt"
            break


    while True:
        max_key = len(SYMBOLS) - 1
        print(f"Enter the size of key ranging from 0 to {max_key}")
        key = input("> ")
        if not key.isdecimal():
            print("Please enter a valid number!!")
            continue
        key = int(key)
        if 0 <= key < len(SYMBOLS):
            break

    print(f"Write the message to {mode}:")
    message  = input("> ")

    message = message.upper()

    translated = ""

    for symbol in message:
        if symbol in SYMBOLS:
            location = SYMBOLS.find(symbol)
            if mode == "Encrypt":
                location = location + key
            if mode == "Decrypt":
                location = location - key

            if location >= len(SYMBOLS): #as indexes start from 0, so for 26th letter 
        # it would be 25 index thus added 1 for key makes 26 which dosent exist
                location -= len(SYMBOLS)

            elif location < 0:
                location += len(SYMBOLS)


            translated += SYMBOLS[location]
        else:
            translated += symbol

    print(f"The {mode} message is:  ")
    if mode == "Decrypt":
        print(translated.title())
    else:
        print(translated)

    try:
        pyperclip.copy(translated)
    except:
        pass

    print("Do you wanna try this again? (y/n)")
    reponse = input("> ")
    if reponse.upper().startswith("Y"):
        continue
    else:
        break
