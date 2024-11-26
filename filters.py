
import cv2
import numpy as np

def apply_filters(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read image. Check the file path.")
        return

    # Display the original image
    cv2.imshow("Original Image", image)

    # Apply grayscale filter
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imshow("Gaussian Blur", blurred)

    # Apply Canny Edge Detection
    edges = cv2.Canny(image, 100, 200)
    cv2.imshow("Canny Edge Detection", edges)

    # Apply Sobel Filter
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobel_x, sobel_y)
    sobel = np.uint8(np.absolute(sobel))
    cv2.imshow("Sobel Filter", sobel)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Path to the sample image
    image_path = "images/sample.jpg"

    apply_filters(image_path)
