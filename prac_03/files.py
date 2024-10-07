
#1

user_name = input("Enter your name: ")
new_file = "name.txt" #creating the file
new_file_open = open(new_file, "w") #opens name.txt to write
print(user_name, file = new_file_open, end='') #writes the user name input to the file

new_file_open.close() #closing



#2

new_file_read = open(new_file, "r")
print(f"Hi {new_file_read.read()}!")


new_file_read.close()


#3

numbers_file = "numbers.txt"
