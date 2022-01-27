import os 
from .base import * 

if os.environ.get('blog_site') == 'production':
	from .production import * 
else: 
	from .development import * 
	