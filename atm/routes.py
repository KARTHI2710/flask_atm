from . import app
from flask import Flask,render_template

@app.route('/')
def cardless():
    return render_template('atm/cardless.html',title="cardless")