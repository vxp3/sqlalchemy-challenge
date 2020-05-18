import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
#m = Base.classes.measurment
# s = Base.classes.station
# se = Session(engine)
# # 2. Create an app
# app = Flask(__name__)
# # 3. Define static routes
# @app.route("/")
# def index():
#     return (
#         f"Welcome to the Homepage!<br/>"
#         f"/api/v1.0/precipitation<br/>"
#         f"/api/v1.0/stations<br/>"
#         f"/api/v1.0/tobs<br/>"
#         f"/api/v1.0/<start><end>"
#         )
# @app.route("/api/v1.0/precipitation")
# def precipitation():
#     query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     result=se.query(m.prcp, m.date).\
#         filter(m.date >= query_date).order_by(m.date).all()
#     pre = {date: prcp for date, prcp in result}
#     return jsonify(pre)

# @app.route("/api/v1.0/stations")
# def stations():
#     stations=se.query(m.station).all()
#     station_list=list(np.ravel(stations))
#     return jsonify(station_list)

# @app.route("/api/v1.0/tobs")
# def temp():
#     oYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     pYear = se.query(m.tobs).filter(m.date >= oYear).filter(m.station == 'USC00519281').all()
#     temp_list=list(np.ravel(pYear))
#     return jsonify(station_list)

# @app.route("/api/v1.0/<start>")
# @app.route("/api/v1.0/<start><end>")
# def calc_temps(start_date = None, end_date = None):
    
#     if not end:
  
#         result = se.query(func.min(m.tobs), func.avg(m.tobs), func.max(m.tobs)).filter(m.date >= start_date).all() 
#         temp_list = list(np.ravel(result))
#         return jsonify( temp_list)
    
#     result = se.query(func.min(m.tobs), func.avg(m.tobs), func.max(m.tobs)).filter(m.date >= start_date).filter(m.date <= end_date).all()
#     temp_list = list(np.ravel(result))
#     return jsonify( temp_list)

if __name__ == "__main__":
    app.run(debug=True)
