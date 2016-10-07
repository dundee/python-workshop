import json

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from .model import Messages


def run_server(config: dict, messages: Messages):

    @Request.application
    def receive_message(request):
        content = request.get_data().decode('utf-8')
        message = json.loads(content)
        messages.add(message)
        return Response('OK')

    run_simple('0.0.0.0', config['server']['port'], receive_message)
