"""
Dummy Flask Web Application
A simple web app that displays a welcome page and provides an API endpoint
"""




from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

# HTML template for the home page
HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Dummy Python App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        .endpoint {
            background-color: #e8f4f8;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        code {
            background-color: #f0f0f0;
            padding: 2px 6px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Welcome to Dummy Python App!</h1>
        <p>This is a simple Flask application demonstrating basic web functionality.</p>
        
        <h2>Available Endpoints:</h2>
        <div class="endpoint">
            <strong>GET /</strong> - This home page
        </div>
        <div class="endpoint">
            <strong>GET /api/hello</strong> - Returns a JSON greeting
        </div>
        <div class="endpoint">
            <strong>GET /api/status</strong> - Returns application status
        </div>
        
        <h2>Quick Test:</h2>
        <p>Try accessing: <code>http://localhost:5000/api/hello</code></p>
    </div>
</body>
</html>
"""


@app.route('/')
def home():
    """Home page with application information"""
    return render_template_string(HOME_TEMPLATE)


@app.route('/api/hello')
def hello():
    """Simple API endpoint that returns a greeting"""
    return jsonify({
        'message': 'Hello from the Dummy Python App!',
        'status': 'success',
        'version': '1.0.0'
    })


@app.route('/api/status')
def status():
    """API endpoint that returns application status"""
    return jsonify({
        'status': 'running',
        'environment': os.environ.get('FLASK_ENV', 'production'),
        'debug': app.debug
    })


if __name__ == '__main__':
    # Run the application
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    
    print(f"Starting Dummy Python App on port {port}...")
    print(f"Debug mode: {debug_mode}")
    print(f"Visit http://localhost:{port} to view the application")
    
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
