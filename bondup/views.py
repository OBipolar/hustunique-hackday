from bondup import app

@app.route('/')
def home():
    return 'Welcome.'

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/person/<int:person_id>')
def show_person(person_id):
    cur = db.execute('SELECT iden, age FROM people WHERE id = ?', person_id)
    person = cur.fetchall()
    return render_template('show_person.html', person=person)