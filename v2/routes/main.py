from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models.fact import Fact, Category, Vote
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return redirect(url_for('main.dashboard'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    facts = Fact.query.order_by(Fact.created_at.desc()).all()
    return render_template('main/dashboard.html', facts=facts)

@main_bp.route('/fact/new', methods=['GET', 'POST'])
@login_required
def create_fact():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        category_id = request.form.get('category_id')
        
        fact = Fact(title=title, content=content, 
                   category_id=category_id, user_id=current_user.id)
        db.session.add(fact)
        db.session.commit()
        
        return redirect(url_for('main.dashboard'))
    
    categories = Category.query.all()
    return render_template('main/create_fact.html', categories=categories)

@main_bp.route('/category/new', methods=['GET', 'POST'])
@login_required
def create_category():
    if request.method == 'POST':
        name = request.form.get('name')
        
        if Category.query.filter_by(name=name).first():
            flash('Category already exists')
            return redirect(url_for('main.create_category'))
        
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        
        return redirect(url_for('main.dashboard'))
    
    return render_template('main/create_category.html')

@main_bp.route('/fact/<int:fact_id>')
@login_required
def view_fact(fact_id):
    fact = Fact.query.get_or_404(fact_id)
    return render_template('main/view_fact.html', fact=fact)

@main_bp.route('/fact/<int:fact_id>/vote', methods=['POST'])
@login_required
def vote(fact_id):
    is_fact = request.form.get('is_fact') == 'true'
    supporting_info = request.form.get('supporting_info')
    
    # Check if user has already voted
    existing_vote = Vote.query.filter_by(
        fact_id=fact_id, 
        user_id=current_user.id
    ).first()
    
    if existing_vote:
        existing_vote.is_fact = is_fact
        existing_vote.supporting_info = supporting_info
    else:
        vote = Vote(
            is_fact=is_fact,
            supporting_info=supporting_info,
            fact_id=fact_id,
            user_id=current_user.id
        )
        db.session.add(vote)
    
    db.session.commit()
    return redirect(url_for('main.view_fact', fact_id=fact_id))