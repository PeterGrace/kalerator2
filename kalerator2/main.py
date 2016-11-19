import argparse
import json
import os
import sys

from kalerator.keyboard import Keyboard

def write_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

def main(filename, flag_free=False, flag_paid=False):
    with open(filename) as file:
        data = json.load(file)

    (root, ext) = os.path.splitext(filename)
   
    if flag_free:
        free_board_fn = '{0}{1}.{2}'.format(root, '-board-free', '.scr')
        free_schm_fn = '{0}{1}.{2}'.format(root, '-schm-free', '.scr')
        k_free = Keyboard(filename, flag_free)
        write_file(free_board_fn, k_free.board_scr())
        write_file(free_schm_fn, k_free.schematic_scr())

    if flag_paid:
        paid_board_fn = '{0}{1}.{2}'.format(root, '-board-paid', '.scr')
        paid_schm_fn = '{0}{1}.{2}'.format(root, '-schm-paid', '.scr')
        k_paid = Keyboard(filename, flag_paid)
        write_file(paid_board_fn, k_paid.board_scr())
        write_file(paid_schm_fn, k_paid.schematic_scr())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('free', action='store_true', default=False)
    parser.add_argument('paid', action='store_true', default=False)
    args = parser.parse_args()

    if not args.filename:
        print('Require --filename for input json; output files will be (rootname).json -> (rootname)-{board|schm}-{free|paid}.scr')
        sys.exit(1)

    if not (args.free or args.paid):
        print('Was given nothing to do, require --free or --paid.')
        sys.exit(1)

    sys.exit(main(args.filename, args.free, args.paid))
