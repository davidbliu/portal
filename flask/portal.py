from flask import Flask, request, jsonify, render_template
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('course_webpage.html')

@app.route("/past_announcements")
def past_announcements():
	return render_template('past_announcements.html')

if __name__ == "__main__":
    host = '0.0.0.0'
	port = 5139

	app.run(host = host, port = port, debug=True)
