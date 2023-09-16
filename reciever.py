import os, time, random

path =  'C:\\Users\\Hem Parekh\\AppData\\Local\\Temp\\CC-test'   # Change the path to your local tmp directory 

time.sleep(5)


def binary_to_ascii(binary_str):
    ascii_str = ''
    for i in range(0, len(binary_str),8):
        ascii_str += chr(int(binary_str[i:i+8],2))
    return ascii_str

binary_message_received = ''
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        binary_message_received += '1'
    else:
        binary_message_received += '0'


decoded_original_message  = binary_to_ascii(binary_message_received)



print("Decoded ASCII message: ", decoded_original_message)