from flask import Flask

#create flask instance
app = Flask(__name__)

@ app.route("/")
def hello():
    return "Hello, World"

<<<<<<< HEAD

app.run('0.0.0.0', port=5000)
=======
app.run('0.0.0.0', port=5000,)
app.run(debug=True)
>>>>>>> 85b02e7 (make some changes)

