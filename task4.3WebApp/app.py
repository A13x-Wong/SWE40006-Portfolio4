from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DATABASE = "expenses.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db_connection()

    expenses = conn.execute(
        "SELECT * FROM expenses ORDER BY id DESC"
    ).fetchall()

    total = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM expenses"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )


@app.route("/add", methods=["POST"])
def add_expense():
    description = request.form["description"]
    category = request.form["category"]
    amount = request.form["amount"]

    if description and category and amount:
        conn = get_db_connection()

        conn.execute(
            "INSERT INTO expenses (description, category, amount) VALUES (?, ?, ?)",
            (description, category, float(amount))
        )

        conn.commit()
        conn.close()

    return redirect(url_for("index"))


@app.route("/delete/<int:id>", methods=["POST"])
def delete_expense(id):
    conn = get_db_connection()

    conn.execute(
        "DELETE FROM expenses WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )