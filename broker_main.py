import sys

import click

from broker import MajorDomoBroker

@click.command()
@click.option("--port", default=6789, help="Port where for the broker.")
def main(port):
    """create and start new broker"""
    verbose = '-v' in sys.argv
    broker = MajorDomoBroker(verbose)
    broker.bind(f"tcp://*:{port}")
    broker.mediate()

if __name__ == '__main__':
    main()