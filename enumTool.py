file = open("Departments.txt", "r")
out = open("Out.txt", "w")
paragraph = file.readlines()

#for i in file:
#   out.write("'%s'," % (i))

for line in paragraph:
    line = line.replace("\n","','")
    out.write(line)