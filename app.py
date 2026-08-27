from flask import Flask, send_from_directory, render_template_string
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
PLAYLIST_FILE = "playlist.m3u"


@app.route("/")
def home():
    playlist_url = "/playlist.m3u"

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Stream Server</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #111827;
                color: white;

                display: flex;
                justify-content: center;
                align-items: center;

                min-height: 100vh;
                margin: 0;
            }}

            .container {{
                width: 90%;
                max-width: 600px;

                background: #1f2937;

                padding: 30px;
                border-radius: 15px;

                box-sizing: border-box;
            }}

            h1 {{
                margin-top: 0;
            }}

            .url {{
                background: #111827;

                padding: 15px;

                border-radius: 8px;

                word-break: break-all;

                margin: 20px 0;
            }}

            a {{
                display: inline-block;

                background: #2563eb;

                color: white;

                text-decoration: none;

                padding: 12px 18px;

                border-radius: 8px;
            }}

            a:hover {{
                background: #1d4ed8;
            }}
        </style>
    </head>

    <body>

        <div class="container">

            <h1>📺 Stream Server</h1>

            <p>Sua playlist está disponível em:</p>

            <div class="url">
                /playlist.m3u
            </div>

            <a href="{playlist_url}">
                Abrir playlist
            </a>

        </div>

    </body>
    </html>
    """

    return render_template_string(html)


@app.route("/playlist.m3u")
def playlist():

    return send_from_directory(
        BASE_DIR, PLAYLIST_FILE, mimetype="text/plain", as_attachment=False
    )


@app.route("/health")
def health():

    return {"status": "ok"}


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080, debug=True)
