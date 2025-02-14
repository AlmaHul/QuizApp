from app.auth_manager import AuthManager
from getpass import getpass
from app.play_quiz import start_quiz
from app.states_game import guess_states_play
import threading
from app.server import start_flask_website


class UserApp:
    """Visar menyer för användaren att välja olika alternativ."""
    def __init__(self):
        self.auth_manager = AuthManager()

    def run(self):
        while True:
            choice = input("Välkommen\n1. Registrera\n2. Logga in\n3. Avsluta\nVälj:  ")
            if choice == "1":
                self.register()
            elif choice == "2":
                if self.login():  # Om login returnerar True, visa spelmenyn
                    self.show_logged_in_menu()
            elif choice == "3":
                print ("Slut")
                break
            else:
                print("Du måste välja ett alternativ")

    def get_user_credentials(self):
        username = input("Användarnamn: ")
        password = getpass("Lösenord: ")
        return username, password

    def register(self):
        username, password = self.get_user_credentials()
        try:
            self.auth_manager.register(username, password)
            print("Registereing lyckades")
        except Exception as err:
            print(err)

    def login(self):
        username, password = self.get_user_credentials()
        try:
            self.auth_manager.login(username, password)
            print("Du är nu inloggad")
            return True
        except Exception as err:
            print(err)
            return False


    def show_logged_in_menu(self):
        while True:
            choice= input("\nVad vill du göra?\n1. Visa facit på 50 stater\n2. Gissa 50 stater\n3. Svara rätt eller Fel\n4. Avsluta\nVälj: ")
            if choice == "1":
                self.show_webpage()
            elif choice == "2":
                guess_states_play()
            elif choice == "3":
                start_quiz()
            elif choice == "4":
                print("Avslutar...")
                break
            else:
                print("Ogiltigt val. Försök igen.")

    def show_webpage(self):
        # Starta Flask-webbplatsen i en separat tråd
        try:
            flask_thread = threading.Thread(target=start_flask_website)
            flask_thread.daemon = True  # Gör tråden till en daemon-tråd så att den stängs när huvudtråden avslutas
            flask_thread.start()
            print("Webbplatsen är nu igång. Gå till http://127.0.0.1:5000/ för att se den.")
            self.show_logged_in_menu()

        except KeyboardInterrupt:
            print("\nFlask-servern stoppades av användaren.")
        except Exception as err:
            print(err)


