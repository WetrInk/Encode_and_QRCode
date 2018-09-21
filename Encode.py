#!/usr/bin/env python

import sys
sys.path.append("python-qrcode-master\\qrcode\\__init__.py")

import hashlib
import base64
import qrcode
from PIL import Image

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
	print('And this QR Code will be saved in current path.\n')
	print('The image will be loaded with your default image application...')
	img.save("QRCode.png")
	img = Image.open("QRCode.png")
	img.show()

#main process begins

print("""
	This program providing three functions:
		1. Encoding your given string in SHA256.
		2. Decoding your given string in base64.
		3. Encoding your given string in base64.
		4. To generate a QRCode of your given string.
		
	(choose from: 1 / 2 / 3 / 4 )""")

choice = input("> ")

while choice not in ['1', '2', '3', '4']:
	print("Plz input a number from 1 to 4.")
	choice = input("> ")

print("And your string, a not-null string.")
s = input("> ")

while not s:
	print("You should input something.")
	s = input("> ")

try:
	if choice == '1':
		print("You chose SHA256 Encoding.\n")
		SHA256_EN(s)
	elif choice == '2':
		print("You chose BASE64 Decoding.\n")
		BASE64_DE(s)
	elif choice == '3':
		print("You chose BASE64 Encoding.\n")
		BASE64_EN(s)
	elif choice == '4':
		print("You chose to generate a QR code.\n")
		QRCode_EN(s)

except EOFError:
	print("Terminated by input. Bye!")
	# this part seems doesn't work.

except:
	print("Plz input a appropriate string, esp. when you hope your BASE64 string to be rightly decoded.")
	print("Let's try again to get your STRING, or just input ctl-z to exit.")
	s = input("> ")
	
finally:
	print("\nSeems it worked well. Bye!")
