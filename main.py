import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo+"\n\n")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(start_text, shift_amount, cipher_direction):
    end_msg = list()
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            encrypted_position = position + shift_amount
        elif cipher_direction == "decode":
            encrypted_position = position - shift_amount
        encrypted_letter = alphabet[encrypted_position]
        end_msg.append(encrypted_letter)
    encrypted_output = ''.join(end_msg)
    print(f"\nThe {cipher_direction} message is:   {encrypted_output}\n")

ceaser(start_text = text, shift_amount = shift, cipher_direction = direction)


