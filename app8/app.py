from flask import Flask, render_template, request, redirect, url_for
from bd_config import get_db_connection
import psycopg2
import psycopg2.extras

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM post ORDER BY created DESC;")
        posts = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html', posts=posts)
    except Exception as ex:
        # For debugging purposes, you might want to print the exception
        print(ex)
        return render_template('index.html', posts=[])

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if title and content:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO post (title, content) VALUES (%s, %s)",
                        (title, content))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM post WHERE id = %s", (id,))
    post = cur.fetchone()
    cur.close()
    conn.close()

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if title and content:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("UPDATE post SET title = %s, content = %s WHERE id = %s",
                        (title, content, id))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM post WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
