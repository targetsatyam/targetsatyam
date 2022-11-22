import pyqrcode
import png
link = "https://www.freecodecamp.org/news/python-tuple-vs-list-what-is-the-difference/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram2.png", scale=5)