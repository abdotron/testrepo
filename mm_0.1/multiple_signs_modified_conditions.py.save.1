import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
from matplotlib import style
from subprocess import call
import threading
import pdb
global last_displayed
def open_file(file):
        f = open(file,"r")
	#skip first line
        f2 =f.readlines()
        f.close
	return f2[1:]

def write_tofile(f2,filename):
        f2length=int(len(f2))
        f = open(filename,"w+")
        for line in range(f2length):
                f.write("%s"%f2[line])
        f.close()

##################################################################data analytics section###################################################
def get_agents(time_stamp,agents_list,signs_list,rangex,rangey,rangez):
	diffx=1 #direction check sensitivity for x direction .This is important only to check the sign arrow direction .To determine if the agent continues moving in the same direction or turns right or left
	diffy=1 #direction check sensitivity for y direction 
	diffz=1	#direction check sensitivity for z direction
        check_x=0 #this is changed for each sign
        check_y=0 #this is changed for each sign
        check_z=0 #this is changed for each sign

	timestampdiff=10 #not used
	number_of_agents=600 #not used
	signs=[] #the list of filtered agents positions apended with the direction of the arrow and each sign direction
#        time_stamps_list=list(dict.fromkeys(time_stamps_list))
# this function returns the agents ids at all signs in a certain time  returned agents[sign_id] regraded that the signs are in csv file with id order in 0,1,2,3,... sample output [['1001', '1002'], ['1064', '1073']] i.e [[ids@sign0], [ids@sign1]]
	i=1
	#debugger
	#pdb.set_trace()
	min_signs=[float(agents_list[0].split(',')[2]),float(agents_list[0].split(',')[3]),float(agents_list[0].split(',')[4])]
	max_signs=[float(agents_list[0].split(',')[2]),float(agents_list[0].split(',')[3]),float(agents_list[0].split(',')[4])]
	for list_index in range(0,len(agents_list)):
		line=agents_list[list_index]		
		#finding the global minimum and maximum
		min_signs[0]=float(line.split(',')[2]) if min_signs[0] > float(line.split(',')[2]) else min_signs[0]
		min_signs[1]=float(line.split(',')[3]) if min_signs[1] > float(line.split(',')[3]) else min_signs[1]
		min_signs[2]=float(line.split(',')[4]) if min_signs[2] > float(line.split(',')[4]) else min_signs[2]
		max_signs[0]=float(line.split(',')[2]) if max_signs[0] < float(line.split(',')[2]) else max_signs[0]
		max_signs[1]=float(line.split(',')[3]) if max_signs[1] < float(line.split(',')[3]) else max_signs[1]
		max_signs[2]=float(line.split(',')[4]) if max_signs[2] < float(line.split(',')[4]) else max_signs[2]
		for i in range(0,len(signs_list)):
	                X=signs_list[i].split(',')[1]
        	        Y=signs_list[i].split(',')[2]
                	Z=signs_list[i].split(',')[3]
			rangex=float(signs_list[i].split(',')[5])
			rangey=float(signs_list[i].split(',')[6])
			rangez=float(signs_list[i].split(',')[7])

			if (1):
				if ((float(X)-rangex)<=float(line.split(',')[2])) and (float(line.split(',')[2])<=(float(X)+rangex)) and ((float(Y)-rangey)<=float(line.split(',')[3])) and (float(line.split(',')[3])<=(float(Y)+rangey)) and ((float(Z)-rangez)<=float(line.split(',')[4])) and (float(line.split(',')[4])<=(float(Z)+rangez)):
					signs.append(signs_list[i].split(',')[4]+","+str(i)+","+line) #append the check direction and sign id as i and agent position as line
			#check only in z put it one to check only in z direction
			#if (0):
			#	if (((float(Z)-rangez)<=float(line.split(',')[4])) and (float(line.split(',')[4])<=(float(Z)+rangez))):
			#		signs.append(str(list_index)+","+str(i)+","+line)


	write_tofile(signs,"signs_scrampled.csv")
	timestampdiff=10 # not used
	number_of_agents=600 # not used
	k=1 #not used
	directions=[]
	data=[]
	# set 1 for the direction to be taken into consideration x or y or z 
	i=0
	#signs=open_file("./signs_scrampled.csv")
#	data.append(signs[0]) 
#######signs is the list of formatted agents positions 
	for i in range(0,len(signs)):
		if (float(signs[i].split(',')[1])!=float(k)):
			#filename="sign_direction"+str(k)
	                #write_tofile(directions,filename)
			#extracting position data to files
			directions=[]
			k=k+1
		j=0
		# search for agent in list with the same id, the interesting direction to be checked pers sign
		for j in range(0,len(signs)):
                        if (signs[i].split(',')[0]=='x'):
                                check_x=1
                        if (signs[i].split(',')[0]=='y'):
                                check_y=1
                        if (signs[i].split(',')[0]=='z'):
                                check_z=1
			# same agent bigger time stamp not te same sign
			if (check_x==1):
				# first next sign (float(signs[j].split(',')[1])==float(signs[i].split(',')[1])+1) and
###############################check if not the same sign , the same agent and bigger frame as a timestamp
				if ((signs[j].split(',')[1]!=signs[i].split(',')[1]) and (signs[j].split(',')[3]==signs[i].split(',')[3]) and (float(signs[j].split(',')[2]) > float(signs[i].split(',')[2]))):			
                               #straight condition if the difference in next position is less than diffx
					if (float(signs[i].split(',')[4])-float(signs[j].split(',')[4])>=diffx):
						data.append("x"+","+signs[i])
					elif (float(signs[i].split(',')[4])-float(signs[j].split(',')[4])<=-diffx):
                        	                data.append("-x"+","+signs[i])
					else:
						data.append("u"+","+signs[i])

					break
                        if (check_y==1):
                                if ((signs[j].split(',')[1]!=signs[i].split(',')[1]) and (signs[j].split(',')[3]==signs[i].split(',')[3]) and (float(signs[j].split(',')[2]) > float(signs[i].split(',')[2]))):
                               #straight condition if the difference in next position is less than diffx
				#########it hould be implemented this way if the difference < -diffx then it should have goone in the negative x direction replace the else
                                        if (float(signs[i].split(',')[5])-float(signs[j].split(',')[5])>=diffy):
                                                data.append("x"+","+signs[i])
                                        elif (float(signs[i].split(',')[5])-float(signs[j].split(',')[5])<=-diffy):
                                                data.append("-x"+","+signs[i])
					else:
						data.append("u"+","+signs[i])
                                        break
#			pdb.set_trace()
                        if (check_z==1):
                                if ((signs[j].split(',')[1]!=signs[i].split(',')[1]) and (signs[j].split(',')[3]==signs[i].split(',')[3]) and (float(signs[j].split(',')[2]) > float(signs[i].split(',')[2]))):
                               #straight condition if the difference in next position is less than diffx
                                        if (float(signs[i].split(',')[6])-float(signs[j].split(',')[6])>=diffz):
                                                data.append("x"+","+signs[i])
					#	last_displayed[int(signs[i].split(',')[1])]="x"
                                        elif (float(signs[i].split(',')[6])-float(signs[j].split(',')[6])<=-diffz):
                                                data.append("-x"+","+signs[i])
					else:
						data.append("u"+","+signs[i])
					#	last_displayed[int(signs[i].split(',')[1])]="-x"
                                        break
			#agent not found again increases ordered_display length 
				else:
					if (j==len(signs)-1):
						#data.append("x"+","+signs[i])
 						index=int(signs[i].split(',')[1])
						#data.append(str(last_displayed[index])+","+signs[i])	
	write_tofile(data,"data_scrampled.csv")
	print min_signs
	print max_signs
	return data
###########################initial display##################33
def get_initial(length,ordered_display):
	#initial	
	last_displayed=[2 for i in range(length)]
	for j in range(0,length):
		for k in range(0,len(ordered_display)):
			if int(ordered_display[k].split(',')[2])==int(j):
                                if (ordered_display[k].split(',')[0]=="x"):
                                	last_displayed[j]=1
					break
                                if (ordered_display[k].split(',')[0]=="-x"):
                                        last_displayed[j]=-1
                                        break
                                if (ordered_display[k].split(',')[0]=="u"):
                                        last_displayed[j]=2
					break
#	print length
	
	return last_displayed
########## check division of 3 elements###################3

def check_division2 (x,y,z):
	index=["x","u",1]
	if x==0 and y==0:
		index=["u","x",-1]
		return index
	elif x==0 and z==0:
		index=["-x","x",-1]
		return index
	elif y==0 and z==0:
		index=["x","x",-1]
		return index
	else:
		if x !=0 and y !=0 and z !=0 and x > y and x > z :
			if y>z :
				divided=x
				divisor=y
				index[0]='x'
				index[1]='-x'
			else:
				divided=x
				divisor=z
				index[0]='x'
				index[1]='u'
			
		elif x!=0 and y!=0 and z !=0 and y>x and y>z:
			if x>z:
				divided=y
				divisor=x
				index[0]='-x'
				index[1]='x'
			else:
				divided=y
				divisor=u
				index[0]='-x'
				index[1]='u'
		elif x!=0 and y!=0 and z!=0 and z>x and z>y:
			if x>y:
				divided=z
				divisor=x
				index[0]='u'
				index[1]='x'
			else:
				divided=z
				divisor=y
				index[0]='u'
				index[1]='-x'
		elif x==0 and y!=0 and z!=0:
			if y>z:
				divided=y
				divisor=z
				index[0]='-x'
				index[1]='u'
			else:
				divided=z
				divisor=y
				index[0]='u'
				index[1]='-x'
		elif (y==0 and x!=0 and z!=0):
			if x>z:
				divided=x
				divisor=z
				index[0]='x'
				index[1]='u'
			else:
				divided=z
				divisor=x
				index[0]='u'
				index[1]='x'
		elif z==0 and x !=0 and y !=0:
			if x>y:
				divided=x
				divisor=y
				index[0]='x'
				index[1]='-x'
			else:
				divided=y
				divisor=x
				index[0]='-x'
				index[1]='x'

		else: 
			index=["x","-x",-1]
	index[2]=int(divided/divisor)
	return index #3 5 6 8

###############################elemenating redundant timestamps and summarizing###############33
def agents_average(ordered_display,selected_signs):
	avereged=[]
	out_signs=0
	#selected_signs the signs that are at the same positions and there is a possibility that the agents at that time will be divided
	####################################
	################################
	###########===================DANGER=============
	########selected_signs is a variable of the signs that should be static and is set at the beginning also it is the same as skip_signs
	selected_signs=[0,0]
	timestamp=-1
	j=0
	count=0
	i=0
	first_second= int(ordered_display[0].split(',')[8].split(':')[2])+60*int(ordered_display[0].split(',')[8].split(':')[1])+60*60*int(ordered_display[0].split(',')[8].split(':')[0])	
	last_display_second=0
	last_second= int(ordered_display[len(ordered_display)-1].split(',')[8].split(':')[2])+60*int(ordered_display[len(ordered_display)-1].split(',')[8].split(':')[1])+60*60*int(ordered_display[len(ordered_display)-1].split(',')[8].split(':')[0])
#	print first_second
#	print last_second
	i=0
	while i <len(ordered_display):
		averaged_sub_list=signs_list[:] #copy the list and creating new one [:] is mandatory
		count_list=[[0,0,0] for q in range(0,len(signs_list))]
		count_x=0
		countx=0
		countu=0
		current_sign=ordered_display[i].split(',')[2]
		previous_second= int(ordered_display[i].split(',')[8].split(':')[2])+60*int(ordered_display[i].split(',')[8].split(':')[1])+60*60*int(ordered_display[i].split(',')[8].split(':')[0])	
		j=i
		while j <len(ordered_display):
			current_second= int(ordered_display[j].split(',')[8].split(':')[2])+60*int(ordered_display[j].split(',')[8].split(':')[1])+60*60*int(ordered_display[j].split(',')[8].split(':')[0])	
			averaged_sub_list[int(current_sign)]=ordered_display[i]
			#print current_second
			#print  str(i)+','+str(j)
			if current_second > previous_second+averaging_time_seconds:
				break
		#print i
			else :
				for f in range(0,len(signs_list)) :
				#sign_index,countx,count_x,countu
					if f not in skip_signs : #don't calculate exit signs

						if ordered_display[j].split(',')[0]=='x' and int(ordered_display[j].split(',')[2])==f and int(ordered_display[j].split(',')[4]) !=int(ordered_display[i].split(',')[4]):
							count_list[f][0]=count_list[f][0]+1
						elif ordered_display[j].split(',')[0]=='u' and int(ordered_display[j].split(',')[2])==f and int(ordered_display[j].split(',')[4]) !=int(ordered_display[i].split(',')[4]):
							count_list[f][2]=count_list[f][2]+1
						elif ordered_display[j].split(',')[0]=='-x' and int(ordered_display[j].split(',')[2])==f and int(ordered_display[j].split(',')[4]) != int(ordered_display[i].split(',')[4]):
							count_list[f][1]=count_list[f][1]+1
						else :
							out_signs=out_signs+1 #dummy variable
						if ordered_display[j].split(',')[2] !=ordered_display[i].split(',')[2]:
							averaged_sub_list[int(ordered_display[j].split(',')[2])]=ordered_display[j].split(',')[0]+','+ordered_display[j].split(',')[1]+','+ordered_display[j].split(',')[2]+','+ordered_display[j].split(',')[3]+','+ordered_display[j].split(',')[4]+','+ordered_display[j].split(',')[5]+','+ordered_display[j].split(',')[6]+','+ordered_display[j].split(',')[7]+','+ordered_display[i].split(',')[8]+','+ordered_display[i].split(',')[9]
						else :
							averaged_sub_list[int(ordered_display[j].split(',')[2])]=ordered_display[i]


			j=j+1
		#######deleteing non necessary signs info from the sub list
		sub_list_index=0
		count_list_index=0
		for m in range(0,len(count_list)) :
			if len(averaged_sub_list[m-sub_list_index]) ==len(signs_list[m]):
				del averaged_sub_list[m-sub_list_index]
				sub_list_index=sub_list_index+1
                        if count_list[m-count_list_index]==[0,0,0]:
                                del count_list[m-count_list_index]
                                count_list_index=count_list_index+1

		print count_list
		print averaged_sub_list
		for r in range(0,len(count_list)):
			hi=check_division2(count_list[r][0],count_list[r][1],count_list[r][2])
			if 5>= hi[2] >= 1  :
				averaged_sub_list[r]=hi[0]+hi[1]+","+averaged_sub_list[r].split(',')[1]+","+averaged_sub_list[r].split(',')[2]+","+averaged_sub_list[r].split(',')[3]+","+averaged_sub_list[r].split(',')[4]+","+averaged_sub_list[r].split(',')[5]+","+averaged_sub_list[r].split(',')[6]+","+averaged_sub_list[r].split(',')[7]+","+averaged_sub_list[r].split(',')[8]+","+averaged_sub_list[r].split(',')[9]
#############################append only the seconds of interest
                if i< len(ordered_display):
			for t in range(0,len(averaged_sub_list)):
                                avereged.append(averaged_sub_list[t])

		last_display_second=current_second
		i=j
		i=i+1
	write_tofile(avereged,"./data_summarized")
	return avereged

##################################################3plotting section##################################################################3####3
#animate the signs to be plotted  the plotted directions according to the direction of the agent
def animate(i):
	right=mpimg.imread('right.png')
	left=mpimg.imread('left.png')
	straight=mpimg.imread('up.png')
	ux=mpimg.imread('ux.png')
	u_x=mpimg.imread('u_x.png')
	minusxu=mpimg.imread('minusxu.png')
	minusxx=mpimg.imread('minusxx.png')
	x_x=mpimg.imread('x_x.png')
	xu=mpimg.imread('xu.png')
	fig.clear()
	number_of_plot=3
	
	#j is counter on the sub plots we have # of subplots = # of signs
	for j in range(0,len(signs_list)):
		sub_plot_index=number_of_plot*100+number_of_plot*10+j+1
                sign_name="Sign ("+str(j+1)+")"
		plt.subplot(sub_plot_index)
		
	#in case it didn't find the direction for the agent plot the previous one
		if ( 1 ): #####################just to display previous displayed value
                	if (last_displayed[j]==1):
                		plt.imshow(right)
                	if (last_displayed[j]==-1):
                		plt.imshow(left)
                	if (last_displayed[j]==2):
                		plt.imshow(straight)
                	if (last_displayed[j]==3):
                		plt.imshow(minusxu)
                	if (last_displayed[j]==4):
                		plt.imshow(xu)
                	if (last_displayed[j]==5):
                		plt.imshow(minusxx)
                	if (last_displayed[j]==6):
                		plt.imshow(x_x)
                	if (last_displayed[j]==7):
                		plt.imshow(u_x)
                	if (last_displayed[j]==8):
                		plt.imshow(ux)
                plt.title(sign_name,fontsize=16)
	        plt.axis('off')
		plt.xticks([])
		plt.yticks([])
		# skip certain signs if you don't want to plot certain signs##############static signs
		if j in skip_signs:
			plt.imshow(straight)
			continue
	#check for each element in the small data for the time stamp = the same plotted time stamp and the sign number and plot it for the current sign
		for k in range(0,len(ordered_display)):
			#print k 
			#print ordered_display[k]
			current_second= int(ordered_display[k].split(',')[8].split(':')[2])+60*int(ordered_display[k].split(',')[8].split(':')[1])+60*60*int(ordered_display[k].split(',')[8].split(':')[0])
			if (int(ordered_display[k].split(',')[2])==int(j) and  current_second==int(i+plotting_time_delay)):
				if (ordered_display[k].split(',')[0]=="x"):
					global last_displayed
					last_displayed[j]=1
					plt.imshow(right)
					#print str(j)+"here"+" "+str(last_displayed[j])
					break
					#zero means no change occured on the position so plot the previous position
				if (ordered_display[k].split(',')[0]=="-x"):
					global last_displayed
					last_displayed[j]=-1
					plt.imshow(left)
					break
                                if (ordered_display[k].split(',')[0]=="u"):
					global last_displayed	
					last_displayed[j]=2
					plt.imshow(straight)			
					break
                                if (ordered_display[k].split(',')[0]=="-xu"):
					global last_displayed	
					last_displayed[j]=3
					plt.imshow(minusxu)			
					break
                                if (ordered_display[k].split(',')[0]=="xu"):
					global last_displayed	
					last_displayed[j]=4
					plt.imshow(xu)			
					break
                                if (ordered_display[k].split(',')[0]=="-xx"):
					global last_displayed	
					last_displayed[j]=5
					plt.imshow(minusxx)			
					break				
                                if (ordered_display[k].split(',')[0]=="x-x"):
					global last_displayed	
					last_displayed[j]=6
					plt.imshow(x_x)			
					break	
                                if (ordered_display[k].split(',')[0]=="u-x"):
					global last_displayed	
					last_displayed[j]=7
					plt.imshow(u_x)			
					break
                                if (ordered_display[k].split(',')[0]=="ux"):
					global last_displayed	
					last_displayed[j]=8
					plt.imshow(ux)			
					break

		print i
		#print last_displayed
		#print ordered_display[k]
	return 
###playing video
def vid1():
#	call(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe","./left and right movie for testing.mov"])
        call(["mplayer","-zoom","-quiet","-xy","600","./left and right movie for testing.mov"])




#agents_positions="./left and right agents positions .csv"
agents_positions="./right and left final runs with clock time .csv"
signs_positions="./signs_positions_latst_test.csv"
signs_list=open_file(signs_positions)
#timescale=4.5
skip_signs=[1,2] #static signs
averaging_time_seconds=6
plotting_time_delay=0
#at the same time stamp some agents are divided among different signs for certain signs
#calling the filteration system

ordered_directions=get_agents("0",open_file(agents_positions),signs_list,0.5,0.5,1)

#ordered_directions=open_file("./data_scrampled.csv")
#
ordered_display=agents_average(ordered_directions,skip_signs)
#ordered_display=open_file("./data_summarized")

#print check_division2(4,2,1)

#initialize the list which will store old signs positions so i store the previous plotted value
#initial value isn't on timestamp zero as some signs don't get changed until final time stamps


#initialization of last version of display
last_displayed=get_initial(len(signs_list),ordered_directions)
#print last_displayed

#last_displayed=[8 for i in range(0,len(signs_list))]
a=8
style.use('fivethirtyeight')
fig = plt.figure()
#the signs to skip plotting which will stay the same chosen direction 1 neglect 0 plot
####skip_signs=[1,2] #######################################static displays defined here 



thread1 = threading.Thread(target = vid1)
thread1.start()
ani = animation.FuncAnimation(fig, animate, interval=int(500)) #the interval here is doubled so a 500 ms *2 =1 Second
plt.show()
	 





