import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from sqlalchemy import extract 

# setup Database engine
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the Database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link
session = Session(engine)

# setup Flask and create routes
app = Flask(__name__)

months = ["January", "February", "March", "April", "May", "June", "July",\
    "August", "September", "October", "November", "December"]


@app.route("/")
def welcome():
    return(
        '''
    Welcome to the Climate Analysis API!<br>
    Available Routes:<br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/temp/start/end<br>
    /api/v1.0/num_month<br>
    ''')


@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    session = Session(engine)
    sel = [func.min(Measurement.tobs), func.avg(
             Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
       results = session.query(*sel).\
                   filter(Measurement.date >= start).\
                   filter(Measurement.date <= end).all()
       temps = list(np.ravel(results))
       session.close()
       return jsonify(temps)

    results = session.query(*sel).\
      filter(Measurement.date >= start).\
      filter(Measurement.date <= end).all()
    session.close()
    temps = list(np.ravel(results))
    return jsonify(temps)

## challenge
@app.route("/api/v1.0/<nm>")
def june_stats(nm=1):
    session = Session(engine)
    month = months[int(nm)-1]
    sel1 = [func.min(Measurement.prcp), func.avg(
             Measurement.prcp), func.max(Measurement.prcp)]
    sel2 = [func.min(Measurement.tobs), func.avg(
             Measurement.tobs), func.max(Measurement.tobs)] 
    prcp_month = session.query(*sel1).filter(extract('month', Measurement.date)==nm).all()
    tobs_month = session.query(*sel2).filter(extract('month', Measurement.date)==nm).all()
    session.close()
    
    temps1=list(np.ravel(prcp_month))
    temps2=list(np.ravel(tobs_month))
       
    return  jsonify(month, "min-avg-max precipitation", temps1,\
         "min-avg-max temperature", temps2)


if __name__ == '__main__':
    app.run(debug=True)


