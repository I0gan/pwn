map_ = [0x5F, 0xF2 ,0x5E ,0x8B ,0x4E ,0x0E ,0xA3 ,0xAA ,0xC7 ,0x93 ,0x81 ,0x3D , 0x5F ,0x74 ,0xA3 ,0x09
,0x91 ,0x2B ,0x49 ,0x28 ,0x93 ,0x67 ,0x00 ,0x00  ,0x00 ,0x08 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00]
flag = ''
for i in range(22):
	v_ = i + 1;
	j = 0
	r = 0
	while j < v_:
		j += 1
		r = 0x6D01788D * r + 0x3039;
	flag += chr((map_[i] ^ r) & 0xFF)

print(flag)
