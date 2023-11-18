import cv2
import glob
import os

# Correct path to the license plates folder
path_for_license_plates = os.path.join(os.getcwd(), "license-plates/**/*.jpg")
list_license_plates = []

for path_to_license_plate in glob.glob(path_for_license_plates, recursive=True):
    license_plate_file = os.path.basename(path_to_license_plate)
    license_plate, _ = os.path.splitext(license_plate_file)
    list_license_plates.append(license_plate)

print("Actual License Plates:")
print("----------------------")

for plate in list_license_plates:
    print(plate)
