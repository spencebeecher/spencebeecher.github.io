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
@app.route('/holly.png')
def serve_holly():
    return send_from_directory('.', 'holly.png')

# serve spooky.png

@app.route('/spooky.png')
def serve_spooky():
    return send_from_directory('.', 'spooky.png')

# slasher page and image
@app.route('/slasher.html')
def serve_slasher_page():
    return send_from_directory('.', 'slasher.html')

@app.route('/slasher.png')
def serve_slasher_image():
    return send_from_directory('.', 'slasher.png')

# monster page and image
@app.route('/monster.html')
def serve_monster_page():
    return send_from_directory('.', 'monster.html')
@app.route('/monster.png')
def serve_monster_image():
    return send_from_directory('.', 'monster.png')


@app.route('/super_spooky.png')
def serve_super_spooky():
    return send_from_directory('.', 'super_spooky.png')


@app.route('/october-fest.html')
def serve_octoberfest():
    return send_from_directory('.', 'octoberfest.html')
@app.route('/octoberfest.png')
def serve_octoberfest_image():
    return send_from_directory('.', 'octoberfest.png')

# stranger things page and image
@app.route('/stranger_things.html')
def serve_stranger_things():
    return send_from_directory('.', 'stranger_things.html')
@app.route('/stranger.png')
def serve_stranger_image():
    return send_from_directory('.', 'stranger.png')

# football page and image
@app.route('/football.html')
def serve_football():
    return send_from_directory('.', 'football.html')
@app.route('/football.png')
def serve_football_image():
    return send_from_directory('.', 'football.png')

# bingo.png
@app.route('/bingo.png')
def serve_bingo_image():
    return send_from_directory('.', 'bingo.png')

if __name__ == '__main__':
    
    #app.listen(80, address="0.0.0.0")
    # bind the app to the address
    
    app.run(host="127.0.0.1", debug=False, port=8080)
    
