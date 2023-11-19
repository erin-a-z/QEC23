from flask import Flask, jsonify
from flask_restful import Api, Resource, abort
from flask_cors import CORS

import matplotlib.pyplot as plt
import numpy as np
import time

app = Flask("CO2.ai")
CORS(app)
api = Api(app)

class CO2AI(Resource):
    def get(self, _long, _lat, _start, _stop):
        now = time.time()
        long = float(_long)
        lat = float(_lat)
        start = float(_start)
        stop = float(_stop)
        bars = ""#[a.replace("-", " ") for a in _bars.split("_")]

        #GET DATA
        data = np.array([[1, 2], [3, 4]])

        fig, ax = plt.subplots()

        ax.plot(data)

        ax.set_xlabel("Time")
        ax.set_ylabel("CO2 Levels")

        fig_name = f"{_long}_{_lat}_{_start}_{_stop}_{now}_BARS_.jpg"
        fig.savefig(fig_name)

        return {"src": fig_name}



api.add_resource(CO2AI, "/api/<_long>/<_lat>/<_start>/<_stop>")

if __name__ == "__main__":
    app.run()
