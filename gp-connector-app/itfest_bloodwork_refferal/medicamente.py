import json

class Medicine:
    def _init_(self, name, interval_hours):
        self.name = name
        self.interval_hours = interval_hours

def read_medicine_data_from_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        return json.load(json_file)

def search_medicine_schedule_from_json(medicine_name, json_file_path):
    medicines_info = read_medicine_data_from_json(json_file_path)
    for medicine_info in medicines_info:
        if medicine_info["name"].lower() == medicine_name.lower():
            return Medicine(medicine_info["name"], medicine_info["interval_hours"])
    return None

json_file_path = '/mnt/data/medicines.json'  # Path to the JSON file
user_input = "Ibuprofen"  # Simulated user input
medicine_found = search_medicine_schedule_from_json(user_input, json_file_path)

if medicine_found:
    print(f"Medicine: {medicine_found.name}, Interval: every {medicine_found.interval_hours} hours")
else:
    print("Medicine not found.")