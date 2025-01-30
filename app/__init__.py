from app.auth_manager import AuthManager


class App:
    def __init__(self):
        self.auth_manager = AuthManager()
    
    def run(self):
        while True:
            choice = input("Välkommen\n1. Registrera\n2. Logga in\n3. Avsluta\nVälj: ")
            if choice == "1":
                print("Registrera")
            elif choice == "2":
                print("Login")
            elif choice == "3":
                print("Slut")
                break
    
    def login(self):
        pass # ALL KOD FÖR LOGIN
    
    def register(self):
        pass # ALL KOD FÖR register
