import cv2  # Import OpenCV for image processing
from pyzbar.pyzbar import decode  # Import Pyzbar for QR code decoding
import matplotlib.pyplot as plt  # Import Matplotlib for displaying images

# Load and display the image containing QR codes
img = cv2.imread('QRcode.PNG')  # Load the image file
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR (OpenCV format) to RGB and display
plt.axis('off')  # Disable axis
plt.show()  # Display the image

# Convert the image to grayscale for QR code detection
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Decode the QR codes in the grayscale image
decoded_qr_codes = decode(gray_img)

# Loop through the detected QR codes and annotate the image
for code in decoded_qr_codes:
    x, y, w, h = code.rect  # Get bounding box coordinates
    # Draw a rectangle around the QR code
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Annotate the image with the decoded QR code data
    cv2.putText(img, code.data.decode("utf-8"), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Display the annotated image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB and display
plt.axis('off')  # Disable axis
plt.show()  # Show the annotated image
