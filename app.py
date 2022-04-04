"""Flask Application"""

from flask import Flask, jsonify

from blueprints.emailing import emailing

app = Flask(__name__, template_folder='email_templates')

app.register_blueprint(emailing)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) #for dev