from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .forms import LoginForm, SignupForm, EntryForm
from .models import User, Entry
from . import db, login_manager

from bson.objectid import ObjectId
from flask import abort

import json

main = Blueprint("main", __name__)

@login_manager.user_loader
def load_user(user_id):
    user_data = User.get_user_by_id(db, user_id)
    return User(user_data) if user_data else None

@main.route("/")
def home():
    return redirect(url_for("main.login"))

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_data = User.get_user_by_email(db, form.email.data)
        if user_data and check_password_hash(user_data["password"], form.password.data):
            user = User(user_data)
            login_user(user)
            return redirect(url_for("main.dashboard"))
        flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)

@main.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing = User.get_user_by_email(db, form.email.data)
        if existing:
            flash("Email already registered", "warning")
        else:
            hashed_pw = generate_password_hash(form.password.data)
            db.users.insert_one({
                "username": form.username.data,
                "email": form.email.data,
                "password": hashed_pw
            })
            flash("Account created. Please log in.", "success")
            return redirect(url_for("main.login"))
    return render_template("signup.html", form=form)

@main.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    form = EntryForm()
    if form.validate_on_submit():
        Entry.create_entry(db, current_user.id, form.title.data, form.content.data)
        flash("Entry saved!", "success")
        return redirect(url_for("main.dashboard"))

    entries = Entry.get_entries_by_user(db, current_user.id)
    return render_template("dashboard.html", form=form, entries=entries)

@main.route("/entry/<entry_id>/edit", methods=["GET", "POST"])
@login_required
def edit_entry(entry_id):
    entry = db.entries.find_one({"_id": ObjectId(entry_id), "user_id": current_user.id})
    if not entry:
        abort(404)

    form = EntryForm(data=entry)

    if form.validate_on_submit():
        db.entries.update_one(
            {"_id": ObjectId(entry_id)},
            {"$set": {"title": form.title.data, "content": form.content.data}}
        )
        flash("Entry updated!", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("entry_form.html", form=form, editing=True)

@main.route("/entry/<entry_id>/delete", methods=["POST"])
@login_required
def delete_entry(entry_id):
    result = db.entries.delete_one({"_id": ObjectId(entry_id), "user_id": current_user.id})
    if result.deleted_count == 1:
        flash("Entry deleted.", "info")
    else:
        flash("Entry not found or unauthorized.", "danger")
    return redirect(url_for("main.dashboard"))

@main.route('/calendar')
@login_required
def calendar():
    # Fetch entries from MongoDB
    entries = entries_collection.find({'user_id': ObjectId(current_user.id)})

    events = []
    for entry in entries:
        events.append({
            'title': entry.get('title', 'No Title'),
            'start': entry['timestamp'].strftime('%Y-%m-%d'),
            'url': url_for('main.edit_entry', entry_id=entry['_id'])  # or view_entry if you prefer
        })

    return render_template('calendar.html', events=events)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))
