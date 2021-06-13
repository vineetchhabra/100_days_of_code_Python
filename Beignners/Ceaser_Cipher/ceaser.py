from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

   

def ceaser(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
            
    for i in plain_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += i
    print(f"The {cipher_direction}d text is {cipher_text}")
    
shift = shift % 26

ceaser(plain_text=text, shift_amount=shift, cipher_direction=direction) 

