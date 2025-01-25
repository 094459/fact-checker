from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models.fact import Fact
from models.category import Category
from models.vote import Vote
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return redirect(url_for('main.dashboard'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    facts = Fact.query.all()
    return render_template('main/dashboard.html', facts=facts)

@main_bp.route('/fact/new', methods=['GET', 'POST'])
@login_required
def create_fact():
    if request.method == 'POST':
        content = request.form.get('content')
        category_id = request.form.get('category_id')
        supporting_url = request.form.get('supporting_url')
        supporting_info = request.form.get('supporting_info')
        
        fact = Fact(
            user_id=current_user.user_id,
            category_id=category_id,
            content=content,
            supporting_url=supporting_url,
            supporting_info=supporting_info
        )
        
        db.session.add(fact)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    
    categories = Category.query.all()
    return render_template('main/create_fact.html', categories=categories)

@main_bp.route('/fact/<int:fact_id>')
@login_required
def view_fact(fact_id):
    fact = Fact.query.get_or_404(fact_id)
    return render_template('main/view_fact.html', fact=fact)

@main_bp.route('/fact/<int:fact_id>/vote', methods=['POST'])
@login_required
def vote_fact(fact_id):
    vote_type = request.form.get('vote_type')
    if vote_type not in ['FACT', 'FAKE']:
        flash('Invalid vote type')
        return redirect(url_for('main.view_fact', fact_id=fact_id))
    
    existing_vote = Vote.query.filter_by(
        fact_id=fact_id,
        user_id=current_user.user_id
    ).first()
    
    if existing_vote:
        existing_vote.vote_type = vote_type
    else:
        vote = Vote(
            fact_id=fact_id,
            user_id=current_user.user_id,
            vote_type=vote_type
        )
        db.session.add(vote)
    
    db.session.commit()
    return redirect(url_for('main.view_fact', fact_id=fact_id))

@main_bp.route('/category/new', methods=['GET', 'POST'])
@login_required
def create_category():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        
        if Category.query.filter_by(name=name).first():
            flash('Category already exists')
            return redirect(url_for('main.create_category'))
        
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    
    return render_template('main/create_category.html')