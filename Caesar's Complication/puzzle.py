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
