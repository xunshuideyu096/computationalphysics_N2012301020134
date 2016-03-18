#Character Picture
l = '''@      
@      
@      
@      
@ @ @ @'''
i = """@
@
@
@
@"""
n = '''@       @
@ @     @
@   @   @
@     @ @
@       @'''
c = ''' @ @ @ @
@       
@       
@       
 @ @ @ @'''
h = '''@       @
@       @
@ @ @ @ @
@       @
@       @'''
u = '''@       @
@       @
@       @
@       @
 @ @ @ @ '''
#
value = 1
while value == 1:
	x = raw_input('''Input an Arbitrary Order of My Last Name (lin), Press Enter to Continue.
(Note: Must Be 3 Lower-Case Characters):  ''')
	y = raw_input('''Input an Arbitrary Order of My First Name (chun), Press Enter to Continue.
(Note: Must Be 4 Lower-Case Characters):   ''')
	#
	x1 = x[0]
	if x1 == 'l':
		x1 = l.split("\n")
		i1 = 1
	elif x1 == 'i':
		x1 = i.split("\n")
		i1 =  1
	elif x1 == 'n':
		x1 = n.split("\n")
		i1 = 1
	else:
		i1 = 0
	#	
	x2 = x[1]
	if x2 == 'l':
		x2 = l.split("\n")
		i2 = 1
	elif x2 == 'i':
		x2 = i.split("\n")
		i2 = 1
	elif x2 == 'n':
		x2 = n.split("\n")
		i2 = 1
	else:
		i2 = 0
	#
	x3 = x[2]
	if x3 == 'l':
		x3 = l.split("\n")
		i3 = 1
	elif x3 == 'i':
		x3 = i.split("\n")
		i3 = 1
	elif x3 == 'n':
		x3 = n.split("\n")
		i3 = 1
	else:
		i3 = 0
	#
	x4 = y[0]
	if x4 == 'c':
		x4 = c.split("\n")
		i4 = 1
	elif x4 == 'h':
		x4 = h.split("\n")
		i4 =  1
	elif x4 == 'u':
		x4 = u.split("\n")
		i4 = 1
	elif x4 == 'n':
		x4 = n.split("\n")
		i4 = 1
	else:
		i4 = 0
	#
	x5 = y[1]
	if x5 == 'c':
		x5 = c.split("\n")
		i5 = 1
	elif x5 == 'h':
		x5 = h.split("\n")
		i5 =  1
	elif x5 == 'u':
		x5 = u.split("\n")
		i5 = 1
	elif x5 == 'n':
		x5 = n.split("\n")
		i5 = 1
	else:
		i5 = 0
	#
	x6 = y[2]
	if x6 == 'c':
		x6 = c.split("\n")
		i6 = 1
	elif x6 == 'h':
		x6 = h.split("\n")
		i6 =  1
	elif x6 == 'u':
		x6 = u.split("\n")
		i6 = 1
	elif x6 == 'n':
		x6 = n.split("\n")
		i6 = 1
	else:
		i6 = 0
	#
	x7 = y[3]
	if x7 == 'c':
		x7 = c.split("\n")
		i7 = 1
	elif x7 == 'h':
		x7 = h.split("\n")
		i7 =  1
	elif x7 == 'u':
		x7 = u.split("\n")
		i7 = 1
	elif x7 == 'n':
		x7 = n.split("\n")
		i7 = 1
	else:
		i7 = 0
	#
	if (i1 == 1 and i2 == 1 and i3 == 1  and i4 == 1 and i5 == 1 and i6 == 1 and i7 == 1 and len(x) == 3 and len(y) == 4 ):
	 print x1[0],'  ',x2[0],'  ',x3[0],'        ',x4[0],'  ',x5[0],'  ',x6[0],'  ',x7[0]
	 print x1[1],'  ',x2[1],'  ',x3[1],'        ',x4[1],'  ',x5[1],'  ',x6[1],'  ',x7[1]
	 print x1[2],'  ',x2[2],'  ',x3[2],'        ',x4[2],'  ',x5[2],'  ',x6[2],'  ',x7[2]
	 print x1[3],'  ',x2[3],'  ',x3[3],'        ',x4[3],'  ',x5[3],'  ',x6[3],'  ',x7[3]
	 print x1[4],'  ',x2[4],'  ',x3[4],'        ',x4[4],'  ',x5[4],'  ',x6[4],'  ',x7[4]
	 z = raw_input('Do you want to retry Or Move it? yes=y/move=m/no=n: ')
	 if z == 'y':
	 	 value = 1
	 elif z == 'm':
	 	 value1 = 1
	 	 while value1 == 1:
		 	 num1 = 20
		 	 print 'Now, I put the characters on the middle of the nearly 80x25 screen:'
		 	 for i0 in range(10):
		 	 	 if i0 < 11:
		 	 	 	 print ' '
		 	 print ' '*num1,x1[0],'  ',x2[0],'  ',x3[0],'        ',x4[0],'  ',x5[0],'  ',x6[0],'  ',x7[0]
		 	 print ' '*num1,x1[1],'  ',x2[1],'  ',x3[1],'        ',x4[1],'  ',x5[1],'  ',x6[1],'  ',x7[1]
		 	 print ' '*num1,x1[2],'  ',x2[2],'  ',x3[2],'        ',x4[2],'  ',x5[2],'  ',x6[2],'  ',x7[2]
		 	 print ' '*num1,x1[3],'  ',x2[3],'  ',x3[3],'        ',x4[3],'  ',x5[3],'  ',x6[3],'  ',x7[3]
		 	 print ' '*num1,x1[4],'  ',x2[4],'  ',x3[4],'        ',x4[4],'  ',x5[4],'  ',x6[4],'  ',x7[4]
		 	 for i00 in range(10):
		 	 	 if i00 < 11:
		 	 	 	 print ' '
		 	 k3 = 1
		 	 k4 = 0
		 	 k5 = 0
		 	 while k3 == 1:
			 	 k1 = raw_input('What direction do you want to move? left=l/right=r/up=u/down=d: ')
			 	 num = input('How many characters/lines do you want to move?(Characters From 0-20 and Lines From 0-10) : ')
			 	 if k1 == 'l':
			 	 	 num1 = 20-num
			 	 	 k3 = 0
			 	 elif k1 == 'r':
			 	 	 num1 = 20+num
			 	 	 k3 = 0
			 	 elif k1 == 'u':
			 	 	 k4 = num
			 	 	 k3 = 0
			 	 elif k1 == 'd':
			 	 	 k5 = num
			 	 	 k3 = 0
			 	 else:
			 	 	 print 'Wrong Format'
			 	 	 
		 	 for i0 in range(10-k4+k5):
		 	 	 if i0 < 11-k4+k5:
		 	 	 	 print ' '
		 	 print ' '*num1,x1[0],'  ',x2[0],'  ',x3[0],'        ',x4[0],'  ',x5[0],'  ',x6[0],'  ',x7[0]
		 	 print ' '*num1,x1[1],'  ',x2[1],'  ',x3[1],'        ',x4[1],'  ',x5[1],'  ',x6[1],'  ',x7[1]
		 	 print ' '*num1,x1[2],'  ',x2[2],'  ',x3[2],'        ',x4[2],'  ',x5[2],'  ',x6[2],'  ',x7[2]
		 	 print ' '*num1,x1[3],'  ',x2[3],'  ',x3[3],'        ',x4[3],'  ',x5[3],'  ',x6[3],'  ',x7[3]
		 	 print ' '*num1,x1[4],'  ',x2[4],'  ',x3[4],'        ',x4[4],'  ',x5[4],'  ',x6[4],'  ',x7[4]
		 	 for i00 in range(10-k5+k4):
		 	 	 if i00 < 11-k5+k4:
		 	 	 	 print ' '
		 	 k2 = raw_input('Do you want to Retry or Go Back it? yes=y/goback=g/no=n: ')
		 	 if k2 == 'n':
		 	 	 value1 = 0
		 	 	 value = 0
		 	 elif k2 == 'g':
		 	 	 value1 = 0
	 else:
	 	 value = 0
	 
	else:
		print x,y, 'Does Not Include in the Arbitrary Orders of My Name'
		value = 0
		z = raw_input('Do you want to retry? yes=y/no=n: ')
		if z == 'y':
			value = 1
