import qrcode

url = "https://github.com/mk-babian/python-2142.32"
img = qrcode.make(url)

img.save("qrcode.png")
