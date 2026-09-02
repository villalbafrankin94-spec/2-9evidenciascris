from flask import Flask
import pymysql
import os

app = Flask(__name__)


def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "servidor-bd"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "sre_db"),
        port=3306
    )


@app.route("/")
def home():
    try:
        connection = get_connection()
        connection.close()

        return {
            "status": "OK",
            "message": "API funcionando y conectada a MySQL"
        }, 200

    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }, 500


@app.route("/health")
def health():
    return {"status": "UP"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104
