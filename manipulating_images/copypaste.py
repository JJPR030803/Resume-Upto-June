from PIL import Image

catIm = Image.open('gatooo.png')
catCopy = catIm.copy()

faceIm = catIm.crop((200,200,400,400))
catCopy.paste(faceIm,(0,0))
catCopy.paste(faceIm,(400,500))
catCopy.save('pasted.png')
print(faceIm.size)