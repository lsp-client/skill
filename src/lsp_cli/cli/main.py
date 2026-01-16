import typer

from lsp_cli.utils.debug import setup_debug

from . import options as op


def main_callback(
    ctx: typer.Context,
    debug: op.DebugOpt = False,
) -> None:
    setup_debug(debug)

    ctx.ensure_object(dict)
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())
        raise typer.Exit
