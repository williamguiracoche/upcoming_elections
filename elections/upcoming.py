import functools
import requests

from elections import ocd_tools

from elections.us_states import postal_abbreviations

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('address_form', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def search():
    """Take in an address."""
    if request.method == 'GET':
        return render_template('address_form.html', states=postal_abbreviations)
        
    if request.method == 'POST':
        # Retrieve address values from form submission
        street = request.form['street']
        street2 = request.form['street-2']
        city = request.form['city']
        state = request.form['state']
        zip_num = request.form['zip']
        
        # To print the values from the form, uncomment below: 
        # print([street, street2, city, state])

        # Get data from (state, city) 
        data = ocd_tools.get_all(state, city)

        # If you were able to get data from the (city, state) then send 
        # the user to the elections results route
        if data:
            return redirect(url_for('address_form.result', city = city, state= state))

        # If you were NOT able to get data from the (city, state) then 
        # do not show results to user. Just send a flash message that 
        # there are no upcoming elections for the user's area.    
        else:
            flash("No upcoming elections for your area")
            return render_template('address_form.html', states=postal_abbreviations)

@bp.route('election-results/<state>/<city>')
def result(state, city):
    """ Show the details of the upcoming elections to the user """

    # Pull data from state and city 
    # Data in format [website, polling_place, description, date]
    data = ocd_tools.get_all(state, city)

    # If you were able to get data from the (state, city) then show 
    # the user election_results.html with their custom data
    if data:
        website = data[0]
        polling_place_url = data[1]
        description = data[2]
        date = data[3]
        
        return render_template('election_results.html', \
            state = state, city =city.title(), \
            website = website, date=date, \
            description = description, polling_place_url = polling_place_url)

    # If the user typed a url for a (state, city) that did NOT return data,
    # the user will be redirected to the form with a flashed message saying
    # that there are no upcoming elections.
    else:
        flash("No upcoming elections for your area")
        return redirect(url_for('address_form.search'))