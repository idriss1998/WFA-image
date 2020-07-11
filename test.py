import struct
file = open("my_file", "rb")
byte = file.read(4)
print(struct.unpack('f',byte)[0])
file.close()