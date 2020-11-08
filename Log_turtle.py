Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Turtle()
>>> .shape ('turtle')
SyntaxError: invalid syntax
>>> tao.shape('turtle')
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)

	
>>> range (4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in [10,50,90]:
	print(i)

	
10
50
90
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)
	print('No.', i)

	
No. 0
No. 1
No. 2
No. 3
>>> tao.reset()
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('NO.',i)

	
NO. 0
NO. 1
NO. 2
NO. 3
NO. 4
NO. 5
NO. 6
NO. 7
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('i8 เหลี่ยมรูปที่',i)

	
i8 เหลี่ยมรูปที่ 0
i8 เหลี่ยมรูปที่ 1
i8 เหลี่ยมรูปที่ 2
i8 เหลี่ยมรูปที่ 3
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('i8 เหลี่ยมรูปที่',i)
	tao.left(90)

	
i8 เหลี่ยมรูปที่ 0
i8 เหลี่ยมรูปที่ 1
i8 เหลี่ยมรูปที่ 2
i8 เหลี่ยมรูปที่ 3
>>> tao.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x000002925348ECA0>>
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('i8 เหลี่ยมรูปที่',i)
	tao.left(180)

	
i8 เหลี่ยมรูปที่ 0
i8 เหลี่ยมรูปที่ 1
i8 เหลี่ยมรูปที่ 2
i8 เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('i8 เหลี่ยมรูปที่',i)
	tao.left(135)

	
i8 เหลี่ยมรูปที่ 0
i8 เหลี่ยมรูปที่ 1
i8 เหลี่ยมรูปที่ 2
i8 เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('i8 เหลี่ยมรูปที่',i)
	tao.left(36)

	
i8 เหลี่ยมรูปที่ 0
i8 เหลี่ยมรูปที่ 1
i8 เหลี่ยมรูปที่ 2
i8 เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(10):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('i8 เหลี่ยมรูปที่',i)
	tao.left(36)

	
i8 เหลี่ยมรูปที่ 0
i8 เหลี่ยมรูปที่ 1
i8 เหลี่ยมรูปที่ 2
i8 เหลี่ยมรูปที่ 3
i8 เหลี่ยมรูปที่ 4
i8 เหลี่ยมรูปที่ 5
i8 เหลี่ยมรูปที่ 6
i8 เหลี่ยมรูปที่ 7
i8 เหลี่ยมรูปที่ 8
i8 เหลี่ยมรูปที่ 9
>>> tao.reset()
>>> def regtangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
>>> retangle()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    retangle()
NameError: name 'retangle' is not defined
>>> regtangle
<function regtangle at 0x0000029253475B80>
>>> regtangle()
>>> for i in range(10):
	regtangle()
	tao.left(36)

	
>>> 