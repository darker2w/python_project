# import Image
from PIL import Image
import string
import os
import json

def CutImage(handler, rect, bRotate, fileName):	
	region=handler.crop(rect)
	if bRotate:
		region = region.rotate(-90)
	
	w,h = region.size
	#region = region.resize((w/2,h/2))
	region = region.convert('RGBA') 
	region.save(fileName)


def CutImageByJson(jsonStr, savePath):
	global jsonObj
	if len(jsonStr) < 2 or len(savePath) < 0:
		print 'json or savePath error'
		return

	jsonObj = json.loads(jsonStr)
	imgs = Image.open('./1.png')
	# imgs = imgs.convert('RGBA')
	obj = jsonObj['frames']
	for key in obj:
		value = obj[key]
		print ('key:%s value:%s\n'%(key, value))
		
		x0 = int(value['frame']['x'])
		y0 = int(value['frame']['y'])
		w0 = int(x0)+int(value['frame']['w'])
		h0 = int(y0)+int(value['frame']['h'])
		rect = (x0,y0,w0,h0)
		CutImage(imgs, rect, value['rotated'], savePath+'/'+key)



def _main_():
	f = open('./1.txt','r')
	jsonStr = f.read()

	isExists=os.path.exists('./save')
	if not isExists:
		os.makedirs('./save') 
	
	CutImageByJson(jsonStr, './save')

_main_()