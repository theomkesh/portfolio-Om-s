from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ensure the data directory exists
if not os.path.exists('data'):
    os.makedirs('data')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    message = request.form['message']

    # Save the data to a file
    with open('data/contact_data.txt', 'a') as file:
        file.write(f'Name: {name}\n')
        file.write(f'Email: {email}\n')
        file.write(f'Number: {number}\n')
        file.write(f'Message: {message}\n')
        file.write('---\n')

    return jsonify({"status": "success", "message": "Data saved successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


