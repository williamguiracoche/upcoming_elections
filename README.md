# Upcoming Elections Practical

## Purpose
The purpose of this app is to inform the user about upcoming elections based on the address of the user. The user simply fills out the form and the app returns the necessary information for the user.

The app uses the state and city of the user to create
and Open Civic Data ID (OPC-ID) and uses a Democracy Works Elections Public API to find upcoming elections.

## How to run

Full instructions for installing Flask can be found [here](http://flask.pocoo.org/docs/1.0/installation/)

For the requirements:
pip install -r requirements.txt

To run the app on your localhost, run:
python run.py

## Testing

```
pytest
```
## Notes about the project/ future things to work on
* There are no additional testing scripts yet.
* As it is right now, the app will only display the first upcoming election.

## Resources
* This mini app was done as an exercise for Democracy Works
* Public API by democracy Works
* Democracy Works provided base.html and address_form.html
