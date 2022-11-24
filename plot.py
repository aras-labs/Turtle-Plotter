import argparse

from plotter.plotter import plotter
from functions.svg_reader import svg_reader
from functions.code_reader import code_reader
from functions.prop_reader import prop_reader

parser = argparse.ArgumentParser("Turtle Plotter")
parser.add_argument("-f", "--file", help="Input file.", required=True)
parser.add_argument("-t", "--type", choices=['code', 'svg'], help="Input type.", required=True)
opts, rem_args = parser.parse_known_args()
if opts.type == 'code':
    parser.add_argument("-c", "--config", help="Config file.", required=True)
parser.add_argument("--height", help="Height of the plot.", default=700)
parser.add_argument("--width", help="Width of the plot.", default=700)
args = parser.parse_args()


if __name__ == "__main__":
    if args.type == 'code':
        config = prop_reader(file_name=args.config)
        points = code_reader(filename=args.file, config=config)
    elif args.type == 'svg':
        points = svg_reader(filename=args.file)

    plotter(h=args.height, w=args.width, points=points)