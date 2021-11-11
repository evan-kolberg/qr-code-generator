import pyqrcode
url = "https://github.com/me-like-code"; code = pyqrcode.create(url); code.svg("generated-qr-code.svg", scale=8)