from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return "Hello Admin, you have logged on {}".format(request.headers.get('User_Agent'))

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return render_template('user.html', name=name)

@app.route('/home')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)
