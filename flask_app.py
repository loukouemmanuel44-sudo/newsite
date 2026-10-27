from flask import Flask

app = Flask(__name__)

@app.get("/")
def accueil():
    return """
    <html>
    <head>
        <title>Emmanuel Loukou</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background:#f4f4f4;
                text-align:center;
                padding:40px;
            }

            .card{
                background:white;
                max-width:700px;
                margin:auto;
                padding:30px;
                border-radius:15px;
                box-shadow:0 0 10px rgba(0,0,0,0.2);
            }

            img{
                width:180px;
                border-radius:50%;
            }

            h1{
                color:#222;
            }

            a{
                text-decoration:none;
                color:#0078d4;
                font-weight:bold;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>Loukou Emmanuel</h1>

            <p>
                Étudiant en Bachelor Informatique à l'EPSI Paris
            </p>

            <p>
                Passionné par le développement web, Linux et les réseaux.
            </p>

            <h2>Compétences</h2>

            <ul style="list-style:none;">
                <li>HTML / CSS / JavaScript</li>
                <li>Python</li>
                <li>PHP</li>
                <li>Linux</li>
                <li>Réseaux</li>
            </ul>

            <br>

            <a href="https://github.com/loukouemmanuel44-sudo">
                Mon GitHub
            </a>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
