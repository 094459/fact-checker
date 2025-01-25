from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.fact import Fact
from models.category import Category
from models.vote import Vote
from models.user import User
from extensions import db
from datetime import datetime

fact_routes = Blueprint('facts', __name__)

@fact_routes.route('/')
@fact_routes.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))
    
    facts = Fact.query.order_by(Fact.created_at.desc()).all()
    categories = Category.query.all()
    return render_template('facts/dashboard.html', facts=facts, categories=categories)

@fact_routes.route('/facts/create', methods=['GET', 'POST'])
def create():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        source_url = request.form['source_url']
        category_id = request.form['category_id']
        
        fact = Fact(
            title=title,
            content=content,
            source_url=source_url,
            user_id=session['user_id'],
            category_id=category_id
        )
        db.session.add(fact)
        db.session.commit()
        
        flash('Fact created successfully!')
        return redirect(url_for('facts.dashboard'))
    
    categories = Category.query.all()
    return render_template('facts/create.html', categories=categories)

@fact_routes.route('/facts/<int:fact_id>')
def view(fact_id):
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))
    
    fact = Fact.query.get_or_404(fact_id)
    user_vote = Vote.query.filter_by(fact_id=fact_id, user_id=session['user_id']).first()
    vote_history = Vote.query.filter_by(fact_id=fact_id).order_by(Vote.created_at.desc()).all()
    return render_template('facts/view.html', fact=fact, user_vote=user_vote, vote_history=vote_history)

@fact_routes.route('/facts/<int:fact_id>/vote', methods=['POST'])
def vote(fact_id):
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))
    
    vote_type = request.form['vote_type']
    supporting_info = request.form.get('supporting_info')
    
    if vote_type not in ['Fact', 'Fake']:
        flash('Invalid vote type')
        return redirect(url_for('facts.view', fact_id=fact_id))
    
    existing_vote = Vote.query.filter_by(
        fact_id=fact_id,
        user_id=session['user_id']
    ).first()
    
    if existing_vote:
        existing_vote.vote_type = vote_type
        if supporting_info:
            existing_vote.supporting_info = supporting_info
    else:
        new_vote = Vote(
            fact_id=fact_id,
            user_id=session['user_id'],
            vote_type=vote_type,
            supporting_info=supporting_info
        )
        db.session.add(new_vote)
    
    db.session.commit()
    flash('Your vote has been recorded!')
    return redirect(url_for('facts.view', fact_id=fact_id))

@fact_routes.route('/categories/create', methods=['GET', 'POST'])
def create_category():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        
        flash('Category created successfully!')
        return redirect(url_for('facts.dashboard'))
    
    return render_template('facts/create_category.html')