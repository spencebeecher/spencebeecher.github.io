from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_bingo():
    return send_from_directory('.', 'bingo.html')

if __name__ == '__main__':
    
    #app.listen(80, address="0.0.0.0")
    # bind the app to the address
    
    app.run(host="0.0.0.0", debug=False)
