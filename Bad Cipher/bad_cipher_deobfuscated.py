message = ""
key = ""


def encrypt(message,key):
	L=len(key)
	s=[message[i::L] for i in range(L)]
	for i in range(L):
		act=0
		enc=""
		for c in s[i]:
			act=ord(c)^ord(key[i])^(act>>2)
			enc+=chr(act)
		s[i]=enc
	return ''.join( hex(ord(y))[2:] for y in ''.join(''.join(x) for x in zip(*s)))

print encrypt(message,key)
