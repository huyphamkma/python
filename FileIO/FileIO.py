fo = open("test.txt", "w+")
fo.write("1234567890")
fo.close()


fi = open("test.txt", "r+")
fi.seek(3,0)
str = fi.read(5)
print(str)
fi.close()

