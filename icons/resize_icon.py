from PIL import Image
import os
import sys

if len(sys.argv) != 2:
    print("Uso: python3 resize_icon.py <imagen_original>")
    sys.exit(1)

input_path = sys.argv[1]
output_dir = "icons"
output_path = os.path.join(output_dir, "icon-192.png")

try:
    img = Image.open(input_path)
    img = img.resize((192, 192), Image.Resampling.LANCZOS)

    os.makedirs(output_dir, exist_ok=True)
    img.save(output_path)
    print(f"Icono guardado en: {output_path}")
except Exception as e:
    print(f"Error al procesar la imagen: {e}")
