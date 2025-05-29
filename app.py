from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'rdcafe_secret_key'

# Database Connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='razan2409',
    database='rd_cafe'
)
cursor = conn.cursor()

# ---------------- ROUTES ----------------

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        if user:
            session['user'] = user[1]  # name
            return redirect('/dashboard')
        else:
            message = "Login असफल भयो। कृपया फेरि प्रयास गर्नुहोस्।"
    return render_template('login.html', message=message)

# Signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    message = ""
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            message = "यो Email पहिले नै दर्ता भइसकेको छ।"
        else:
            cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
            conn.commit()
            message = "Sign-up सफल भयो! कृपया login गर्नुहोस्।"
            return redirect('/login')

    return render_template('signup.html', message=message)

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    return redirect('/login')

# Menu
@app.route('/menu')
def menu():
    cursor.execute("SELECT * FROM menu")
    items = cursor.fetchall()
    return render_template('menu.html', items=items)

# Order
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        item = request.form['item']
        quantity = request.form['quantity']
        cursor.execute("INSERT INTO orders (item, quantity) VALUES (%s, %s)", (item, quantity))
        conn.commit()
        return "Order सफलतापूर्वक गरियो!"
    return render_template('order.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')

# Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Coupon
@app.route('/coupon')
def coupon():
    return render_template('coupon.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# 404 Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# ---------------- MAIN ----------------
if __name__ == '__main__':
    app.run(debug=True)