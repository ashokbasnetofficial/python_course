# implementing ceaser cipher
import string 
lowecase_letter =list(string.ascii_lowercase)
uppercase_letter = list(string.ascii_uppercase)
def encrypt(message, shift_key):
       cipher_text =''
       for letter in message:
           positon = lowecase_letter.index(letter)
           new_position = (positon+shift_key)%26
           print(new_position)
           new_letter = lowecase_letter[new_position]
           cipher_text+=new_letter
       return  cipher_text
def decrypt(message, shift_key):
       plain_text =''
       for letter in message:
           positon = lowecase_letter.index(letter)
           new_position = (positon-shift_key)%26
           print(new_position)
           new_letter = lowecase_letter[new_position]
           plain_text+=new_letter
       return  plain_text
isTrue = 'yes'
while isTrue =='yes':
      direction = str(input("Please type 'encode' to encrpyt and 'decode' to decrypt the message: ")).lower();
      print(direction)
      message = str(input("Type your message:"));
      shift_key = int(input("Enter the shift key:"));
      if direction == 'encode':
        cipher_text = encrypt(message=message,shift_key=shift_key);
        print(f"Your chiper text is {cipher_text}")
      if direction =='decode':
        plain_text = decrypt(message=message,shift_key=shift_key);
        print(f"Your plain text is {plain_text}")
      isTrue = str(input("Do you want to continue? Type 'yes' for continue and 'no' for exit"))
    
               
