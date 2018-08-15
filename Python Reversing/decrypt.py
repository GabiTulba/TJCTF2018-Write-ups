import numpy as np

enc='1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101'
flag= ''

def encrypt(flag):
	np.random.seed(12345)
	arr = np.array([ord(c) for c in flag])
	other = np.random.randint(1,5,len(arr))
	arr = np.multiply(arr,other)
	b = [x for x in arr]
	lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
	c = [b[i]^lmao[i] for i,j in enumerate(b)]
	y=(''.join(bin(x)[2:].zfill(8) for x in c))
	p=0
	while(p<len(y) and enc[p]==y[p]):
		p+=1
	return p
L=0
while(L<len(enc)):
	for j in range(256):
		if(L<=encrypt(flag+chr(j))-8):
			flag+=chr(j)
			L=encrypt(flag)
			print L
			break
print flag
