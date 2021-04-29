

###       Affine Cipher Functions          ###
# affine gcd
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# affine encrytion function 
def affine_encrypt(text, key): 
	return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) 
				+ ord('A')) for t in text.upper().replace(' ', '') ]) 

# affine invers function
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# affine decryption function 
def affine_decrypt(cipher, key): 
	return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) 
					% 26) + ord('A')) for c in cipher ]) 

# gcd co prime function
def __gcd(a, b):  
    if (a == 0 or b == 0): return 0
    if (a == b): return a 
    if (a > b):  
        return __gcd(a - b, b) 
    return __gcd(a, b - a) 
  
# checks with m=26 if user input is co prime 
def coprime(a, m):  
        if ( __gcd(a, m) == 1): 
            print("Co-Prime,") 
        else: 
            print("Not Co-Prime, Try Again")
            exit()
###      Vigenere Cipher Functions          ###
# Vigenere encrypt
def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ' '
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

# Vigenere decrypt
def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ' '
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext


cipher = input("Which cipher would you like to choose Affine or Vigenere(A/V): ")

if cipher == 'A':
    print('You picked Affine cipher')
    def a_main():
        #mode
        mode = input('Encrypt or Decrypt(E/D)')
        if mode == ('E'):
        # user input message
            user_text = input('Enter your message:')
            text = user_text
        # unser input A key
            a_key = int(input('Enter coprime to be your A key:'))
            a = a_key
        # co prime checker
            a ; m = 26
            coprime(a,m)
        # user input B key
            b_key = int(input('Enter you key for B:'))
            b = b_key
        # encrrypt fun called
            key = [a, b] 
            affine_encrypted_text = affine_encrypt(text, key) 
            print('Encrypted Text: {}'.format(affine_encrypted_text)) 
        
        elif mode == ('D'):
        # user input cipher text
            user_ciphertext = input('Enter the cipher here :')
            cipher = user_ciphertext
        # user input A key
            user_a = int(input('Enter A key:'))
            a = user_a
            user_b = int(input('Enter B key:'))
            b = user_b
            key = [a,b]
        # decrypt fun called
            decrypt = affine_decrypt(cipher, key)
            print("Decrypt Message:{}".format(decrypt))
    a_main()
elif cipher == 'V':
    print('You picked Vigenere cipher')
    def v_main():
        #mode
        mode = input('Encrypt or Decrypt(E/D)')
        if mode == ('E'):
        # User input message
            user_text = input('Enter message here :')
            plaintext = user_text.upper()
        # user input key
            user_key = input('Enter key:')
            key = user_key.upper()
            if len(key) != 5:
                print ('Must be 5 letters long, Try again')
                exit()
            else:
                pass
        # encrypt fun called  
            cipher_text = encrypt(plaintext, key)
            print("Cipher text:{}".format(cipher_text))


        elif mode == ('D'):
        # user input cipher text
            user_ciphertext = input('Enter the cipher here :') 
            ciphertext = user_ciphertext.upper()
        # user input key
            user_key = input('Enter key(5 length):')
            key = user_key.upper()
            if len(key) != 5:
                print ('Must be 5 letters long, Try again')
                exit()
            else:
                pass
        # decrypt fun called 
            decrypt_text = decrypt(ciphertext, key)
            print ("Decrypted message:{}".format(decrypt_text))
    v_main()

else:
    print('Try again')


  

