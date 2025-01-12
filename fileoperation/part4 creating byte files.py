# Writing binary data to a file
with open("test4.bin", "wb") as f:  # 'wb' mode for writing binary data
    f.write(b"\x01\x02\x03")  # Writing three bytes of binary data

# Reading binary data from a file
with open("test4.bin", "rb") as f:  # 'rb' mode for reading binary data
    print(f.read())  # Print the contents of the file, which will be in bytes
