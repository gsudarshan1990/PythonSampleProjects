from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! "

"""
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
"""
