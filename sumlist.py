import  sys
sample.txt=sys.argv[0]
line_count=0
char_count=0
with open(sample.txt,"r") as file:
    for line in file:
        line_count+=1
        char_count+=len(line)
print(f"{line_count} lines")
print(f"{char_count} characters")
               