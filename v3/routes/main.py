from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models.fact import Fact, Category, Vote
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/dashboard')

def dashboard():
    facts = Fact.query.order_by(Fact.created_at.desc()).all()
    return render_template('main/dashboard.html', facts=facts)

@main_bp.route('/fact/new', methods=['GET', 'POST'])
@login_required
def create_fact():
    categories = Category.query.all()
    
    if request.method == 'POST':
        category_id = request.form.get('category_id')
        fact_text = request.form.get('fact_text')
        supporting_url = request.form.get('supporting_url')
        supporting_info = request.form.get('supporting_info')
        
        fact = Fact(
            user_id=current_user.user_id,
            category_id=category_id,
            fact_text=fact_text,
            supporting_url=supporting_url,
            supporting_info=supporting_info
        )
        
        db.session.add(fact)
        db.session.commit()
        
        flash('Fact created successfully!')
        return redirect(url_for('main.dashboard'))
    
    return render_template('main/create_fact.html', categories=categories)

@main_bp.route('/category/new', methods=['GET', 'POST'])
@login_required
def create_category():
    if request.method == 'POST':
        category_name = request.form.get('category_name')
        description = request.form.get('description')
        
        if Category.query.filter_by(category_name=category_name).first():
            flash('Category already exists')
            return redirect(url_for('main.create_category'))
        
        category = Category(category_name=category_name, description=description)
        db.session.add(category)
        db.session.commit()
        
        flash('Category created successfully!')
        return redirect(url_for('main.dashboard'))
    
    return render_template('main/create_category.html')

@main_bp.route('/fact/<int:fact_id>')
@login_required
def view_fact(fact_id):
    fact = Fact.query.get_or_404(fact_id)
    return render_template('main/view_fact.html', fact=fact)

@main_bp.route('/fact/<int:fact_id>/vote', methods=['POST'])
@login_required
def vote_fact(fact_id):
    fact = Fact.query.get_or_404(fact_id)
    is_true = request.form.get('vote') == 'true'
    
    existing_vote = Vote.query.filter_by(
        fact_id=fact_id,
        user_id=current_user.user_id
    ).first()
    
    if existing_vote:
        existing_vote.is_true = is_true
    else:
        vote = Vote(
            fact_id=fact_id,
            user_id=current_user.user_id,
            is_true=is_true
        )
        db.session.add(vote)
    
    db.session.commit()
    flash('Vote recorded successfully!')
    return redirect(url_for('main.view_fact', fact_id=fact_id))