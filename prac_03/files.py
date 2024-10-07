
#1

user_name = input("Enter your name: ")
new_file = "name.txt" #creating the file
new_file_open = open(new_file, "w") #write
print(user_name, file = new_file_open)

new_file_open.close()
s
