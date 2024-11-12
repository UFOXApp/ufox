from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a route
@app.route("/")
def home():
    return "Hello, UFO Sightings!"

# Run the app (optional, mainly for local testing)
if __name__ == "__main__":
    app.run(debug=True)
