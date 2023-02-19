import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = "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"

@app.route('/chatgpt', methods=['POST'])
def generate_text():
    data = request.get_json()
    if 'prompt' not in data:
        return jsonify({'error': 'A chave "prompt" está faltando no corpo da solicitação.'}), 400
    prompt = data['prompt']
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    response = {'response': message.strip()}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
