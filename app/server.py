from flask import Flask, render_template
import pandas as pd

from app.data_processor import DataProcessor

server = Flask(__name__)

@server.route("/")
def home():
    data_processor = DataProcessor()
    data_processor.load_data()
    data_processor.process_nutritions()
    tables = [data_processor.df.to_html(classes="data"), ]
    titles = data_processor.df.columns.values
    return render_template("home.html", titles=titles, tables=tables)

if __name__ == "__main__":
    server.run(debug=True)