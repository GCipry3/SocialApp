from flask import render_template, url_for, flash, redirect, request
from socialmedia_app import app, db, bcrypt


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')