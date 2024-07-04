from PIL import Image

catIm = Image.open('de-donde-vienen-los-gatos.jpg')
#print(catIm.size)
#print(catIm.format)
#print(catIm.format_description)
im = Image.new('RGBA',(100,200),'purple')
im.save('purpleimage.png')
im2 = Image.new('RGBA',(20,20))
im2.save('imagen-transparente.png')
catIm.save('gatooo.png')