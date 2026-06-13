import qrcode
url="https://www.tops-int.com/"
qr=qrcode.make(url)
qr.save("tops.png")

'''1. import qrcode

qrcode module import કરે છે.
QR Code બનાવવા માટે ઉપયોગ થાય છે.

2. url="https://www.tops-int.com/"

URL string variable માં store કરે છે.
આ URL QR Code માં encode થશે.

3. qr=qrcode.make(url)

URL પરથી QR Code image બનાવે છે.
qr માં QR image object store થાય છે.

4. qr.save("tops.png")

QR Code ને tops.png નામની image file તરીકે save કરે છે.
File current folder માં save થશે.'''