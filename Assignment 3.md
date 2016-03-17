#在屏幕上展示字符组成的字母

**摘要：**本文用简单的python语句，以自己的名字为例，在屏幕上打出自己名字的字符组成的字母，并同样支持显示名字的任意组合，最后实现名字在屏幕上的移动。

**背景介绍：**作为python语言学习入门，掌握一些基本的语句以及语法结构对今后的学习至关重要。
本文作为一个练习性作业，以自己的名字大写拼音为例，运用一些基本的语句和语法，实现在在键盘上输入任意组合的名字，均能显示出对应次序的用@字符组成的大写字母组合，并实现在一定范围内的手动移动。完整python脚本为本目录下MyName.py，本文仅就其中一些代码做一些说明。


**正文：**

一、 首先是创建名字字母的字符画，如：L

        l = '''
        @      
        @      
        @      
        @      
        @ @ @ @'''

二、 创建一个while循环，实现重复演示，然后捕捉键盘输入名字的任意次序，如：

        value = 1
        while value == 1:
        x = raw_input('''Input an Arbitrary Order of My Last Name (lin), Press Enter to Continue.
        (Note: Must Be 3 Lower-Case Characters):  ''')

三、 对最后print出来的字符画的做定义，将需要print的位置Xi(i=1...7)存为一个数组，取自之前定义的字母的字符画的每一行，in(n=1...7)用于后续做判断，如：

        x1 = x[0]
        if x1 == 'l':
            x1 = l.split("\n")
            i1 = 1


四、 打印出输入的任意次序的名字字母组合，取出

        if (i == 1 and len(x) == 3 and len(y) == 4 ):

        print x1[0],'  ',x2[0],'  ',x3[0],'        ',x4[0],'  ',x5[0],'  ',x6[0],'  ',x7[0]

        print x1[1],'  ',x2[1],'  ',x3[1],'        ',x4[1],'  ',x5[1],'  ',x6[1],'  ',x7[1]

        print x1[2],'  ',x2[2],'  ',x3[2],'        ',x4[2],'  ',x5[2],'  ',x6[2],'  ',x7[2]

        print x1[3],'  ',x2[3],'  ',x3[3],'        ',x4[3],'  ',x5[3],'  ',x6[3],'  ',x7[3]

        print x1[4],'  ',x2[4],'  ',x3[4],'        ',x4[4],'  ',x5[4],'  ',x6[4],'  ',x7[4]

        z = raw_input('Do you want to retry Or Move it? yes=y/move=m/no=n: ')

五、 下面是对字符集的移动，首先在屏幕中央print出一个字符画
            
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
六、输入想移动的方向和步长：

        k1 = raw_input('What direction do you want to move? 
                        left=l/right=r/up=u/down=d: ')
        num = input('How many characters/lines do you want to move?
                            (Characters From 0-20 and Lines From 0-10) : ')
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
七、移动字符集：

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
