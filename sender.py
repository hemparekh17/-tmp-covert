import os, time, random

message = "Hello World!"

binary_message = ''.join(format(ord(char),'08b') for char in message)
ascii_message = ''.join(str(ord(char)) for char in message )

directory_path ='C:\\Users\\Hem Parekh\\AppData\\Local\\Temp\\CC-test'     # Change location to your tmp directory.
os.makedirs(directory_path, exist_ok=True)

for bit in binary_message:
    file_name = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(8))
    file_size =  random.randint(100,1000)
    file_path = os.path.join(directory_path, file_name)

    if bit =='1':
        with open(file_path, 'wb') as f:
            f.write(os.urandom(file_size))     # Creating random binary file
    else:
        os.makedirs(file_path)

    time.sleep(random.uniform(0.2,1.0))

print("Message Sent Successfully")