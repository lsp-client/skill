from typing import Annotated

import typer

from lsp_cli.utils.debug import setup_debug


def main_callback(
    ctx: typer.Context,
    debug: Annotated[
        bool,
        typer.Option(
            "--debug",
            "-d",
            help="Enable verbose debug logging for troubleshooting.",
        ),
    ] = False,
) -> None:
    setup_debug(debug)

    ctx.ensure_object(dict)
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())
        raise typer.Exit
