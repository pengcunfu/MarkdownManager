from app import config
from app.pygments_css import generate_style

config.IS_TEST = True
generate_style()
