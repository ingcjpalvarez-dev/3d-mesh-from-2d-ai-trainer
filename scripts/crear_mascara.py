"""
crear_mascara.py

Generates 2D reference images (binary mask and RGB version) used as input
for the 3D mesh generation pipeline. The mask defines the object's shape
in black and white, while the RGB version adds color context for visual reference.

Author: Carlos Alvarez
"""

import cv2
import numpy as np
import os

# ── Image configuration ──────────────────────────────────────────────────────
IMAGE_WIDTH  = 512
IMAGE_HEIGHT = 512

# Bounding box coordinates for the reference object
BOX_X1, BOX_Y1 = 100, 100
BOX_X2, BOX_Y2 = 400, 400

# Output color for the RGB version (orange in BGR format)
RGB_COLOR = [0, 120, 255]

# Output directory for generated images
OUTPUT_DIR = "images"

# ── Create output directory if it doesn't exist ──────────────────────────────
os.makedirs(OUTPUT_DIR, exist_ok=True)

try:
    # Create a blank black canvas for the binary mask
    mask = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH), dtype=np.uint8)

    # Draw a filled white rectangle representing the reference object
    cv2.rectangle(mask, (BOX_X1, BOX_Y1), (BOX_X2, BOX_Y2), 255, -1)

    # Save the binary mask to disk
    mask_path = os.path.join(OUTPUT_DIR, "box_mask.png")
    cv2.imwrite(mask_path, mask)

    # Convert the mask to a 3-channel BGR image for the RGB version
    img_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # Apply the defined color to the object region
    img_rgb[BOX_Y1:BOX_Y2, BOX_X1:BOX_X2] = RGB_COLOR

    # Save the RGB version to disk
    rgb_path = os.path.join(OUTPUT_DIR, "box_rgb.png")
    cv2.imwrite(rgb_path, img_rgb)

    print(f"Binary mask saved at: {mask_path}")
    print(f"RGB image saved at:   {rgb_path}")
    print("Reference images created successfully.")

except Exception as e:
    print(f"Error while creating images: {e}")