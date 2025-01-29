from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Backend Table (List of Names)
names_table = [
    "Shanmugapriya", "BOB", "Charlie", "David", "Emma",
    "Frank", "Grace", "Hannah", "Ian", "Jack"
]

# API Endpoint to get the list of names
@app.route('/api/names', methods=['GET'])
def get_names():
    return jsonify({"names": names_table})

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
