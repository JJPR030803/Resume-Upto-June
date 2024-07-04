from PIL import Image
cat = Image.open('gatooo.png')
width,height = cat.size
quarter = cat.resize((int(width/2),int(height/2)))
quarter.save('quarter.png')