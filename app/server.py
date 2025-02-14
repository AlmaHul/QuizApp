from flask import Flask
import pandas as pd

flask_app = Flask(__name__)

@flask_app.route('/')
def facit_states():
    data = pd.read_csv("50_states.csv")
    html = """
           <div style="text-align: center;">
           <h3 style=""text-align: left>
           """ + '<br>'.join(data["state"].tolist()) + """
           </h3>
           </div>
           """
    return html

def start_flask_website():
    try:
        flask_app.run(debug=True, use_reloader=False, threaded=True)
    except KeyboardInterrupt:
        print("\nFlask-servern stängdes av.")

