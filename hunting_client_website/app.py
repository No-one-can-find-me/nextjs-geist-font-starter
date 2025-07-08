from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hunting_client.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    admin_reply = db.Column(db.Text, nullable=True)
    reply_timestamp = db.Column(db.DateTime, nullable=True)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comments')
def comments():
    comments = Comment.query.order_by(Comment.timestamp.desc()).all()
    return render_template('comments.html', comments=comments)

@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    username = request.form['username']
    email = request.form.get('email', '')
    message = request.form['message']
    
    new_comment = Comment(username=username, email=email, message=message)
    db.session.add(new_comment)
    db.session.commit()
    
    flash('Your comment has been submitted successfully!', 'success')
    return redirect(url_for('comments'))

@app.route('/admin')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin_login', methods=['POST'])
def admin_login_post():
    username = request.form['username']
    password = request.form['password']
    
    # Simple admin check (in production, use proper password hashing)
    if username == 'admin' and password == 'admin123':
        session['admin_logged_in'] = True
        return redirect(url_for('admin_panel'))
    else:
        flash('Invalid credentials!', 'error')
        return redirect(url_for('admin_login'))

@app.route('/admin_panel')
def admin_panel():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    comments = Comment.query.order_by(Comment.timestamp.desc()).all()
    return render_template('admin_panel.html', comments=comments)

@app.route('/admin_reply/<int:comment_id>', methods=['POST'])
def admin_reply(comment_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    reply = request.form['reply']
    comment = Comment.query.get_or_404(comment_id)
    comment.admin_reply = reply
    comment.reply_timestamp = datetime.utcnow()
    db.session.commit()
    
    flash('Reply added successfully!', 'success')
    return redirect(url_for('admin_panel'))

@app.route('/admin_logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
