from unittest import TestLoader, runner
import click
from app import app

@click.group()
def c():
    ...

@c.command()
def runserver():
    app.run(debug=True)

@c.command()
def tests():
    loader = TestLoader()
    test = loader.discover('tests/')
    testrunner = runner.TextTestRunner()
    testrunner.run(test)
