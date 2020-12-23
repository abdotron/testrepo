def check_division (x,y,z):
	index=["x","u",1]
	# this function returns the maximum division of permutations of x,y,z
	divisor=1 #down
	divided=1 #up
	if x>y and x > z:
		divided = x
		index[0]="x"
        	if y>z:
            		divisor=y
            		index[1]="-x"
        	else:
            		divisor=z
            		index[1]="u"        
	elif y>z and y > x:
		divided = y
		index[0]="-x"
		if x>z:
			divisor=x
			index[1]="x"
		else:
			divisor=z
			index[1]="u"
	else:
		divided = z
		index[0]="u"
		if x>y:
			divisor=x
			index[1]="x"
		else:
			divisor=y
			index[1]="-x"

	index[2]= (divided/divisor)
	return index #3 5 6 8




print check_division(2,3,1)