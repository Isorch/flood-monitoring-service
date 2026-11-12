from pathlib import Path
from flask import Flask, render_template, jsonify, send_file

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CURRENT_DIR = DATA_DIR / "current"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/geojson/current")
def geojson_current():
    # TODO: чтение shapefile через geopandas
    return jsonify({"type": "FeatureCollection", "features": []})


@app.route("/metadata/current")
def metadata_current():
    # TODO: чтение meta.json
    return jsonify({"status": "no_data", "message": "Актуальных данных о затоплении нет"})


@app.route("/download/shapefile")
def download_shapefile():
    # TODO: сборка ZIP
    return "Функция в разработке", 501


@app.route("/download/geojson")
def download_geojson():
    # TODO: реализация
    return "Функция в разработке", 501


if __name__ == "__main__":
    app.run(debug=True)