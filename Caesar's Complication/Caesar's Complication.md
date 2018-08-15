# Caesar's Complication (20 points/ 76 solves)
## Problem statement:
> King Julius Caesar was infamous for his [wordsearch]() solving speed.
<br><br>
## My opinion:
Even if the idea of this challenge was pretty straight forward, it was still very frustrating.<br>
<br>
## Understanding the challenge:
First of all,i t was clear from the chall's name that the encryption was a **Caesar cipher** with some arbitrary shift, and also the statement explicitly said that the ciphertext was a **wordsearch**, so to search for the flag we just needed some code to check for the string that starts with`tjctf{` and ends with `}` in all 8 directions for every possible key.<br>
<br>

## The code:
```python
mat=[list(x) for x in open('ciphertext').read().split('\n')]

dirx=[0,1,1,1,0,-1,-1,-1]
diry=[1,1,0,-1,-1,-1,0,1]

def Check(x,y,d):
	s=''
	while(x<len(mat) and y<len(mat[x]) and x>0 and y>0):
		s+=mat[x][y]
		x+=dirx[d]
		y+=diry[d]
		if(s.startswith('tjctf{') and s.endswith('}')):
			print 'Possible flag found:',s
			return

def Search():
	for x in range(len(mat)):
		for y in range(len(mat[x])):
			for d in range(8):
				Check(x,y,d)
def Shift():
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			if(mat[i][j]=='{' or mat[i][j]=='}'):
				continue
			elif(mat[i][j]=='z'):
				mat[i][j]='a'
			else: mat[i][j]=chr(ord(mat[i][j])+1)

for i in range(26):
	print 'Key:',i
	Search()
	Shift()
```

## Finding the flag:
The python code gave the following output:
>Key: 0
>Key: 1
>...
>Key: 8
>Possible flag found: tjctf{idesofmarch}
>Key: 9
>...
>Key: 25
So the flag was very easy to find:
Flag: **tjctf{idesofmarch}**
