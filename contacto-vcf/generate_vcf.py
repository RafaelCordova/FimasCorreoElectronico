import qrcode
from PIL import Image

BASE_URL = "https://gestionayaprende.com/contacto"

# Export photo as JPEG
img = Image.open("fotoPerfil.jpeg").convert("RGB")
img.thumbnail((400, 400), Image.LANCZOS)
img.save("jorge.jpg", format="JPEG", quality=85)

vcard = (
    "BEGIN:VCARD\r\n"
    "VERSION:3.0\r\n"
    "FN:Jorge Luis Collazos Martínez\r\n"
    "N:Collazos Martínez;Jorge Luis;;;\r\n"
    "ORG:Gestiona y Aprende SAC\r\n"
    "TITLE:Jefe de Tecnologías de la Información\r\n"
    "TEL;TYPE=CELL:+51983593020\r\n"
    "EMAIL:jcollazos@gestionayaprende.com\r\n"
    "URL:https://gestionayaprende.com/\r\n"
    "X-SOCIALPROFILE;type=linkedin:https://www.linkedin.com/in/jorgecollaz/\r\n"
    f"PHOTO;VALUE=URI:{BASE_URL}/jorge.jpg\r\n"
    "END:VCARD"
)

with open("jorge.vcf", "w", encoding="utf-8") as f:
    f.write(vcard)

print(f"VCF generado: jorge.vcf ({len(vcard):,} bytes)")
print(f"Foto generada: jorge.jpg")

url = f"{BASE_URL}/jorge.vcf"

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="#1a1a2e", back_color="white").convert("RGBA")
qr_size = qr_img.size[0]

logo = Image.open("../assets/logo.png").convert("RGBA")
logo_max = int(qr_size * 0.28)
logo.thumbnail((logo_max, logo_max), Image.LANCZOS)
logo_w, logo_h = logo.size

padding = 16
bg = Image.new("RGBA", (logo_w + padding * 2, logo_h + padding * 2), (255, 255, 255, 255))
qr_img.paste(bg, ((qr_size - bg.width) // 2, (qr_size - bg.height) // 2), bg)
qr_img.paste(logo, ((qr_size - logo_w) // 2, (qr_size - logo_h) // 2), logo)

qr_img.convert("RGB").save("qr_contacto.png", dpi=(300, 300))
print(f"QR generado: qr_contacto.png → {url}")
