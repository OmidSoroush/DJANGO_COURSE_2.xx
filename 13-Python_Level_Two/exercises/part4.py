
try:
    f = open("simple.txt", "r")
    f.write("Test write to simple text!")
except Exception as e:
    print(e)

else:
    print("success")
    f.close()


print("hello world")
