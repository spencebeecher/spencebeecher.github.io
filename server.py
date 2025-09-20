from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_bingo():
    return send_from_directory('.', 'index.html')

# serve christmas.html
@app.route('/christmas.html')
def serve_christmas():
    return send_from_directory('.', 'christmas.html')

#serve haloween.html
@app.route('/halloween.html')
def serve_haloween():
    return send_from_directory('.', 'halloween.html')

#serve spooky.html
@app.route('/spooky.html')
def serve_spooky_page():
    return send_from_directory('.', 'spooky.html')

# serve holly.jpeg
@app.route('/holly.jpeg')
def serve_holly():
    return send_from_directory('.', 'holly.jpeg')

@app.route('/spooky.png')
def serve_spooky():
    return send_from_directory('.', 'spooky.png')

@app.route('/super_spooky.png')
def serve_super_spooky():
    return send_from_directory('.', 'super_spooky.png')

if __name__ == '__main__':
    
    #app.listen(80, address="0.0.0.0")
    # bind the app to the address
    
    app.run(host="127.0.0.1", debug=False, port=8080)
    
