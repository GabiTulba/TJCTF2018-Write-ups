import os

def Join(path,directory):
	return path+'/'+directory

#decrypt a string
def dec_str(filename):
	f=hex(int(filename)).strip('L')[2:]
	return ''.join(chr(y) for y in [int(f[i:i+2],16) for i in range(0,len(f),2)])

#decrypt a file's contents and name
def dec_file(filename):
	if(filename=='HAHAHA.txt'):
		return
	decfilename=dec_str(filename)
	os.rename(filename,decfilename)

	f=open(decfilename,'r')
	content=f.read()
	f.close()
	deccontent=dec_str(content)
	open(decfilename,'w').write(deccontent)

#decrypt the name of a file and rename it
def dec_filename(filename):
	decfilename=dec_str(filename)
	os.rename(filename,decfilename)	

#DFS for decrypting everyting in a directory
def DFS(path):
	father=os.getcwd()
	os.chdir(path)

	l=os.listdir(os.getcwd())
	for name in l:
		if os.path.isdir(Join(path,name)):
			dec_filename(name)
			DFS(Join(path,dec_str(name)))
		else:
			dec_file(name)
	
	os.chdir(father)

for y in os.listdir(os.getcwd()):
	if(os.path.isdir(Join(os.getcwd(),y))):
		DFS(Join(os.getcwd(),y))
		os.rename(y,'Decrypted')
