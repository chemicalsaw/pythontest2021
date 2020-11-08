Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['toyota','honda','izusu']
>>> garage.append('suzui')
>>> print(garage)
['toyota', 'honda', 'izusu', 'suzui']
>>> print(garage[2])
izusu
>>> garage.remove('honda')
>>> print(garage)
['toyota', 'izusu', 'suzui']
>>> garage.insert(1,'benz')
>>> print(garage)
['toyota', 'benz', 'izusu', 'suzui']
>>> del garage[2]
>>> print(garage)
['toyota', 'benz', 'suzui']
>>> print(garage[-1])
suzui
>>> printe(garage[-2])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    printe(garage[-2])
NameError: name 'printe' is not defined
>>> print(garage[-2])
benz
>>> print(garage)
['toyota', 'benz', 'suzui']
>>> mycar = garage.pop(-1)
>>> print(mycar)
suzui
>>> print(garage)
['toyota', 'benz']
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> garage[1] = 'tesla'
>>> print(garage)
['toyota', 'tesla', 'suzuki']
>>> print (len(garage))
3
>>> user = ['z','r','t','b','n','p'p]
SyntaxError: invalid syntax
>>> user = ['z','r','t','b','n','p']
>>> user.sort()
>>> print(user)
['b', 'n', 'p', 'r', 't', 'z']
>>> users.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    users.sort(reverse=True)
NameError: name 'users' is not defined
>>> user.sort(reverse=True)
>>> user
['z', 't', 'r', 'p', 'n', 'b']
>>> print(sortes(user))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(sortes(user))
NameError: name 'sortes' is not defined
>>> print(sorted(user))
['b', 'n', 'p', 'r', 't', 'z']
>>> print(user)
['z', 't', 'r', 'p', 'n', 'b']
>>> user = ['z','r','t','b','n','p']
>>> user.reverse()
>>> print(user)
['p', 'n', 'b', 't', 'r', 'z']
>>> for u in user:
	print(u)

	
p
n
b
t
r
z
>>> for u in sorted(user):
	print(u)

	
b
n
p
r
t
z
>>> for u in user.reverse():
        print(u)
        

user.reverse()
for u in user:
	print(u)




	print(u)