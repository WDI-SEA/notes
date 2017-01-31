from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"
  
@app.route("/profile/<username>")
def profile(username):
  return "You're viewing {}'s profile.".format(username)
  
@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
  # WARNING: Python expects route results to be strings. We must manually
  # convert our mathematical number return value into a string with str()
  result = num1 * num2
  return str(result)

if __name__ == "__main__":
  app.run()
