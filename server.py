from flask import Flask, render_template, redirect, request, session
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    return render_template("index.html", all_friends=friends)

@app.route('/add', methods=['POST'])
def add_friend():
    data = {
    'first_name': request.form['fname'],
    'last_name': request.form['lname'],
    'occupation': request.form['occ']
    }
    Friend.insert_friend(data)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    id = int(request.form['f_id'])
    Friend.delete_friend(id)
    return redirect('/')

@app.route('/get_friend', methods=['POST'])
def get_friend():
    id = int(request.form['fid'])
    print(id)
    friend = Friend.get_friend(id)
    session['friend_fname'] = friend.first_name
    session['friend_lname'] = friend.last_name
    session['friend_occ'] = friend.occupation
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
