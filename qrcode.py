from turtle import fillcolor
import pyqrcode
import png
from pyqrcode import QRCode

s="www.geeksforgeeks.org"
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
url.png("myqr.png",scale=6)


