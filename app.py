
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('orphanage.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    conn = get_db_connection()

    counts = {
        'children': conn.execute(
            'SELECT COUNT(*) FROM Children'
        ).fetchone()[0],

        'supervisors': conn.execute(
            'SELECT COUNT(*) FROM Supervisors'
        ).fetchone()[0],

        'donations': conn.execute(
            'SELECT COUNT(*) FROM Donations'
        ).fetchone()[0],

        'visits': conn.execute(
            'SELECT COUNT(*) FROM Visits'
        ).fetchone()[0]
    }

    conn.close()

    return render_template('index.html', counts=counts)


@app.route('/children', methods=['GET', 'POST'])
def children_page():
    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form['Child_Name']
        birth = request.form['Birth_Date']
        gender = request.form['Gender']
        health = request.form['Health_Status']
        supervisor_id = request.form['Supervisor_ID']

        conn.execute("""
            INSERT INTO Children
            (Child_Name, Birth_Date, Gender, Health_Status, Supervisor_ID)
            VALUES (?, ?, ?, ?, ?)
        """, (name, birth, gender, health, supervisor_id))

        conn.commit()

    children = conn.execute('SELECT * FROM Children').fetchall()
    supervisors = conn.execute('SELECT * FROM Supervisors').fetchall()

    conn.close()

    return render_template(
        'children.html',
        children=children,
        supervisors=supervisors
    )

@app.route('/supervisors', methods=['GET', 'POST'])
def supervisors_page():
    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form['Name']
        phone = request.form['Phone']

        conn.execute(
            'INSERT INTO Supervisors (Name, Phone) VALUES (?, ?)',
            (name, phone)
        )
        conn.commit()

    supervisors = conn.execute(
        'SELECT * FROM Supervisors'
    ).fetchall()

    conn.close()

    return render_template('supervisors.html', supervisors=supervisors)


@app.route('/health', methods=['GET', 'POST'])
def health_page():
    conn = get_db_connection()

    if request.method == 'POST':
        child_id = request.form['Child_ID']
        record_date = request.form['Record_Date']
        diagnosis = request.form['Diagnosis']
        treatment = request.form['Treatment']

        conn.execute("""
            INSERT INTO Medical_Records
            (Child_ID, Record_Date, Diagnosis, Treatment)
            VALUES (?, ?, ?, ?)
        """, (child_id, record_date, diagnosis, treatment))

        conn.commit()

    medical_records = conn.execute(
        'SELECT * FROM Medical_Records'
    ).fetchall()

    conn.close()

    return render_template(
        'health.html',
        medical_records=medical_records
    )


@app.route('/education', methods=['GET', 'POST'])
def education_page():
    conn = get_db_connection()

    if request.method == 'POST':
        child_id = request.form['Child_ID']
        grade = request.form['Grade']
        academic_year = request.form['Academic_Year']
        result = request.form['Result']

        conn.execute("""
            INSERT INTO Education
            (Child_ID, Grade, Academic_Year, Result)
            VALUES (?, ?, ?, ?)
        """, (child_id, grade, academic_year, result))

        conn.commit()

    education = conn.execute(
        'SELECT * FROM Education'
    ).fetchall()

    conn.close()

    return render_template(
        'education.html',
        education=education
    )

@app.route('/donors', methods=['GET', 'POST'])
def donors_page():
    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form['Name']
        phone = request.form['Phone']

        conn.execute(
            'INSERT INTO Donors (Name, Phone) VALUES (?, ?)',
            (name, phone)
        )
        conn.commit()

    donors = conn.execute(
        'SELECT * FROM Donors'
    ).fetchall()

    conn.close()

    return render_template(
        'donors.html',
        donors=donors
    )

@app.route('/donations', methods=['GET', 'POST'])
def donations_page():
    conn = get_db_connection()

    if request.method == 'POST':
        donor_id = request.form['Donor_ID']
        amount = request.form['Amount']
        donation_date = request.form['Donation_Date']

        conn.execute("""
            INSERT INTO Donations (Donor_ID, Amount, Donation_Date)
            VALUES (?, ?, ?)
        """, (donor_id, amount, donation_date))

        conn.commit()

    donations = conn.execute(
        'SELECT * FROM Donations'
    ).fetchall()

    conn.close()

    return render_template(
        'donations.html',
        donations=donations
    )

@app.route('/visitors', methods=['GET', 'POST'])
def visitors_page():
    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form['Name']
        phone = request.form['Phone']

        conn.execute(
            'INSERT INTO Visitors (Name, Phone) VALUES (?, ?)',
            (name, phone)
        )
        conn.commit()

    visitors = conn.execute(
        'SELECT * FROM Visitors'
    ).fetchall()

    conn.close()

    return render_template(
        'visitors.html',
        visitors=visitors
    )

@app.route('/visits', methods=['GET', 'POST'])
def visits_page():
    conn = get_db_connection()

    if request.method == 'POST':
        visitor_id = request.form['Visitor_ID']
        child_id = request.form['Child_ID']
        visit_date = request.form['Visit_Date']
        notes = request.form['Notes']

        conn.execute("""
            INSERT INTO Visits
            (Visitor_ID, Child_ID, Visit_Date, Notes)
            VALUES (?, ?, ?, ?)
        """, (visitor_id, child_id, visit_date, notes))

        conn.commit()

    visits = conn.execute(
        'SELECT * FROM Visits'
    ).fetchall()

    conn.close()

    return render_template(
        'visits.html',
        visits=visits
    )

if __name__ == '__main__':
    app.run(debug=True)

