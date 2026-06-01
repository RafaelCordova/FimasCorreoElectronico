import qrcode
from PIL import Image

vcard = (
    "BEGIN:VCARD\n"
    "VERSION:3.0\n"
    "FN:Jorge Luis Collazos Martínez\n"
    "N:Collazos Martínez;Jorge Luis;;;\n"
    "ORG:Gestiona y Aprende SAC\n"
    "TITLE:Jefe de Tecnologías de la Información\n"
    "TEL;TYPE=CELL:+51983593020\n"
    "EMAIL:jcollazos@gestionayaprende.com\n"
    "URL:https://gestionayaprende.com/\n"
    "X-SOCIALPROFILE;type=linkedin:https://www.linkedin.com/in/jorgecollaz/\n"
    "END:VCARD"
)

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)
qr.add_data(vcard)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="#1a1a2e", back_color="white").convert("RGBA")
qr_size = qr_img.size[0]

logo = Image.open("../assets/logo.png").convert("RGBA")

# Logo ocupará ~28% del QR
logo_max = int(qr_size * 0.28)
logo.thumbnail((logo_max, logo_max), Image.LANCZOS)
logo_w, logo_h = logo.size

# Fondo blanco redondeado detrás del logo para legibilidad
padding = 16
bg_w = logo_w + padding * 2
bg_h = logo_h + padding * 2
bg = Image.new("RGBA", (bg_w, bg_h), (255, 255, 255, 255))

# Pegar fondo centrado
pos_bg = ((qr_size - bg_w) // 2, (qr_size - bg_h) // 2)
qr_img.paste(bg, pos_bg, bg)

# Pegar logo encima
pos_logo = ((qr_size - logo_w) // 2, (qr_size - logo_h) // 2)
qr_img.paste(logo, pos_logo, logo)

out = qr_img.convert("RGB")
out.save("qr_contacto.png", dpi=(300, 300))
print(f"QR generado: qr_contacto.png ({qr_size}x{qr_size}px)")
