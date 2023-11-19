import cv2
import requests
import time
from flask import Flask, Response
import googlesheetsdata

import googlemaps
GOOGLE_MAPS_API_KEY = ''  # Replace with your Google Maps API key
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)



app = Flask(__name__)
camera = cv2.VideoCapture(0)  # Use 0 for the default camera

API_KEY = ''
API_URL = ''
INTERVAL = 5

# Store the last detected plate's position
last_plate = {'x': 0, 'y': 0, 'w': 0, 'h': 0}

# Your JSON data
json_data = [
        {
            "alertId": 9,
            "alertTime": "2023-11-18T10:25:00Z",
            "alertLocation": "Dallas, Texas, United States",
            "alertType": "Missing Person",
            "missingPerson": {
                "name": "William Turner",
                "age": 60,
                "gender": "Male",
                "description": "White hair, blue eyes, height 5'8",
                "lastSeen": "2023-11-18T10:10:00Z",
                "lastSeenLocation": "456 Main Street, Dallas, Texas",
                "clothing": "Brown jacket, jeans"
            },
            "suspectVehicle": {
                "type": "SUV",
                "make": "Jeep",
                "model": "Grand Cherokee",
                "color": "Gray",
                "licensePlate": "CSD5055"
            }
        },
        {
            "alertId": 10,
            "alertTime": "2023-11-18T10:35:00Z",
            "alertLocation": "Phoenix, Arizona, United States",
            "alertType": "Missing Person",
            "missingPerson": {
                "name": "Linda Martinez",
                "age": 45,
                "gender": "Female",
                "description": "Black hair, brown eyes, height 5'6",
                "lastSeen": "2023-11-18T10:20:00Z",
                "lastSeenLocation": "123 Desert Road, Phoenix, Arizona",
                "clothing": "Red blouse, blue jeans"
            },
            "suspectVehicle": {
                "type": "Car",
                "make": "Ford",
                "model": "Escape",
                "color": "Silver",
                "licensePlate": "YZA3456"
            }
        }

]

# Extract license plates from JSON data
license_plates = [entry["suspectVehicle"]["licensePlate"] for entry in json_data]


def gen_frames():
    last_time = time.time() - INTERVAL  # Set initial last_time to current time minus INTERVAL
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            current_time = time.time()
            if current_time - last_time > INTERVAL:
                last_time = current_time

                ret, buffer = cv2.imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()


                response = requests.post(
                    API_URL,
                    files=dict(upload=frame_bytes),
                    headers={'Authorization': f'Token {API_KEY}'}
                )
                plates = response.json()  # Parse response

                # Check if any plates are detected and process
                for result in plates.get('results', []):
                    # Update last_plate coordinates
                    last_plate['x'] = result['box']['xmin']
                    last_plate['y'] = result['box']['ymin']
                    last_plate['w'] = result['box']['xmax'] - result['box']['xmin']
                    last_plate['h'] = result['box']['ymax'] - result['box']['ymin']

                    # Print only the license plate number in uppercase
                    plate_number = result.get('plate', 'N/A').upper()
                    print("Detected Plate:", plate_number)

                    # Check if detected plate is in the list from JSON data
                    if plate_number in license_plates:

                        location = gmaps.geolocate()
                        # print(f"Alert: Match found for plate {plate_number}")
                        lat, lng = location['location']['lat'], location['location']['lng']
                        print(f"Alert: Match found for plate {plate_number} at location {lat}, {lng}")
                        print("Alert: Sending alert to authorities...")
                        print("____")
                        print("Alert details:")
                        print("Alert ID:", json_data[0]["alertId"])
                        print("Alert Time:", json_data[0]["alertTime"])
                        print("Alert Location:", json_data[0]["alertLocation"])
                        print("Alert Type:", json_data[0]["alertType"])
                        print("Missing Person Name:", json_data[0]["missingPerson"]["name"])
                        print("Missing Person Age:", json_data[0]["missingPerson"]["age"])
                        print("Alert: Alert sent!")

                        alert_data = next(
                            (item for item in json_data if item["suspectVehicle"]["licensePlate"] == plate_number),
                            None)
                        sheet_name = "LicensePlateData"
                        credentials_file = ''
                        sheet = googlesheetsdata.initialize_google_sheets(sheet_name, credentials_file)
                        data_to_append = [
                            plate_number,
                            alert_data['alertId'],
                            alert_data['alertTime'],
                            alert_data['alertLocation'],
                            alert_data['missingPerson']['name'],
                            f"{lat}, {lng}"
                        ]
                        googlesheetsdata.append_data_to_sheet(sheet, data_to_append)


            # Draw rectangle around the last detected license plate
            x, y, w, h = last_plate['x'], last_plate['y'], last_plate['w'], last_plate['h']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green color


            # Convert frame to bytes for streaming
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')



@app.route('/')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
