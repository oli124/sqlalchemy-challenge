import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a dictionary of precipitation by date"""
    # Query all dates and precipitation data points
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    date_prcp_query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > year_ago).all()

    date_prcp_dict = dict(date_prcp_query)

    session.close()

       
    return jsonify(date_prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations from dataset"""
    # Query all stations
        
    all_stations = session.query(Station.station).all()

    session.close()

    all_stations_unravel = list(np.ravel(all_stations))
       
    return jsonify(all_stations_unravel)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of temperature by date of most active station for previous year"""
    # Query all dates and tobs data points
    
    # Define year ago point
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Define most active station
    most_act_station = session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).all()

    # Query date and tobs with filters
    date_tobs_query = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == most_act_station[0][0]).\
    filter(Measurement.date > year_ago).all()

    date_tobs_dict = dict(date_tobs_query)

    session.close()
         
    return jsonify(date_tobs_dict)

# @app.route("/api/v1.0/<start>")
# def start_date(start):
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of min, avg, and max temperature for specified date range"""
#     # Query all dates and tobs data points
    
#     # Define year ago point
#     start_date = dt.date(2017, 1, 1)

#     min_temp = session.query(func.min(Measurement.tobs)).\
#     filter(Measurement.date > start_date).all()

#     max_temp = session.query(func.max(Measurement.tobs)).\
#     filter(Measurement.date > start_date).all()

#     avg_temp = session.query(func.avg(Measurement.tobs)).\
#     filter(Measurement.date > start_date).all()

#     print(f'The lowest temperature after {start_date} was {min_temp[0][0]}')
#     print(f'The highest temperature after {start_date} was {max_temp[0][0]}')
#     print(f'The average temperature after {start_date} was {round(avg_temp[0][0],1)}')
    
#     # Define most active station
#     most_act_station = session.query(Measurement.station, func.count(Measurement.station)).\
#     group_by(Measurement.station).\
#     order_by(func.count(Measurement.station).desc()).all()

#     # Query date and tobs with filters
#     date_tobs_query = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_act_station[0][0]).filter(Measurement.date > year_ago).all()

#     date_tobs_dict = dict(date_tobs_query)

#     session.close()
         
#     return jsonify(date_tobs_dict)


if __name__ == '__main__':
    app.run(debug=True)


