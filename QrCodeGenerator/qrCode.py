import qrcode as qr

img = qr.make("Some Data is here:")

# type(img) #just type checking

img.save("someData.png")