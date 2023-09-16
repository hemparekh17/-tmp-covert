# /tmp Covert Channel

## About the code
1. Can be affected by sender.
2. Modulation can be observed by the reciever. 
3. Modulation is the creation/deletion of files in '/tmp'
4. Quantification is binary (existance/absence = 1/0)
5. Encoding is binary/ASCII


## Sender.py
1. Message Encoding:
    - The script encodes a specific message into binary and ASCII formats, representing characters as 8-bit binary strings and and ASCII values, respectively
2. Modulation Simulation:
    - It creatively simulates the modulation process by manipulating file existance within a specified diretory ('/tmp/CC-test') to represent binary bits (1s and 0s).
3. Randome File Generation:
    - Files with random names and sizes are generated to represent the binary bits of the encoded message, contributing to the modulation simulation.
4. Transmission Delay Simulation:
    - The Script introduces variable trnasmissions delays by simulating delays of random durations between file creations, enhancing the realism of the modulation process.


## Reciever.py
1. Message Deocding Process:
    - The script decodes a modulated message by checking the existence of files in a specified directory, treating files as '1' bits and directories as '0' bits.
2. Binary to ASCII conversion:
    - A function called binary_to_ascii is defined to convert the binary string to ascii representation in 8-bit chunks
3. Modulated Message Representation:
    - The modulated message is represented by the existence of files ('1' bits) and directories ('0' bit) in the designated directories.
4. Decoding Modulated Message:
    - The script reads the directory, assigning '1' for files and '0' for directories, effectively decoding the modulated message.
5. Reconstructing the Original Message:
    - The deocded binary message is converted back into ASCII characters using the binary_to_ascii function, reconstructing the original message
    