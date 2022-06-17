import qrcode

request = input('Send me link: ')
request_name = input('Send me name for your qr code: ')

data = f'qr_codes/{request_name}.png'

img = qrcode.make(request)

img.save(data)

# img.show()
