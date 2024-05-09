
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # Letters defined for encryption.

def encrypt(plain_txt,shift): # Encryption process
    cipher_txt=''
    for char in plain_txt:
        position=alphabet.index(char)
        ne_post=(position+shift)%26
        cipher_txt +=alphabet[ne_post]
    print(f'[+] Cipher text :{cipher_txt}')   # output 
def decrypt(cy_txt,shift):  # Decryption process
    plain_text=''
    for char in cy_txt:
        position=alphabet.index(char)
        ne_post=(position-shift)%26
        plain_text +=alphabet[ne_post]
    print(f'[+] Plain Text :{plain_text}')  # output

    
print('[!] caesar cipher ')         # Heading
mode=str(input('[+] For Encrypt or Decrypt (e/d):'))        # Mode selection for encryption 
print('[!] Please use Uppercase only.')
if mode=="e":           # condition define
        plain_txt=str(input('[+] Enter your Message :'))        # input the message
        shift=int(input('[+] Enter shift / key :'))         # input the shift
        encrypt(plain_txt,shift)        # call the funtion encrypt
elif mode=="d":         # condition define
        cy_txt=str(input('[+] Enter message for Decrypt :'))     # input the cypher text
        shift=int(input('[+] Enter shift / key :'))     # input the shift
        decrypt(cy_txt,shift)   # call the funtion decrypt
          