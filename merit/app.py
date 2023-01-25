from flask import Flask, render_template, request, abort
import sqlite3

con = sqlite3.connect("main.db")

def get_house(name):
    cur = con.cursor()
    x = cur.execute("SELECT * FROM students WHERE house=(?)", (name,))
    return x.fetchall()
    cur.close()

def get_points(house_name):
    cur = con.cursor()
    points = cur.execute("SELECT SUM(points) FROM students WHERE house=(?)", (house_name,))
    return points.fetchall()
    cur.close()

app = Flask(__name__)

cur = con.cursor()


# Discoverers
disco = get_house("Discoverers")
disco_points = get_points("Discoverers")

#Explorers
expo = get_house("Explorers")
expo_points = get_points("Explorers")

#Voyagers
voya = get_house("Voyagers")
voya_points = get_points("Voyagers")

#Pioneers
pio = get_house("Pioneers")
pio_points = get_points("Pioneers")

houses = {
    "disco": disco,
    "expo": expo,
    "voya": voya,
    "pio": pio
}

print(houses)

house_points = {
    "disco": disco_points,
    "expo": expo_points,
    "voya": voya_points,
    "pio": pio_points
}

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', msg="Page Not Found")

@app.route("/")
def index():
    return render_template("index.html", house=house, house_points=house_points)

@app.route("/house/<house>")
def house(house):
    if house == "disco":
        return render_template("students.html", house_name="Discoverers",houses=houses[house], house_points=house_points[house])
    elif house == "expo":
        return render_template("students.html", house_name="Explorers",houses=houses[house], house_points=house_points[house])
    elif house == "pio":
        return render_template("students.html", house_name="Pioneers",houses=houses[house], house_points=house_points[house])
    elif house == "voya":
        return render_template("students.html", house_name="Voyagers",houses=houses[house], house_points=house_points[house])

@app.route("/edit")
def edit():
    return render_template("edit.html")

if __name__ == '__main__':
    app.run(debug=True, port=8001)