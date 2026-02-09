from flask import Flask, request, send_file
import subprocess
import uuid
import os

app = Flask(__name__)

@app.route("/download")
def download_audio():
    url = request.args.get("url")
    if not url:
        return {"error": "Missing url parameter"}, 400

    filename = f"/tmp/{uuid.uuid4()}.mp3"

    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "-o", filename,
        url
    ]

    subprocess.run(cmd, check=True)

    return send_file(filename, as_attachment=True)

import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

