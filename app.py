# ====================================================================
# Main Application Controller Layer - WealthPath Project
# Architecture: Procedural-Functional Core Pattern for clear code evaluation
# ====================================================================

from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Centralized Driver Utility Function for MySQL Interactions
def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    if 'admin_logged_in' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# --- AUTHENTICATION ENGINE ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        
        conn = get_db_connection()
        try:
            with conn.cursor() as cursor:
                # Parameterized SQL query execution path defending against SQL Injection vulnerabilities
                query = "SELECT email, role FROM users WHERE email = %s AND password = %s"
                cursor.execute(query, (email, password))
                user = cursor.fetchone()
                
                if user:
                    session['admin_logged_in'] = True
                    session['admin_email'] = user['email']
                    session['admin_role'] = user['role']
                    flash('Authentication verified successfully.', 'success')
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid system administrative credentials.', 'danger')
        except Exception as e:
            flash(f"Database Connectivity Interrupted: {str(e)}", "danger")
        finally:
            conn.close()
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Administrative session terminated successfully.', 'info')
    return redirect(url_for('login'))

# --- CENTRAL EXECUTIVE DASHBOARD ---
@app.route('/dashboard')
def dashboard():
    if 'admin_logged_in' not in session:
        flash('Unauthorized system access intercept. Please login.', 'warning')
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            # Metric 1: Total Registered Unique Clients
            cursor.execute("SELECT COUNT(*) as client_count FROM clients")
            total_clients = cursor.fetchone()['client_count']
            
            # Metric 2: Total Investment Lines Configured
            cursor.execute("SELECT COUNT(*) as asset_count FROM investments")
            total_investments = cursor.fetchone()['asset_count']
            
            # Metric 3: Count of Active System Advisors (Simulated naturally from configuration user metrics)
            cursor.execute("SELECT COUNT(*) as user_count FROM users")
            active_advisors = cursor.fetchone()['user_count']
    except Exception as e:
        total_clients, total_investments, active_advisors = 0, 0, 0
        flash(f"Error fetching dashboard metrics: {str(e)}", "danger")
    finally:
        conn.close()
        
    return render_template(
        'dashboard.html', 
        total_clients=total_clients, 
        total_investments=total_investments,
        active_advisors=active_advisors
    )

# --- CLIENT PROVISIONING OPERATIONS ---
@app.route('/clients', methods=['GET', 'POST'])
def clients():
    if 'admin_logged_in' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        email = request.form.get('email', '').strip()
        city = request.form.get('city', '').strip()
        
        if name and phone and email and city:
            try:
                with conn.cursor() as cursor:
                    insert_query = "INSERT INTO clients (name, phone, email, city) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_query, (name, phone, email, city))
                    conn.commit()
                    flash(f'Client record for "{name}" instantiated successfully.', 'success')
            except Exception as e:
                flash(f'Constraint Violated / Storage Exception: {str(e)}', 'danger')
        else:
            flash('All client tracking fields are strictly required.', 'warning')
            
    # Process View/Render phase tracking records
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clients ORDER BY id DESC")
            client_dataset = cursor.fetchall()
    finally:
        conn.close()
        
    return render_template('clients.html', clients=client_dataset)

@app.route('/delete-client/<int:id>')
def delete_client(id):
    if 'admin_logged_in' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            delete_query = "DELETE FROM clients WHERE id = %s"
            cursor.execute(delete_query, (id,))
            conn.commit()
            flash('Target Client mapping cleanly purged from structural context.', 'success')
    except Exception as e:
        flash(f'Cascade or Reference constraint failure: {str(e)}', 'danger')
    finally:
        conn.close()
    return redirect(url_for('clients'))

# --- INVESTMENT BALANCING PORTFOLIO OPERATIONS ---
@app.route('/investments', methods=['GET', 'POST'])
def investments():
    if 'admin_logged_in' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    if request.method == 'POST':
        client_name = request.form.get('client_name', '').strip()
        investment_type = request.form.get('investment_type', '').strip()
        amount = request.form.get('amount', '0').strip()
        risk_level = request.form.get('risk_level', 'Moderate').strip()
        
        if client_name and investment_type and amount:
            try:
                with conn.cursor() as cursor:
                    insert_query = "INSERT INTO investments (client_name, investment_type, amount, risk_level) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_query, (client_name, investment_type, float(amount), risk_level))
                    conn.commit()
                    flash('Investment allocation validated and stored in cloud register.', 'success')
            except Exception as e:
                flash(f'Execution Fault Logging Capital Position: {str(e)}', 'danger')
        else:
            flash('Required structural asset data is incomplete.', 'warning')
            
    # Compile dynamic asset array rendering pipeline
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM investments ORDER BY id DESC")
            investment_dataset = cursor.fetchall()
    finally:
        conn.close()
        
    return render_template('investments.html', investments=investment_dataset)

@app.route('/delete-investment/<int:id>')
def delete_investment(id):
    if 'admin_logged_in' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            delete_query = "DELETE FROM investments WHERE id = %s"
            cursor.execute(delete_query, (id,))
            conn.commit()
            flash('Financial asset transaction ledger mapping revoked.', 'success')
    except Exception as e:
        flash(f'Database operation failed: {str(e)}', 'danger')
    finally:
        conn.close()
    return redirect(url_for('investments'))

if __name__ == '__main__':
    # Binding cleanly over 0.0.0.0 enables AWS EC2 Security Groups integration visibility natively
    app.run(host='0.0.0.0', port=5002, debug=True)