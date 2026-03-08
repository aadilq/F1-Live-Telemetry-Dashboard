import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src')) ##inserts a path to the src/ folders to find layout.py

import dash
from layout import create_layout
from callbacks import register_callbacks

app = dash.Dash(__name__)
app.layout = create_layout()
register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)
