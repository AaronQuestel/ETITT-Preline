# blue prints are imported 
# explicitly instead of using *
from .auth import auth_views_bp

views = [auth_views_bp] 
# blueprints must be added to this list