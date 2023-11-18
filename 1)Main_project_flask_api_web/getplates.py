import json

# Your JSON data (replace this with the actual JSON data)
json_data = [
    {
        "alertId": 1,
        "alertTime": "2023-11-18T09:05:00Z",
        "alertLocation": "Austin, Texas, United States",
        "alertType": "Missing Person",
        "missingPerson": {
            "name": "John Smith",
            "age": 25,
            "gender": "Male",
            "description": "Blonde hair, blue eyes, height 6'0",
            "lastSeen": "2023-11-18T08:30:00Z",
            "lastSeenLocation": "123 Oak Street, Austin, Texas",
            "clothing": "Red shirt, khaki pants"
        },
        "suspectVehicle": {
            "type": "Truck",
            "make": "Ford",
            "model": "F-150",
            "color": "White",
            "licensePlate": "XYZ9876"
        }
    },
    {
        "alertId": 2,
        "alertTime": "2023-11-18T09:15:00Z",
        "alertLocation": "Los Angeles, California, United States",
        "alertType": "Missing Person",
        "missingPerson": {
            "name": "Sarah Johnson",
            "age": 30,
            "gender": "Female",
            "description": "Black hair, brown eyes, height 5'8",
            "lastSeen": "2023-11-18T09:00:00Z",
            "lastSeenLocation": "789 Maple Avenue, Los Angeles, California",
            "clothing": "Blue dress, white shoes"
        },
        "suspectVehicle": {
            "type": "Car",
            "make": "Toyota",
            "model": "Camry",
            "color": "Silver",
            "licensePlate": "ABC1234"
        }
    },
    {
        "alertId": 3,
        "alertTime": "2023-11-18T09:25:00Z",
        "alertLocation": "New York City, New York, United States",
        "alertType": "Missing Person",
        "missingPerson": {
            "name": "Michael Brown",
            "age": 40,
            "gender": "Male",
            "description": "Brown hair, green eyes, height 5'10",
            "lastSeen": "2023-11-18T09:10:00Z",
            "lastSeenLocation": "456 Broadway, New York City, New York",
            "clothing": "Gray suit, black tie"
        },
        "suspectVehicle": {
            "type": "Van",
            "make": "Chevrolet",
            "model": "Express",
            "color": "Black",
            "licensePlate": "DEF5678"
        }
    },
    {
        "alertId": 4,
        "alertTime": "2023-11-18T09:35:00Z",
        "alertLocation": "Chicago, Illinois, United States",
        "alertType": "Missing Person",
        "missingPerson": {
            "name": "Emily Davis",
            "age": 22,
            "gender": "Female",
            "description": "Red hair, hazel eyes, height 5'6",
            "lastSeen": "2023-11-18T09:20:00Z",
            "lastSeenLocation": "789 Lake Street, Chicago, Illinois",
            "clothing": "Purple sweater, black pants"
        },
        "suspectVehicle": {
            "type": "SUV",
            "make": "Honda",
            "model": "CR-V",
            "color": "Blue",
            "licensePlate": "GHI9012"
        }
    },
    {
        "alertId": 5,
        "alertTime": "2023-11-18T09:45:00Z",
        "alertLocation": "San Francisco, California, United States",
        "alertType": "Missing Person",
        "missingPerson": {
            "name": "David Wilson",
            "age": 35,
            "gender": "Male",
            "description": "Black hair, brown eyes, height 5'11",
            "lastSeen": "2023-11-18T09:30:00Z",
            "lastSeenLocation": "123 Market Street, San Francisco, California",
            "clothing": "Green jacket, jeans"
        },
        "suspectVehicle": {
            "type": "Motorcycle",
            "make": "Harley-Davidson",
            "model": "Sportster",
            "color": "Black",
            "licensePlate": "JKL3456"
        }
    },
    {
        "alertId": 6,
        "alertTime": "2023-11-18T09:55:00Z",
        "alertLocation": "Miami, Florida, United States",
        "alertType": "Missing Person",
        "missingPerson": {
            "name": "Maria Garcia",
            "age": 28,
            "gender": "Female",
            "description": "Brown hair, blue eyes, height 5'7",
            "lastSeen": "2023-11-18T09:40:00Z",
            "lastSeenLocation": "456 Ocean Drive, Miami, Florida",
            "clothing": "Yellow blouse, white skirt"
        },
        "suspectVehicle": {
            "type": "Truck",
            "make": "Chevrolet",
            "model": "Silverado",
            "color": "Red",
            "licensePlate": "MNO7890"
        }
    },
    {
        "alertId": 7,
        "alertTime": "2023-11-18T10:05:00Z",
        "alertLocation": "Seattle, Washington, United States",
        "alertType": "Missing Person",
        "missingPerson": {
            "name": "James Anderson",
            "age": 50,
            "gender": "Male",
            "description": "Gray hair, brown eyes, height 5'9",
            "lastSeen": "2023-11-18T09:50:00Z",
            "lastSeenLocation": "123 Pine Street, Seattle, Washington",
            "clothing": "Blue shirt, khaki shorts"
        },
        "suspectVehicle": {
            "type": "Car",
            "make": "Nissan",
            "model": "Altima",
            "color": "White",
            "licensePlate": "PQR1234"
        }
    },
    {
        "alertId": 8,
        "alertTime": "2023-11-18T10:15:00Z",
        "alertLocation": "Denver, Colorado, United States",
        "alertType": "Missing Person",
        "missingPerson": {
            "name": "Olivia Taylor",
            "age": 19,
            "gender": "Female",
            "description": "Blonde hair, green eyes, height 5'4",
            "lastSeen": "2023-11-18T10:00:00Z",
            "lastSeenLocation": "789 Pine Avenue, Denver, Colorado",
            "clothing": "Pink sweater, black leggings"
        },
        "suspectVehicle": {
            "type": "Motorcycle",
            "make": "Honda",
            "model": "Rebel",
            "color": "Black",
            "licensePlate": "STU5678"
        }
    },
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

# Extract license plates from each JSON object and store them in a list
license_plates = [entry["suspectVehicle"]["licensePlate"] for entry in json_data]

# Print the list of license plates
print("License plates:", license_plates)
