"""The primary module for this skeleton application."""
import click
from gevent.wsgi import WSGIServer
from werkzeug.serving import run_with_reloader
from kalerator.web.app import app


def run_server():
    app.debug = True
    ws = WSGIServer(listener=('0.0.0.0', 6543), application=app)
    print(' * Listening on http://0.0.0.0:6543/')
    ws.serve_forever()



@click.command()
def main():
    run_server()

if __name__ == '__main__':
    main()
