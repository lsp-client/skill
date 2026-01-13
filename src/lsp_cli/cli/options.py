from pathlib import Path
from typing import Annotated

import typer

LocateOpt = Annotated[
    str,
    typer.Option(
        "--locate",
        "-L",
        help="Location string (see 'lsp locate --help' for syntax).",
    ),
]

WorkspaceOpt = Annotated[
    Path | None,
    typer.Option(
        "--workspace",
        "-w",
        help="Path to workspace. Defaults to current directory.",
    ),
]

MaxItemsOpt = Annotated[
    int | None,
    typer.Option(
        "--max-items",
        "-n",
        help="Max items to return",
    ),
]

StartIndexOpt = Annotated[
    int,
    typer.Option(
        "--start-index",
        "-i",
        help="Pagination offset",
    ),
]

PaginationIdOpt = Annotated[
    str | None,
    typer.Option(
        "--pagination-id",
        "-p",
        help="Pagination token",
    ),
]
