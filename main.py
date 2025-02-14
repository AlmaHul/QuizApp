import sys
import os

# Lägg till sökvägen till 'app' mappen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from app.app_home import UserApp

if __name__ == "__main__":
    app_instance = UserApp()
    app_instance.run()
