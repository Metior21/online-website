from flask import Flask, jsonify, request
  
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/getLocations', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        
        locations = [
      ['Bondi Beach', -33.890542, 151.274856, 4],
      ['dfhfsdf', -33.923036, 151.259052, 5],
      ['Pretonder Caneday Waley JATT', -34.028249, 151.157507, 3],
      ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
      ['Maroubra Beach', -33.950198, 151.259302, 1]
    ]
        response= jsonify(locations)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == '__main__':
  
    app.run(debug = True)