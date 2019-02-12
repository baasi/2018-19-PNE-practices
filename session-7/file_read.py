# Example of reading a file located in our local filesystem

name = "mynotes.txt"

# Opening the file
myfile = open(name, "r")

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))
