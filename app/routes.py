from flask import request, jsonify
from .auth import check_firebase_token
from .models import summarizer, generator
from .utils import validate_text


def configure_routes(app):
    @app.route('/api/generate', methods=['POST'])
    @check_firebase_token
    def generate_text():
        data = request.get_json()
        error = validate_text(data.get('text'))
        if error:
            return jsonify({'error': error}), 400
        text = generator(data['text'], max_length=1000)[0]['generated_text']
        return jsonify({'title': data.get('title', 'Untitled'), 'generated_text': text})

    @app.route('/api/summarize', methods=['POST'])
    @check_firebase_token
    def summarize_text():
        data = request.get_json()
        error = validate_text(data.get('text'))
        if error:
            return jsonify({'error': error}), 400
        summary = summarizer(data['text'], min_length=30, max_length=200)[
            0]['summary_text']
        return jsonify({'title': data.get('title', 'Untitled'), 'summary_text': summary})
