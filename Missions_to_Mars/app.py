from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# @TODO: setup mongo connection
import pymongo

# @TODO: connect to mongo db and collection
conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)


@app.route('/')
def index():
   
    # @TODO: render an index.html template and pass it the data you retrieved from the database
    return
    return render_template('index.html',product=product)



if __name__ == "__main__":
    app.run(debug=True)
