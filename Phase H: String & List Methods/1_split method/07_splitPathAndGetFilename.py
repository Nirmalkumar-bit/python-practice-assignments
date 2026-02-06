# Split a file path by '/' and print only the filename.
# Expected outcome: prints notes.txt

path = "/home/alex/docs/notes.txt"
parts = path.split("/")
filename =parts[-1] 
print(filename)
