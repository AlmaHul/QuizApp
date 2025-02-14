# Spelprojekt
Detta projekt tillåter användare att registrera sig, logga in och välja mellan två spelalternativ.

## Innehåll

- **Python 3.x**
- **Pip** 
- **Flask** verktyg för att skapa en webbapplikation
- **Pandas** för att hantera CSV-data
- **Tkinter** för att skapa GUI (grafiskt användargränssnitt)
- **Turtle** för att skapa grafik och visuella presentationer
- **Bcrypt** för att hash:a och verifiera lösenord.
- **Pytest** för att skriva och köra tester
- **Requests** för att göra HTTP-förfrågningar
- **Threading** för att kunna köra kod parallellt i olika trådar.


## Funktioner

- **Användarregistrering**: Användaren kan registrera ett konto genom ange ett användarnamn och lösenord.
- **Inloggning**: Efter registreringen kan användaren logga in med sina angivna uppgifter.
- **Spelalternativ**: När användaren är inloggad kan de välja mellan två spelalternativ.
- **Webbgränssnitt**: Flask tillhandahåller en enkel webbsida som visar de 50 amerikanska delstaterna.

## Spelalternativ

1. **Flask-webbplats**
    - En Flask-webbplats som visar alla de 50 amerikanska delstaterna i ett HTML-gränssnitt.

2. **Spel 1: Gissa delstater**
   - Användaren gissar namnen på USA´s 50 delstater.
   - När en stat gissas korrekt, placeras den på en karta.
   - Användaren kan avsluta när som helst genom att skriva "Exit".
   - Syftet med spelet är att gissa alla 50 stater.
   
3. **Spel 2: Frågesport**
   - Användaren får 10 frågor där de kan svara Sant eller Falskt.
   - Poängen uppdateras dynamiskt baserat på användarens svar.
   - Efter att ha besvarat alla frågor, får användaren sitt slutresultat.



## Installation

För att komma igång med projektet, följ dessa steg:

### Förutsättningar

Se till att du har följande installerat:

- **Python 3.x** (https://www.python.org/downloads/)
- **Pip** (https://pip.pypa.io/en/stable/)

### Steg för installation

#### 1. Klona repositoryt:

- Öppna terminalen (eller kommandotolken)
- Navigera till en plats där du vill lagra projektet. Använd cd-kommandot, till exempel:
  ```bash
  cd /QuizApp
- Kör följande kommando i terminalen för att klona repositoryt till din dator:  
  ```bash
  https://github.com/AlmaHul/QuizApp.git


#### 2. Efter att du har klonat repositoryt och har alla projektfiler på din dator, behöver du ladda ner alla de beroenden som anges i requirements.txt.
- Öppna terminalen
- Navigera till mappen där projektet är klonat:  
  ```bash
  cd QuizApp
- Skapa en virtuell Python-miljö  
**För Windows:**  
python -m venv venv  
.\venv\Scripts\activate  
**För Mac**  
python3 -m venv venv  
source venv/bin/activate
- Installera beroenden från requirements.txt:  
  ```bash
  pip install -r requirements.txt  
- Verifiera installationen:  
  ```bash
  pip list

#### 3. Andra moduler
- *Turtle* är en standardmodul som följer med Python, så den behöver inte installeras separat.
- Likaså *Threading*.
- *Tkinter* är också en standardmodul i Python, men på vissa system måste den installeras separat. Säkerställ att Tkinter är installerat, annars installera det manuellt. 

#### 4. Flask webbplats
- **Flask**: kan installeras via pip om det inte redan är installerat, det kan göras genom att öppna terminalen och köra:
  ```bash
  pip install flask
- För att starta Flask-servern separat:  
Navigera till `app/server.py` och kör:
  ```bash
  python server.py
  
#### 5. Bilder och filer 
**CSV-fil:** Projektet använder en CSV-fil som innehåller de 50 amerikanska delstaterna. Filen `50_states.csv` finns i projektets rotmapp. Den används för att visa delstater i Rätt eller Fel spelet och för att presentera alla delstater på webbplatsen.  

**Bilder:** Projektet innehåller tre bilder som finns i mappen images i rotmappen. Dessa tre bilder är blank_states_img.gif som är kartan över USA och de 50 staterna. Samt true.png och false.png som är rätt och fel knapparna i Rätt eller Fel spelet.

## Användning

### Köra programmet
För att starta programmet, kör `python main.py` i terminalen från projektets rotmapp.

### Registrera ett nytt konto
När programmet körs, välj alternativ 1 för att registrera ett nytt användarkonto. Du kommer att bli ombedd att ange ett användarnamn och lösenord.

### Logga in
Välj alternativ 2 för att logga in med dina användaruppgifter. Om login lyckas, kommer du att få tillgång till spelmenyn.

**Varning vid lösenordsinmatning:**
Vid lösenordsinmatning kan du få varningen `Warning: Password input may be echoed.`. Detta är ett känt beteende i vissa terminaler och innebär att terminalen kanske inte helt döljer inmatningen. Det påverkar inte funktionaliteten, men om du vill dölja inmatningen helt kan du prova att köra programmet i en annan terminal eller i en IDE som stöder lösenordsinmatning utan att visa texten.

### Spelmeny
När du är inloggad, kan du välja mellan fyra alternativ.   
Välj alternativ 1 för att starta flask webbservern och sedan kan du välja att spela genom att välja 2 eller 3, alternativt klicka på länken:  
*http://127.0.0.1:5000*  
för att se flask-webbplatsen. 

#### Exempel på hur menyn ser ut:
1. **50 stater:** Facit över de 50 delstaterna i en flask-webbplats.
2. **Gissa 50 stater:** Användaren får försöka att gissa alla 50 amerikanska delstaterna.
3. **Svara Rätt / Fel:** Användaren får svara på 10 rätt eller fel frågor.
4. **Avsluta:** Avslutar programmet.


### Testning
- För att köra testerna, kör pytest från projektets rotmapp. 
`pytest`
- Testfilerna finns i tests-mappen.
