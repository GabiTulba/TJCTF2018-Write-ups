message = open('flag.enc').read().strip('\n')

def transform(msg):
	out=''
	for i in range(0,len(msg),2):
		out+=chr(int(msg[i:i+2],16))
	return out

def decrypt(msg,l):
	flag='tjctf{m4'
	key=[]
	for i in range(len(flag)):
		key.append(chr(ord(msg[i])^ord(flag[i])))
	keylen=len(key)
	dec=''
	act=[0 for i in range(keylen)]
	for i in range(len(msg)):
		if(i>=keylen):
			act[i%keylen]=ord(msg[i])^ord(key[i%keylen])^(ord(msg[i-keylen])>>2)
		else:
			act[i]=ord(msg[i])^ord(key[i])
		dec+=chr(act[i%keylen])
	print dec
	

print 'Msg Len:',len(transform(message))

decrypt(transform(message),8)
