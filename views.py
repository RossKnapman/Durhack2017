from flask import Flask
app = Flask(__name__)
from flask import render_template, redirect, request

import traceback
import logging

from lib.distances import *
from lib.elevation import *

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def show_form():
    '''Shows the homepage, with a search form'''
    return render_template('indextemplate.html')
    
@app.route('/results', methods=['POST', 'GET'])
def show_results():
    '''Calls the backend functions to obtain data, which is then shown'''
    try:
        start = [float(request.form['lat_a']),
                float(request.form['long_a'])]
        end = [float(request.form['lat_b']),
                float(request.form['long_b'])]
                
    except Exception as e:
        print "Error caught:\n",e
        return redirect('/error')
    
    else:
        delta_h = getheight(start, end, KEY, BASEURL)
        dist = haversine(start, end)/1000 #in km
        nearest_lock = find_nearest_bike_parking(end)
        #plus a bunch more cool things
        
        return render_template('resultstemplate.html',
                                searched=request.form,
                                delta_h=delta_h,
                                dist=dist,
                                nearest_lock=nearest_lock) #etc

@app.route('/error')
def show_error():
    return render_template('errortemplate.html')

# --------------------------------------------------
# placeholder functions
# these will be deleted once the functions to import are written
def elevation(a, b):
    '''takes a start and end and returns the change in elevation'''
    return 3.14