from flask import Flask, request, jsonify
from difficulty import detect_difficulty
from simplifier import simplify_text

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
    return response

@app.route('/process', methods=['POST', 'OPTIONS'])
def process():
    if request.method == 'OPTIONS':
        return jsonify({}), 204

    data = request.json or {}
    text = data.get("text", "")

    try:
        level = detect_difficulty(text)
        simplified = simplify_text(text)
    except Exception as exc:
        return jsonify({
            "error": "Processing failed.",
            "details": str(exc)
        }), 500

    return jsonify({
        "difficulty": level,
        "simplified_text": simplified
    })

if __name__ == '__main__':
    app.run(debug=True)
