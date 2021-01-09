alphabet = 'abcdefghijklmnopqrstuvwxyz'
#newMessage = ''

message = input('please enter a message : ')
key = int(input('type your key btween 1&25 : '))

def crypt(msg):
    newMessage = ''
    for character in msg:
        if character in alphabet:
            position = alphabet.find(character)
            #print(position)
            newposition = (position + key) % 26
            #print(newposition)
            newcharacter = alphabet[newposition]
            #print('the new character is: ', newcharacter)
            newMessage +=newcharacter
        else:
            newMessage +=character
    return newMessage

#newMessage = crypt(message)
# nwmsg = newMessage
newmsg = crypt(crypt(crypt(crypt(message))))

print('you new message is : ', newmsg)









#--------------------------------------------------------

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# key = 3
# newMessage = ''

# message = input('please enter the crypted message : ')

# for character in message:
#     if character in alphabet:
#         position = alphabet.find(character)
#         #print(position)
#         newposition = (position + key) % 26 
#         #print(newposition)
#         newcharacter = alphabet[newposition]
#         #print('the new character is: ', newcharacter)
#         newMessage +=newcharacter
#     else:
#         newMessage +=character
    
# print('the message is : ', newMessage)