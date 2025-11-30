from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Your video translation server is running!"

if __name__ == "__main__":
    app.run()
  
