from flask import Flask, Response
import paramiko

app = Flask(__name__)

HOST = "13.206.207.179"
USERNAME = "ubuntu"
KEY_FILE = r"C:\Users\janha\Downloads\wed_key.pem"

REMOTE_HTML = "/var/www/html/index.html"

@app.route("/")
def home():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=HOST,
            username=USERNAME,
            key_filename=KEY_FILE
        )

        stdin, stdout, stderr = ssh.exec_command(f"cat {REMOTE_HTML}")

        html = stdout.read().decode()

        ssh.close()

        return Response(html, mimetype="text/html")

    except Exception as e:
        return f"<h2>Error</h2><pre>{e}</pre>"

if __name__ == "__main__":
    app.run(debug=True)