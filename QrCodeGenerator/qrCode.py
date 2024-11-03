import qrcode as qr

img = qr.make("Some Data is here:")

type(img)

img.save("someData.png")