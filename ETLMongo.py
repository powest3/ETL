from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.wine_db



# Creates a collection in the database and inserts two documents
db.wine.insert_many(
    [
        {
            'winery': 'Goat Bubbles',
            'region_1': 'Santa Maria Valley',
            'price' : '42'
        },
        {
            'winery': 'Grgich Hills',
            'region_1': 'Napa Valley',
            'price' : '93'
        }
    ]
)


# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    wines = list(db.wine.find())
    print(wines)

    # Return the template with the teams list passed in
    return render_template('index.html', wines=wines)


if __name__ == "__main__":
    app.run(debug=True)
