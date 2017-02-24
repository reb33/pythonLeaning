file1 = open("resources/test.png", "rb")

file2 = open("resources/test_copy.png", "wb")

file2.write(file1.read())

file1.close()
file2.close()