from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    length = len(password)
    score = 0

    # If the password is less than 8 characters, it's considered weak
    if length < 8:
        return "Weak"

    # Check for a mix of upper and lower case characters
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1

    # Check for digits and special characters
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in '!@#$%^&*()_+' for c in password):
        score += 1

    # If length is greater than or equal to 12 and it passes the mix of conditions
    if length >= 12 and score == 4:
        return "Strong"

    # If it meets moderate criteria
    if score >= 3:
        return "Moderate"

    # If it doesn't meet any of the above, it's weak
    return "Weak"

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    strength = ""
    if request.method == "POST":
        password = request.form["password"]
        strength = check_password_strength(password)
    return render_template("index.html", password=password, strength=strength)

if __name__ == "__main__":
    app.run(debug=True)
