from PIL import Image


# font-kr
fontSize = 64
imageFile = 61440
im = Image.open("font_kr.png").convert("RGBA")
imageWidth = im.size[0]
imageHeight = im.size[1]

imageCol = imageWidth / 64
imageRow = imageHeight / 64

for z in range(imageRow):
    for y in range(imageCol):
        fileName = "kr/" + '%04x' % imageFile + ".png"
        left = fontSize * y
        upper = fontSize * z
        right = left + 64
        lower = upper + 64
        im.crop((left, upper, right, lower)).save(fileName)
        imageFile = imageFile + 1


# font-cn
fontSize = 64
imageFile = 61440
im = Image.open("font_cn.png").convert("RGBA")
imageWidth = im.size[0]
imageHeight = im.size[1]

imageCol = imageWidth / 64
imageRow = imageHeight / 64

for z in range(imageRow):
    for y in range(imageCol):
        fileName = "jp/" + '%04x' % imageFile + ".png"
        left = fontSize * y
        upper = fontSize * z
        right = left + 64
        lower = upper + 64
        im.crop((left, upper, right, lower)).save(fileName)
        imageFile = imageFile + 1

# font-jp
imageFile = 0
im = Image.open("font_jp.png").convert("RGBA")
imageWidth = im.size[0]
imageHeight = im.size[1]
imageCol = imageWidth / 64
imageRow = imageHeight / 64

for z in range(imageRow):
    for y in range(imageCol):
        if imageFile > 255:
            formatter = '%04x'
        else:
            formatter = '%02x'

        fileName = "jp/" + formatter % imageFile + ".png"
        left = fontSize * y
        upper = fontSize * z
        right = left + 64
        lower = upper + 64
        im.crop((left, upper, right, lower)).save(fileName)
        imageFile = imageFile + 1



