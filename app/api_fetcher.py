import csv
import requests

class ApiFetcher:
    API_URL = "https://fruityvice.com/api/fruit/all"

    def fetch_data(self):
        response = requests.get(self.API_URL)
        if response.status_code == 200: # OK
            return response.json()
        else:
            raise Exception("Fel vid API-anrop")
    

    def save_to_csv(self, data, filename="data.csv"):
        with open(filename, mode="w", newline="") as file :
            writer = csv.writer(file)
            header = data[0].keys()
            writer.writerow(header)
            for entry in data:
                writer.writerow(entry.values())


    def fetch_to_csv(self):
        data = self.fetch_data()
        self.save_to_csv(data)
