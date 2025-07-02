import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', postsHtml=posts)

# Add a new post
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

# Edit/update an existing post
@app.route('/<int:iD>/edit', methods=('GET', 'POST'))
def edit(iD):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE iD = ?', (iD,)).fetchone()

    if post is None:
        conn.close()
        return "Post not found!", 404

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        conn.execute('UPDATE posts SET title = ?, content = ? WHERE iD = ?', (title, content, iD))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', post=post)

# Delete a post
@app.route('/<int:iD>/delete', methods=('POST',))
def delete(iD):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE iD = ?', (iD,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
