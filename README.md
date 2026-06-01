# Firmas de Correo Electrónico — Gestiona y Aprende

Herramientas para generar firmas de correo y tarjetas de contacto digitales para el equipo de **Gestiona y Aprende SAC**.

## Estructura del proyecto

```
FimasCorreoElectronico/
├── assets/                  # Logos compartidos
│   ├── logo.png             # Ícono (usado en centro del QR)
│   ├── logo-completo.png    # Logo horizontal (usado en firma de correo)
│   └── Logo-05.png          # Variante de logo
│
├── firma-web/               # Generador de firma de correo (web)
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── contacto-vcf/            # Generadores de tarjetas de contacto (Python)
    ├── generate_all.py      # Genera VCF + QR para todo el equipo
    ├── generate_vcf.py      # Genera VCF + QR para Jorge (individual)
    └── generate_qr.py       # Genera QR a partir del vCard en texto plano
```

## Firma de correo electrónico

App web que genera una imagen PNG lista para usar como firma en Gmail u otros clientes de correo.

**Cómo usar:**

1. Abre `firma-web/index.html` en el navegador (doble clic o servidor local).
2. Ingresa nombre completo, cargo y teléfono celular.
3. Haz clic en **Exportar PNG** para descargar `firma_gya.png`.
4. En Gmail: Ajustes → Ver todos los ajustes → Firma → insertar imagen.

> El teléfono fijo corporativo (`+51 938 372 216`) se agrega automáticamente.

## Tarjetas de contacto (VCF + QR)

Scripts Python que generan archivos `.vcf` (vCard) y códigos QR con el logo al centro para compartir contactos digitalmente.

**Requisitos:**

```bash
pip install qrcode[pil] Pillow
```

**Generar tarjetas para todo el equipo:**

```bash
cd contacto-vcf
python generate_all.py
```

Coloca las fotos de perfil (`.webp`) en la carpeta `contacto-vcf/` antes de ejecutar.  
Sube los archivos `.vcf` y `.jpg` generados a `https://gestionayaprende.com/contacto/`.

**Archivos generados por persona:**

| Archivo           | Descripción                         |
|-------------------|-------------------------------------|
| `{id}.vcf`        | Tarjeta de contacto vCard 3.0       |
| `{id}.jpg`        | Foto de perfil optimizada (400×400) |
| `qr_{id}.png`     | QR a 300 dpi con logo al centro     |

## Datos corporativos

| Campo      | Valor                                     |
|------------|-------------------------------------------|
| Empresa    | Gestiona y Aprende SAC                    |
| Web        | www.gestionayaprende.com                  |
| Dirección  | Av. República de Colombia Nro. 671, Dpto. 502, San Isidro, Lima, Perú |
| Teléfono fijo | +51 938 372 216                        |
