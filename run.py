# run.py
'''from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
'''
# run.py
import os
import sys
from app import create_app

# Add the directory containing 'app' to the Python path if needed
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
