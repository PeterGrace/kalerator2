import os
import click
import logging
import json
import six

if six.PY3:
    from kalerator2.kalerator.keyboard import Keyboard
elif six.PY2:
    from kalerator.keyboard import Keyboard

logging.basicConfig(level=logging.DEBUG)


def write_file(filename, data):
    print('Writing "{0}"'.format(filename))
    with open(filename, 'wb') as f:
        try:
            f.write(data)
        except TypeError:
            f.write(data.encode('utf-8'))


@click.command()
@click.argument('filename')
@click.option('--free/--paid', default=False, help="Generate EAGLE files for free edition or paid edition")
def main(filename, free):
    with open(filename) as file:
        data = json.load(file)

    (root, ext) = os.path.splitext(filename)

    if free is True:
        board_fn = ''.join([root, '-board-free', '.scr'])
        schm_fn = ''.join([root, '-schm-free', '.scr'])
        k = Keyboard(data, (free is True))
    else:
        board_fn = ''.join([root, '-board-paid', '.scr'])
        schm_fn = ''.join([root, '-schm-paid', '.scr'])
        k = Keyboard(data, (free is False))

    write_file(board_fn, k.board_scr)
    write_file(schm_fn, k.schematic_scr)

if __name__ == '__main__':
    main()
