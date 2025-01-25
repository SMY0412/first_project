#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add():
    try:
        value1 = int(request.form.get("value1", 0))
        value2 = int(request.form.get("value2", 0))
        result = value1 + value2
        return f"Result: {result}"
    except:
        return "Error encountered"