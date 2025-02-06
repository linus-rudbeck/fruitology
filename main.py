from app import App
from app.api_fetcher import ApiFetcher
from app.data_processor import DataProcessor
from app.server import server

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    print("{'a': 'b'}")
    print({"a": "b"})