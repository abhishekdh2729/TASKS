import cv2
import numpy as np

def analyze_brightness_contrast(image_path):
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Error: Image not found or invalid path.")
        return

    # Computing statistics for brightness and constract
    mean_brightness = np.mean(img)
    std_contrast = np.std(img)

    print("Analysing The Report:")
    print(f"Average Brightness (0-255): {mean_brightness:.2f}")
    print(f"Contrast (Std Dev): {std_contrast:.2f}")

    # Here we are checking the brightness of an image
    if mean_brightness < 50:
        print("The image is likely too dark (underexposed).")
    elif mean_brightness > 200:
        print("The image is likely too bright (overexposed).")
    else:
        print("Brightness is within a normal range.")

    # Here we are checking the constrast of an image
    if std_contrast < 30:
        print("The image may have low contrast.")
    elif std_contrast > 100:
        print("The image has very high contrast (may be harsh).")
    else:
        print("Contrast is within a normal range.")

if __name__ == "__main__":
    # here we can change the image(if it is in this directory, directly we can give name of the img)
    analyze_brightness_contrast("dark_img.jpg")
