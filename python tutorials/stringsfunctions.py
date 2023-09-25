msg = "hello world"
print(msg.find("hello")) #function FIND --> if true returns 0, if false returns -1
print(msg.count("l"))
print(msg.replace("world", "hello"))

#formatted string
#placeholders = {}
greeting = 'hello'
name = 'Mike'
newmsg = '{}, {}. Welcome.'.format(greeting, name)
newmsg1 = f'{greeting}, {name}. Welcome!'
print(newmsg)

#functions
#args = normal positional arguments
#kwargs = keyword arguments
#allows us to accept arbitrary number of arguments

courses = ['math', 'compsci']
info = {name: "meme", 'age': 22}
def student_info(*args, **kwargs):
    print(args) #->tuple
    print(kwargs) #->dict

#use the * and ** to "unpack" correctly to args and kwargs
student_info(*courses, **info)