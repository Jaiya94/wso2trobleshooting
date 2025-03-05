from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route for the /abc path
@app.route('/abc', methods=['GET'])
def abc():
    # Check for the required header
    required_header = 'X-Custom-Header'
    header_value = request.headers.get(required_header)

    # If the header is missing, return an error message
    if not header_value:
        return jsonify({
            "code": "400",
            "message": "Bad request"
        }), 400

    # If the header is present, return the normal response
    return jsonify({
        "message": "Header received successfully",
        "header_value": header_value
    })

if __name__ == '__main__':
    # Run the server on port 6000
    app.run(host='0.0.0.0', port=6000)
