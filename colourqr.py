import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
    "darkblue_qrcode.png",
    scale=5,
    light="lightblue",
    dark="darkblue",
)