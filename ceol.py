#!/usr/bin/python

import click
from utils import TelnetClient, format_response

@click.group()
@click.option('--ip', default="192.168.0.11", help='IP address', show_default=True)
@click.pass_context
def cli(ctx, ip):
    ctx.ensure_object(dict)
    ctx.obj['ip'] = ip
    ctx.obj['telnet_client'] = TelnetClient(ip)


# @click.group()
# @click.option('--debug/--no-debug', default=False)
# def cli(debug=False):
#     click.echo(f"Debug mode is {'on' if debug else 'off'}")


@cli.command(short_help='send raw command')
@click.argument('command', required=True, type=click.STRING)
@click.pass_context
def send(ctx, command):
    """Send over Telnet the given command and print response."""
    response = ctx.obj['telnet_client'].request(command)
    click.echo(format_response(response))
    click.echo('')




# @cli.command()
# def standby(ip="192.168.0.11"):
#     telnet = TelnetClient(ip)
#     response = telnet.request("PWSTANDBY")
#     print(format_response(response))


if __name__ == '__main__':
    # click.echo('main')
    cli(obj={})