import os
import PIL.Image as Image

# Custom Setting
folderName = '_vPic_'
outputFile = './resources/assets/minecraft/textures/items/sword.png'

if __name__ == '__main__':
	# 参考第一张确定大小
	firstPic = Image.open(f'{folderName}/{os.listdir(folderName)[0]}')
	width, height = firstPic.size
	size     = max(width,height)

	lenght = len(os.listdir(folderName))
	resImg = Image.new('RGBA', (size, lenght*size))
	for i,f in enumerate(os.listdir(folderName)):
		print(f'{i}/{lenght}')
		tmpImg = Image.open(f'{folderName}/{f}')
		resImg.paste(tmpImg, (0, i*size, 0+width, i*size+height))
	
	resImg.save(outputFile)
