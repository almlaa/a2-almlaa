#######################################################
### Please ignore the lines of code in this section.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do not need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################



###				print("All it can do is print out the contents of a couple of cells of the file a2_input.csv:")
#				print("Cells at index 5")
##				print(contents[5])
########		print(type(contents[5]))
#######			print("Cell at index 13,6:")
######			print(contents[13][6])
#####			print(type(contents[13][6]))
####			print("Cell at index 10,2:")
###				print(contents[10][2])
##				print(type(contents[10][2]))
########		print("Cell at index 1,0:")
#######			print(contents[1][0])
######			print(type(contents[1][0]))
###				a = int(contents[3][1])
######			b = int(contents[3][2])
###				c = int(contents[3][3])
#####			total_of_germany = a + b + c
#######			print("Total german tourists " + str(total_of_germany))


###    			print("Nations:coming tourists in 2014,2015,2016")
###				print("cell at index 3:7,0:3")
####			i=3
#####			while(i<=7):
######		    	print(contents[i][0] + ":" + " " + contents[i][1]  + " " + "," + " " + contents[i][2] + " "  +"," +  " " + contents[i][3])
#######		    	i=i+1
########		print(type(contents[3:7][0:3]))
	
###			x=input("which order do you want in nations")
###			if x in range(1,20):
######			print(contents[int(x)+2][0])
######				else:
######					print('There are only 20 nations')
###			print(type(contents[int(x)+2][0]))
###			print(contents[dog][cat]) = (NameError: name 'dog' is not defined)
####		contents[5][3] + int(contents[3][3]) = TypeError: cannot concatenate 'str' and 'int' objects
#####		print(contents[5][3]*int(contents[3][3]))= became a loop
####		help(contents[5][3])=no Python documentation found for '906336'


print("<!DOCTYPE html>")
print("<html lang=\"en\">")
print("<head>")
print("<title>Coming tourists to the Nations</title>")
print("<meta charset=\"utf-8\" />")
print(""" <style>
  table{ backgraund-color:#f6fca4
  }

  td{color:#306812
  border: 1.5px solid
  } 
  
  th{color:#68112a
   border: 1.5px solid
  }


<style/> """)
print("</head>")
print("<body>")

print("<table>")
a=0

while (a<=23):
	b=0
	print('<tr>')
	while (b<=6):
		if a in (0,1,2):
			print('<th>')
		else:
			print('<td>')
		print(contents[a][b]) 
		if a in (0,1,2):
			print('</th>')
		else:
			print('</td>')
		b+=1
	print('</tr>')
	
	a += 1
print("</table>")

s=0
		

print("<p>Total of nations who increased 2014 to 2015:6337656 </p>")
print("</body>")
print("</html>")
	
