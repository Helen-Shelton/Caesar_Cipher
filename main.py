import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift, direction):
  caesar_message = '' #empty string to add our ciphered message to
  if (direction != 'decode') & (direction != 'encode'): #bitwise and operator checks if BOTH conditions are true, and only  proceeds if BOTH are true
    print("\nThat is not a valid option")
    return
  if direction == 'decode': #negative shift if decoding
      shift *= -1
  for letter in message:
    if letter.isalpha(): # or could do: "if letter in alphabet: "
      new_index = alphabet.index(letter) + shift
      if new_index > (len(alphabet)-1): #for wrap around in case new index exceeds number of alphabet indices (doesn't happen with decode (negative shift because we can have negative indices))
        new_index -= len(alphabet) 
      caesar_message += alphabet[new_index]
    else:
      caesar_message += letter #adds anything thats not a letter to the ciphered message without using the cipher algorithm
  print(f"The new {direction}d message is: {caesar_message}")


# def encrypt(message, shift):
#   encode_message = ''
#   for letter in message: 
#   #for every letter/index in input message, new index is index of string in alphabet list plus the shift
#     new_index = alphabet.index(letter) + shift
#     #if the new index is greater than the number of alphabet indices, wrap around to the beginning of alphabet
#     if new_index > (len(alphabet)-1):
#       new_index -= len(alphabet) 
#       #add a 1 to alphabet length to account for zero index when wrapping around
#     encode_message += alphabet[new_index]
#     #the old string is the string at the new_index calculated above
#   print(f"The encoded text is: {encode_message}")

# def decrypt(message, shift):
#   decode_message = ''
#   for letter in message: 
#   #for every letter/index in input message, new index is index of string in alphabet list minus the shift
#     new_index = alphabet.index(letter) - shift
#     decode_message += alphabet[new_index]
#     #the old string is the string at the new_index calculated above
#   print(f"The decoded text is: {decode_message}")


print(art.logo)
keep_running = True
while keep_running: #exits when user no longer wants to use the program
  direc = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  num = int(input("Type the shift number:\n"))

  if num > len(alphabet): #incase shift exceeds alphabet length:
    num %= len(alphabet) # just take remainder so we can start from index 0 again
  caesar(message = text, shift = num, direction = direc)
  keep_running = int(input("\nWould you like to keep ciphering? Type 1 for 'Yes' and 0 for 'No'\n"))


# if direction == 'encode':
#   encrypt(message = text, shift = num)
# elif direction == 'decode':
#   decrypt(message = text, shift = num)
# else:
#   print("That is not a valid option, you must type 'encode' or 'decode'")



