filename = 'text.txt'
outputname = 'output.txt'

with open(filename) as file, open(outputname, 'w') as output:
    for i in file:
        if len(i) > 5:  
            output.write(i)

print("готово")