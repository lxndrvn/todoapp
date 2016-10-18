my_file = 'todo.txt'

def load():
    with open("todo.txt", "a") as my_file:
         lines = [line.rstrip('\n') for line in open("todo.txt")]
         for i in lines:
             todolist.append(i)
         return todolist

def write(line):
    with open("todo.txt", "a") as my_file:
         my_file.write(line +'\n')

def save():
    for i in range (0,len(todolist)):
        lines = str(todolist[i])
        write(lines)

def clear():
    with open(my_file, 'w'): pass

todolist = []
mark1 = "[ ]"
mark2 = "[x]"

while True:
    
    getdata = input("Please specify a command [list, add, mark, archive]: ")

    command = ['list', 'add', 'mark', 'archive']

    todolist = []

    load()

    if  getdata == command[0]:
        print ("You saved the following to-do items: ")
        line = 1
        for i in todolist:
            print (line,'.',i)
            line += 1   

    elif getdata == command[1]:
        print("Add an item:")
        todolist.append(mark1 + " " + input(""))
        print("Item added.")
        
    elif getdata == command[2]:
        print(command[0])
        print('\n')
        print("You saved the following to-do items:")
        line = 1
        for i in todolist:
            print (line,'.',i)
            line += 1 
        ans = int(input("Which one you want to mark as completed:"))
        if todolist[ans-1][1] == " ":
            todolist[ans-1] = mark2 + todolist[ans-1][3:]

    elif getdata == command[3]:
        print('\n')
        for i in todolist:
            if i[1] == 'x':
                todolist.remove(i)
        print ("All completed tasks got deleted.")
    
    elif getdata not in command:
        exit()

    clear()

    save()

    todolist = []