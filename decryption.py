alphabet = 'abcdefghijklmnopqrstuvwxyz'
#newMessage = ''

message = input('please enter a message : ')
key = int(input('type your key btween 1&25 : '))

def decrypt(msg):
    newMessage = ''
    for character in msg:
        if character in alphabet:
            position = alphabet.find(character)
            #print(position)
            newposition = (position - key) % 26
            #print(newposition)
            newcharacter = alphabet[newposition]
            #print('the new character is: ', newcharacter)
            newMessage +=newcharacter
        else:
            newMessage +=character
    return newMessage

#newMessage = crypt(message)
# nwmsg = newMessage
newmsg = decrypt(decrypt(decrypt(decrypt(message))))

print('the message is : ', newmsg)