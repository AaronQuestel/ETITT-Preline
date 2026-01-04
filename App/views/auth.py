#region IMPORTS 
from flask import Blueprint, render_template, request, url_for, redirect, flash, current_app
#endregion

auth_views_bp = Blueprint('auth_views', __name__, template_folder='/templates')

@auth_views_bp.route('/', methods=['GET', 'POST'])
def login():
   return render_template('navigation.html')
