# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)

@app.route('/play')
def level1():
    return render_template('index.html')

@app.route('/play/<int:num>')
def level2(num):
    return render_template('index.html', num=num)

@app.route('/play/<int:box_num>/<string:name>')
def level3(box_num, name):
    return render_template('index.html', num = box_num, color = name)



if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
