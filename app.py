from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Route for the Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the Admin Page
@app.route('/admin')
def admin():
    # This will serve the admin.html file you already created
    return render_template('admin.html')

# Route for an About Page (just returning text, no HTML file needed)
@app.route('/about')
def about():
    return "<h1>About Us</h1><p>This is a simple Python web application running on EC2!</p>"

if __name__ == '__main__':
    # host='0.0.0.0' is crucial for EC2 so it can accept outside connections
    # port=5000 is the default port for Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
