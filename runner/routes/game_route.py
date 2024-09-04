from flask import Blueprint

from runner.handlers.demohandler import demoHandler

game_handlers = {
    'domo_api': demoHandler
}

game_bp = Blueprint('demo_app', __name__, url_prefix='/runner')
for prefix, handler in game_handlers.items():
    game_bp.add_url_rule(f'{prefix}/<string:action>',
                         view_func=handler.as_view(prefix))
