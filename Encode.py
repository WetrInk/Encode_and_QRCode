#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
sys.path.append("python-qrcode-master\\qrcode\\__init__.py")

import hashlib
import base64
import qrcode
from PIL import Image

#pip install qrcode[pil]

def SHA256_EN(s):
	"""encode string in SHA256 with hashlib module."""
	EN = hashlib.sha256()
	EN.update(s.encode('utf-8'))
	print('SHA256: ')
	print(EN.hexdigest())

def BASE64_DE(s):
	"""decode string in BASE64."""
	DE = base64.b64decode(s.encode('utf-8'))
	print('Decoded as: ')
	print(str(DE, 'utf-8'))

def BASE64_EN(s):
	"""encode string in BASE64, with build-in base64 module."""
	EN = base64.b64encode(s.encode('utf-8'))
	print('BASE64: ')
	print(str(EN, 'utf-8'))

def QRCode_EN(s):
	"""encode string to a QRcode.
	   with module 'qrcode 6.0' from : https://pypi.org/project/qrcode/ """
	img = qrcode.make(s)
	print('Generating the image in default parameters...')
	print('And this QR Code will be saved in current path.')
	print('The image will be loaded with your default image application...')
	img.save("QRCode.png")
	img = Image.open("QRCode.png")
	img.show()

print("""
	This program providing three functions:
		1. Encoding your given string in SHA256.
		2. Decoding your given string in base64.
		3. Encoding your given string in base64.
		4. To generate a QRCode of your given string.
		
	(choose from: 1 / 2 / 3 / 4 )""")

choice = input("> ")

print("And your string.")
s = input("> ")

if choice == '1':
	SHA256_EN(s)
elif choice == '2':
	BASE64_DE(s)
elif choice == '3':
	BASE64_EN(s)
elif choice == '4':
	QRCode_EN(s)
