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
m = Base.classes.measurement
s = Base.classes.station
se = Session(engine)

# Create an app
app = Flask(__name__)

@app.route("/")
def index():
    return (
        f"Welcome to the Homepage!<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><end>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
    qDate = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    result = se.query(m.date, m.prcp).\
        filter(m.date >= qDate).all()
    pre = {date: prcp for date, prcp in result}
    se.close()
    return jsonify(pre)

@app.route("/api/v1.0/stations")
def stations():
    stQuery = se.query(s.station, s.name).all()
    stList = list(np.ravel(stQuery))
    se.close()
    return jsonify(stList)
  
@app.route("/api/v1.0/tobs")
def temp():
    oYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    pYear = se.query(m.tobs).filter(m.date >= oYear).\
        filter(m.station == 'USC00519281').all()
    tempList = list(np.ravel(pYear))
    se.close()
    return jsonify(tempList)

@app.route("/api/v1.0/<start>")
def tempList2(start):
    start1 = se.query(func.min(m.tobs), func.avg(m.tobs), func.max(m.tobs)).\
        filter(m.date >= start).all()
    stList2 = list(np.ravel(start1))
    se.close()
    return jsonify(stList2)

@app.route("/api/v1.0/<start>/<end>")
def stEnd(start, end):
    startDate = dt.datetime.strptime(start, '%Y-%m-%d')
    endDate = dt.datetime.strptime(end, '%Y-%m-%d')
    tempBoth = se.query(func.min(m.tobs), func.avg(m.tobs), func.max(m.tobs)).\
        filter(m.date >= startDate).\
        filter(m.date <= endDate).all()
    tempStend = list(np.ravel(tempBoth))
    se.close()
    return jsonify(tempStend)

if __name__ == "__main__":
    app.run(debug=True)
