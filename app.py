from flask import Flask, render_template, request, redirect, url_for, send_file
from Connection.Connect import connect
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def index():
    conn = connect()
    if not conn:
        return "Ошибка подключения к базе данных."

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM documents")  # Пример запроса
    files = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "Файл не выбран."

    file = request.files['file']
    if file.filename == '':
        return "Файл не выбран."

    conn = connect()
    if not conn:
        return "Ошибка подключения к базе данных."

    try:
        cursor = conn.cursor()
        query = "INSERT INTO documents (file_name, file_data) VALUES (%s, %s)"
        cursor.execute(query, (file.filename, file.read()))
        conn.commit()
        return "Файл успешно загружен!"
    except Exception as e:
        return f"Ошибка: {e}"
    finally:
        cursor.close()
        conn.close()


@app.route('/download/<int:file_id>')
def download(file_id):
    conn = connect()
    if not conn:
        return "Ошибка подключения к базе данных."

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT file_name, file_data FROM documents WHERE id = %s", (file_id,))
        file = cursor.fetchone()
        if file:
            return send_file(
                BytesIO(file[1]),
                as_attachment=True,
                download_name=file[0]
            )
        return "Файл не найден."
    except Exception as e:
        return f"Ошибка: {e}"
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)