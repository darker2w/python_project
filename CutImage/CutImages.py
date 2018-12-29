import Image
import string
import os

def CutImage(handler, rect, bRotate, fileName):	
	region=handler.crop(rect)
	if bRotate:
		region = region.rotate(-90)
	
	w,h = region.size
	#region = region.resize((w/2,h/2))
	region = region.convert('RGBA') 
	region.save(fileName)


filename = ''
def parse(pathtxt, pathpng, savepath):
	f = open('./1.txt','r')
	imgs = Image.open('./1.png')
	imgs=imgs.convert('RGBA') 
	line = f.readline()
	global x
	global y
	global w
	global h
	global ox
	global oy
	global bRotate
	curLine = 0
	
	while line:
		curLine = curLine + 1
		#print line,
		if curLine == 1:
			filename = line.replace('\n','')
			# print filename
		
		if curLine == 2:
			if line.find('false') > -1:
				bRotate = False

			if line.find('true') > -1:
				bRotate = True
		if curLine == 3:

			#position
			tem1 = line.replace(' ','')
			tem1 = tem1.replace('\n','')
			set00 = tem1.split(':')
			set11 = set00[1].split(',')
			x = set11[0]
			y = set11[1]
			# print x
			# print y

		if curLine == 4:
			#size
			tem2 = line.replace(' ','')
			tem2 = tem2.replace('\n','')
			set0 = tem2.split(':')
			set1 = set0[1].split(',')
			w = set1[0]
			h = set1[1]
			# print w
			# print h

		if curLine == 6:
			tem3 = line.replace(' ','')
			tem3 = tem3.replace('\n','')
			set0 = tem3.split(':')
			set1 = set0[1].split(',')
			ox = set1[0]
			oy = set1[1]
			# print ox
			# print oy
		
		

		if curLine == 7:
			if bRotate:
				t = h
				h =w
				w = t
			x0 = int(x)
			y0 = int(y)
			w0 = int(x0)+int(w)
			h0 = int(y0)+int(h)
			
			rect = (x0,y0,w0,h0)
			print rect
			if bRotate:
				CutImage(imgs, rect,True,'./cut/'+filename+'.png')
			else:
				CutImage(imgs, rect,False,'./cut/'+filename+'.png')
			
			curLine = 0
		
		line = f.readline()

# for i in range(9):
# 	txtpath = "./Effect/"+str((i+1))+".txt"
# 	pngpath = "./Effect/"+str((i+1))+".png"
# 	os.makedirs("./cut/"+str((i+1)))
# 	parse(txtpath, pngpath, "./cut/"+str((i+1))+'/')

parse('txtpath', 'pngpath', "")
