 #Dunder methods/ Magic methods
from todo import Todo

k_todo =Todo(name ='Collins')
e_todo = Todo(name = 'Emmanuel')


k_todo.add('I am going there')
k_todo.add('I will see you then')

print(repr(k_todo))
print(e_todo)



print(k_todo > e_todo)
print(k_todo < e_todo)

#x = [1,2,3,4,5]

#print(dir(x))
#This is similar to x.__dir__
#Similarly len(x) is x.__len__
#print(int.__add__(2,2))
# similar to 2+2
#print(str.__add__('c','r')) 
#similar to 'c'+'r'