import base64
import qrcode
from PIL import Image

BASE_URL = "https://gestionayaprende.com/contacto"

def fold_line(header, value, width=75):
    first = f"{header}:{value}"
    if len(first) <= width:
        return first + "\r\n"
    lines = [first[:width]]
    rest = first[width:]
    while rest:
        lines.append(" " + rest[:width - 1])
        rest = rest[width - 1:]
    return "\r\n".join(lines) + "\r\n"

def export_photo_jpeg(src_path, dest_path, max_size=400):
    import io
    img = Image.open(src_path).convert("RGB")
    img.thumbnail((max_size, max_size), Image.LANCZOS)
    img.save(dest_path, format="JPEG", quality=85)

def make_vcf(person):
    photo_url = f"{BASE_URL}/{person['id']}.jpg"
    return (
        "BEGIN:VCARD\r\n"
        "VERSION:3.0\r\n"
        f"FN:{person['nombre']}\r\n"
        f"N:{person['apellidos']};{person['primer_nombre']};;;\r\n"
        f"ORG:{person['empresa']}\r\n"
        f"TITLE:{person['cargo']}\r\n"
        f"TEL;TYPE=CELL:{person['numero']}\r\n"
        f"EMAIL:{person['correo']}\r\n"
        f"URL:{person['web']}\r\n"
        f"X-SOCIALPROFILE;type=linkedin:{person['linkedin']}\r\n"
        f"PHOTO;VALUE=URI:{photo_url}\r\n"
        "END:VCARD"
    )

def make_qr(url, output_path):
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

    qr_img.convert("RGB").save(output_path, dpi=(300, 300))

personas = [
    {
        "id": "daniel",
        "nombre": "Daniel Jesus Ccori",
        "primer_nombre": "Daniel Jesus",
        "apellidos": "Ccori",
        "cargo": "Gerente General",
        "empresa": "Gestiona y Aprende SAC",
        "numero": "+51976076434",
        "correo": "djesus@gestionayaprende.com",
        "web": "https://gestionayaprende.com/",
        "linkedin": "https://www.linkedin.com/in/daniel-jesus-b2309842/",
        "foto": "fotoDaniel.webp",
    },
    {
        "id": "manuel",
        "nombre": "Manuel Santos Montoro",
        "primer_nombre": "Manuel",
        "apellidos": "Santos Montoro",
        "cargo": "Gerente de Línea",
        "empresa": "Gestiona y Aprende SAC",
        "numero": "+51963603052",
        "correo": "msantos@gestionayaprende.com",
        "web": "https://gestionayaprende.com/",
        "linkedin": "https://www.linkedin.com/in/manuel-santos-58a11b48/",
        "foto": "fotoManuel.webp",
    },
    {
        "id": "irene",
        "nombre": "Irene Gutarra Gutarra",
        "primer_nombre": "Irene",
        "apellidos": "Gutarra Gutarra",
        "cargo": "Gerente de Línea",
        "empresa": "Gestiona y Aprende SAC",
        "numero": "+51998740199",
        "correo": "igutarra@gestionayaprende.com",
        "web": "https://gestionayaprende.com/",
        "linkedin": "https://www.linkedin.com/in/irene-gutarra-gutarra-968940b4/",
        "foto": "fotoIrene.webp",
    },
    {
        "id": "ysaac",
        "nombre": "Ysaac Chávez Sánchez",
        "primer_nombre": "Ysaac",
        "apellidos": "Chávez Sánchez",
        "cargo": "Gerente de Línea",
        "empresa": "Gestiona y Aprende SAC",
        "numero": "+51996336250",
        "correo": "ychavez@gestionayaprende.com",
        "web": "https://gestionayaprende.com/",
        "linkedin": "https://www.linkedin.com/in/ysaac-ch%C3%A1vez-s%C3%A1nchez-52426b6a/",
        "foto": "fotoYsaac.webp",
    },
    {
        "id": "jose",
        "nombre": "José Paredes Ventocilla",
        "primer_nombre": "José",
        "apellidos": "Paredes Ventocilla",
        "cargo": "Gerente de Línea",
        "empresa": "Gestiona y Aprende SAC",
        "numero": "+51994041520",
        "correo": "jparedes@gestionayaprende.com",
        "web": "https://gestionayaprende.com/",
        "linkedin": "https://www.linkedin.com/in/joseparedesv/",
        "foto": "fotoJoseA.webp",
    },
    {
        "id": "judith",
        "nombre": "Judith Vásquez Barrientos",
        "primer_nombre": "Judith",
        "apellidos": "Vásquez Barrientos",
        "cargo": "Gerente de Línea",
        "empresa": "Gestiona y Aprende SAC",
        "numero": "+51996040776",
        "correo": "jvasquez@gestionayaprende.com",
        "web": "https://gestionayaprende.com/",
        "linkedin": "https://www.linkedin.com/in/judith-v%C3%A1squez-barrientos-93823191/",
        "foto": "fotoJudith.webp",
    },
]

for p in personas:
    vcf_name = f"{p['id']}.vcf"
    jpg_name = f"{p['id']}.jpg"
    qr_name = f"qr_{p['id']}.png"
    url = f"{BASE_URL}/{vcf_name}"

    export_photo_jpeg(p["foto"], jpg_name)
    vcf_content = make_vcf(p)
    with open(vcf_name, "w", encoding="utf-8") as f:
        f.write(vcf_content)

    make_qr(url, qr_name)
    print(f"[OK] {p['nombre']}: {vcf_name} + {jpg_name} + {qr_name}")

print("\nListo. Sube los .vcf a https://gestionayaprende.com/contacto/")
