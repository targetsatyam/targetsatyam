# f = open('data.txt')
# if f:
#     print("file successfully opened")
#     print(type(f))
f = open("data.txt",mode = "r", buffering=10,  encoding='utf-8')
if f:
    print("opened")
print(f)