# Caesar cipher

# ----------------
# Encrypt message
# ----------------
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 5

newmsg = ''
message = input('Enter new message: ')

for character in message:
    position = alphabet.find(character)
    newposition = (position+key)%26
    newchar = alphabet[newposition]
    print('Encrypted new character is', newchar)
    newmsg += newchar
print('The encrypted final message is:', newmsg)

# ----------------
# Decrypt message
# ----------------
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 5

newmsg = ''
message = input('Enter encrypted message: ')

for character in message:
    position = alphabet.find(character)
    newposition = (position-key)%26
    newchar = alphabet[newposition]
    print('Derypted new character is', newchar)
    newmsg += newchar
print('The decrypted final message is:', newmsg)
