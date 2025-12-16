from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    video = request.files["video"]
    path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(path)

    steps = """
    Step 1: Open the application.
    Step 2: Perform the actions shown in the recording.
    Step 3: Complete the workflow successfully.
    """

    return render_template("index.html", steps=steps)

if __name__ == "__main__":
    app.run(debug=True)
