from getpass import getpass
from app.api_fetcher import ApiFetcher
from app.auth_manager import AuthManager
from app.data_processor import DataProcessor


class App:
    def __init__(self):
        self.auth_manager = AuthManager()
        self.api_fetcher = ApiFetcher()
        self.data_processor = DataProcessor()
    
    def run(self):
        while True:
            choice = input("Välkommen\n1. Registrera\n2. Logga in\n3. Avsluta\nVälj: ")
            if choice == "1":
                self.register()

            elif choice == "2":
                if self.login():
                    break
                
            elif choice == "3":
                print("Slut")
                return
        
        print("🔄 Laddar ner fruktdata...")
        self.api_fetcher.fetch_to_csv()
        print("✅ Fruktdata har sparats till csv")

        print("🔄 Behandlar fruktdata...")
        data = self.data_processor.process_data()
        print(data)
        print("✅ Fruktdata har sparats till csv")


    
    def register(self):
        username, password = self.prompt_username_password()
        try:
            self.auth_manager.register(username, password)
            print("Registrering lyckades")
        except Exception as err:
            print(err)


    def login(self):
        username, password = self.prompt_username_password()
        try:
            self.auth_manager.login(username, password)
            print("Login OK!")
            return True
        except Exception as err:
            print(err)
            return False

    

    def prompt_username_password(self):
        username = input("Användarnamn: ")
        password = getpass("Lösenord: ")
        return username, password
