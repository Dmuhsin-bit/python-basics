#global keyword
x="beutiful"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("python is "+x)
