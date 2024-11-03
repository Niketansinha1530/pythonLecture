import qrcode
from PIL import Image
import qrcode.constants


qr = qrcode.QRCode(
    version=1,
    error_correction= qrcode.constants.ERROR_CORRECT_H,
    box_size= 23,
    border=1,
)

qr.add_data("https://www.w3schools.com/python/python_strings.asp")
qr.make(fit=True)
img=qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
img.save("W3School.png")