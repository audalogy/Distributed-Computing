# (3) Consider a triangle of numbers. By starting at the top of the triangle 
# and moving to adjacent numbers below, we want to find the maximum total from top to bottom.

# Consider the triangle with a hundred rows in the file 
# http://people.ischool.berkeley.edu/~tygar/for.i206/maxtriangle.txt

# Find the path from top to bottom with maximum value. 
# Ans: 58+72+51+52+86+56+91+80+80+78+80+31+85+81+96+54+96+35+61+64+89+92+94+53+70+76+67+70+93+7
# +88+53+41+89+83+90+30+70+92+93+52+68+72+98+88+46+79+95+80+51+97+37+90+77+89+69+6+17+54+83+73+54
# +80+86+88+98+72+87+94+67+36+86+72+76+59+81+86+63+95+64+46+93+84+50+86+64+64+65+90+82+71+23+97+88
# +52+81+56+98+97+94=7173

# URL: http://people.ischool.berkeley.edu/~tygar/for.i206/maxtriangle.txt

import urllib

if __name__ =="__main__":
	tri = []
	tri2 = []
	dummy = []
	output = []
	content = urllib.urlopen('http://people.ischool.berkeley.edu/~tygar/for.i206/maxtriangle.txt').read()
	with open("maxtriangle.txt","r") as fo:
		for line in fo:
			row = [int(i) for i in line.split()]
			tri.append(row)
		"""for i starting at the second to last row, going up each time."""
		for y in range(len(tri)-2,-1,-1):
			sum1 = 0
			sum2 = 0
			"""create empty dummy variable to hold the position of left or right depending on the larger num"""
			dummy1=[]

			"""for each cell in the triangle,"""
			for x in range(y+1):
				""" add the max of the cells below-left and below-right. 
			   the cell at the top will contain the greatest sum from bottom to top"""
				sum1 = tri[y+1][x]+tri[y][x] #left number
				sum2 = tri[y+1][x+1]+tri[y][x] #right number
				# print y,x, tri[y][x]
				tri[y][x] = max(sum1,sum2)
				if tri[y][x] == sum1:
					dummy1.append("L") #append left as "L"
				else:
					dummy1.append("R") #append right as "R"
			dummy.append(dummy1)

		"""reverse the dummy variable to go top-down"""
		dummy = dummy[::-1]
		#print dummy

	"""re-open file and create "new triangle" to trace the path"""
	with open("maxtriangle.txt","r") as fo:
		for line in fo:
			row = [int(i) for i in line.split()]
			tri2.append(row)
		col = 0
		curr_dummy = None 

		"""iterate through dummy with Left/Right directions and append numbers to output"""
		for i in range(0,len(dummy)):
			"""first row at [0][0]"""
			if output == []:
				curr_dummy = dummy[0][0] #initialize dummy
				output.append(tri2[i][col]) #append top number to ouput
				continue
			if curr_dummy == "R":
				col += 1 
			
			"""append the traced number to output"""
			output.append(tri2[i][col])

			"""update current dummy"""
			curr_dummy = dummy[i][col]
		
		"""last row"""
		if curr_dummy == "R":
			col += 1 
		output.append(tri2[i+1][col])

	sum_out = sum([int(o) for o in output])
	#print sum_out

	out_str = '+'.join([str(o) for o in output])
	print out_str + "=" + str(tri[0][0])

	
			