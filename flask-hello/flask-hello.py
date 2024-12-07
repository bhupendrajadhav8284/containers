from flask import Flask, jsonify

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Flask Hello world! Version 3'
 
@app.route('/test')
def test():
    return 'Testing hidden functionality ;)'

# Optional: Add error handlers
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500
 
if __name__ == '__main__':
    # Consider using environment variables for configuration
    app.run(
        debug=False,
        host='0.0.0.0',
        port=5000  # Explicitly define port
    )