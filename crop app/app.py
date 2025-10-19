from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("iconhome.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/service')
def service():
    return render_template("service.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            return ("Please fill all the fields.")  # Translated error message

        # Process form (save/send etc.)
        print(f"Received contact from {name} - {email}: {message}")

        return render_template('succes.html')

    return render_template('contact.html')

@app.route('/language')
def language():
    return render_template("language.html")



if __name__ == '__main__':
    app.run(debug=True)
