import os
import shutil
import cv2
import numpy as np
from paddleocr import PaddleOCR


# Function to correct image rotation
def correct_rotation(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

    if lines is not None:
        angle = np.median([np.rad2deg(line[0][1]) - 90 for line in lines])  # Compute median angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated
    return image  # Return original if no rotation detected


# Initialize OCR with angle classification
ocr = PaddleOCR(use_angle_cls=True)

# Define paths
photos_dir = "photos"
renamed_dir = "renamed"
os.makedirs(renamed_dir, exist_ok=True)

# Track existing filenames to avoid duplicates
file_counts = {}

# Process each image
for filename in os.listdir(photos_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  # Check for image files
        image_path = os.path.join(photos_dir, filename)

        # Correct rotation
        fixed_image = correct_rotation(image_path)
        corrected_path = os.path.join(photos_dir, "corrected_" + filename)
        cv2.imwrite(corrected_path, fixed_image)  # Save the corrected image

        result = ocr.ocr(corrected_path)

        if result and result[0]:
            label = result[0][0][1][0]  # Extract text label
            label = label.replace(" ", "_")  # Replace spaces with underscores
            label = label.replace("/", "_")  # Replace forward slashes with underscores

            # Handle duplicate filenames
            if label in file_counts:
                file_counts[label] += 1
                new_filename = f"{label}_{file_counts[label]}.JPG"
            else:
                file_counts[label] = 1
                new_filename = f"{label}.JPG"

            # Copy and rename file
            new_path = os.path.join(renamed_dir, new_filename)
            shutil.copy(image_path, new_path)
            print(f"Renamed {filename} -> {new_filename}")

print("Processing complete.")
