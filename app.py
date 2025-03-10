<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
import os

app = Flask(__name__)
app.config.from_object('config.Config')
app.secret_key = 'your_secret_key_here'

=======
from flask import Flask, render_template, request, redirect, url_for, flash
=======
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
>>>>>>> c43bdd4 (init)
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
import os

app = Flask(__name__)
<<<<<<< HEAD
app.config.from_object(Config)
>>>>>>> 1f6e356 (init)
=======
app.config.from_object('config.Config')
app.secret_key = 'your_secret_key_here'

>>>>>>> c43bdd4 (init)
mysql = MySQL(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

<<<<<<< HEAD
<<<<<<< HEAD
@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor()
=======
# User loader function
@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
>>>>>>> 1f6e356 (init)
=======
@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor()
>>>>>>> c43bdd4 (init)
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
<<<<<<< HEAD
<<<<<<< HEAD
        return User(id=user[0], username=user[1], email=user[2])
=======
        return User(id=user['id'], username=user['username'], email=user['email'])
>>>>>>> 1f6e356 (init)
=======
        return User(id=user[0], username=user[1], email=user[2])
>>>>>>> c43bdd4 (init)
    return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
<<<<<<< HEAD
<<<<<<< HEAD
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()
        cursor.close()
        if user and bcrypt.check_password_hash(user[3], password):
            user_obj = User(id=user[0], username=user[1], email=user[2])
            login_user(user_obj)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials', 'danger')
=======

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
=======
        cursor = mysql.connection.cursor()
>>>>>>> c43bdd4 (init)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()
        cursor.close()
        if user and bcrypt.check_password_hash(user[3], password):
            user_obj = User(id=user[0], username=user[1], email=user[2])
            login_user(user_obj)
            flash('Login successful!', 'success')
<<<<<<< HEAD
            return redirect(url_for('dashboard'))  # Redirect to dashboard

        flash('Invalid credentials. Please try again.', 'danger')

>>>>>>> 1f6e356 (init)
=======
            return redirect(url_for('dashboard'))
        flash('Invalid credentials', 'danger')
>>>>>>> c43bdd4 (init)
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
<<<<<<< HEAD
<<<<<<< HEAD
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            cursor.close()
            flash('Email already exists.', 'danger')
            return redirect(url_for('register'))
        password = bcrypt.generate_password_hash(password).decode('utf-8')
        cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                       (username, email, password))
        mysql.connection.commit()
        cursor.close()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
=======

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
=======
        cursor = mysql.connection.cursor()
>>>>>>> c43bdd4 (init)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            cursor.close()
            flash('Email already exists.', 'danger')
            return redirect(url_for('register'))
        password = bcrypt.generate_password_hash(password).decode('utf-8')
        cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                       (username, email, password))
        mysql.connection.commit()
        cursor.close()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
<<<<<<< HEAD

>>>>>>> 1f6e356 (init)
=======
>>>>>>> c43bdd4 (init)
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c43bdd4 (init)
@app.route('/download-dataset')
@login_required
def download_dataset():
    file_path = os.path.join('static', 'datasets', 'gdp_data.csv')
    return send_file(file_path, as_attachment=True)

<<<<<<< HEAD
=======
>>>>>>> 1f6e356 (init)
=======
>>>>>>> c43bdd4 (init)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
