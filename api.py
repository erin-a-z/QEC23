from flask import Flask, jsonify
from flask_restful import Api, Resource, abort
from flask_cors import CORS

import matplotlib.pyplot as plt
import numpy as np
import time

import analysis

app = Flask("CO2.ai")
CORS(app)
api = Api(app)

class CO2AI(Resource):
    def get(self, _long, _lat, _start, _stop):
        np.random.seed(42)
        ctime = np.linspace(_start, _stop, 500)
        xco2 = np.polyval([1, -2, 5, 0, 3], time) + np.random.randn(100) * 10  # Replace with your own coefficients

        now = time.time()
        long = float(_long)
        lat = float(_lat)
        start = float(_start)
        stop = float(_stop)
        bars = ""#[a.replace("-", " ") for a in _bars.split("_")]

        #GET DATA
        data = analysis.get_pred(ctime, xco2, _stop)


        fig, ax = plt.subplots()

        ax.plot(ctime, xco2)

        ax.plot(data)

        ax.set_xlabel("Time")
        ax.set_ylabel("CO2 Levels")

        fig_name = f"{_long}_{_lat}_{_start}_{_stop}_{now}_BARS_.jpg"
        fig.savefig(fig_name)

        return {"src": fig_name}



api.add_resource(CO2AI, "/api/<_long>/<_lat>/<_start>/<_stop>")

if __name__ == "__main__":
    app.run()
