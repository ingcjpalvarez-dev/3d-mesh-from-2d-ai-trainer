import cv2
import numpy as np

# Crear imagen negra 512x512
img = np.zeros((512, 512), dtype=np.uint8)

# Dibujar caja blanca (máscara)
cv2.rectangle(img, (100, 100), (400, 400), 255, -1)

# Guardar máscara
cv2.imwrite("images/box_mask.png", img)

# Crear versión RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img_rgb[100:400, 100:400] = [0, 120, 255]  # Color naranja

# Guardar RGB
cv2.imwrite("images/box_rgb.png", img_rgb)

print("Imágenes creadas exitosamente")