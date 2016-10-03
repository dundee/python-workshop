import json

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

PORT = 9000


@Request.application
def receive_message(request):
    content = request.get_data().decode('utf-8')
    content = json.loads(content)

    print('Prisla zprava od {}: {}'.format(content['user_name'], content['message']))
    return Response('OK')


def run_server():
    run_simple('localhost', PORT, receive_message)
