from flask import Flask, render_template
import sqlite3
import pathlib

app = Flask(__name__) # Flask is a class

base_path = pathlib.Path().cwd()
db_name = "Churn_Modelling.db"
file_path = base_path / db_name


@app.route("/")
def index():
    return render_template( "index.html")

@app.route("/about")
def about():
    return render_template( "about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    Churn_Modelling_data = cursor.execute("SELECT * FROM Churn_Modelling_data").fetchall()
    cols = cursor.execute("PRAGMA table_info(Churn_Modelling_data)").fetchall()
    columns = [column[1] for column in cols]
    con.close()
    return render_template( "data_table.html", Churn_Modelling_data = Churn_Modelling_data, columns=columns)


if __name__=="__main__":
    app.run(debug=True)