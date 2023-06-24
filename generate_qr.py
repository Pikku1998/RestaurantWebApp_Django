import qrcode

url = 'http://127.0.0.1:8000/'  # Pass your website address here.
image = qrcode.make(url)
image.save('menu_qr_code.png')
