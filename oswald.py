import os
from PIL import ImageColor
from PIL import Image
ss=Image.open('oswald.png')
px=ss.load()
for i in range(0,662):
	for j in range(0,662):
		px[i,j]=(128, 128, 128, 255)
ss.rotate(270)
ss.transpose(Image.FLIP_LEFT_RIGHT).save('oswalds.png')



