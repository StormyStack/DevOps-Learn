from flask import Flask, render_template

app = Flask(__name__)

# Root route
@app.route('/')
def root():
    return render_template('index.html')

# Health check route
@app.route('/health')
def health_check():
    return 'Everything healthy here!', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
