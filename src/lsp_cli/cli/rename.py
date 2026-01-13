from pathlib import Path
from typing import Annotated

import typer
from lsap.schema.rename import (
    RenameExecuteRequest,
    RenameExecuteResponse,
    RenamePreviewRequest,
    RenamePreviewResponse,
)

from lsp_cli.utils.sync import cli_syncify

from . import options as op
from .shared import create_locate, managed_client, print_resp

app = typer.Typer(name="rename", help="Rename a symbol at a specific location.")


@app.command("preview")
@cli_syncify
async def rename_preview(
    new_name: Annotated[str, typer.Argument(help="The new name for the symbol.")],
    locate: op.LocateOpt,
):
    """
    Preview the effects of renaming a symbol at a specific location.
    """

    locate_obj = create_locate(locate)

    async with managed_client(locate_obj.file_path) as client:
        resp_obj = await client.post(
            "/capability/rename/preview",
            RenamePreviewResponse,
            json=RenamePreviewRequest(locate=locate_obj, new_name=new_name),
        )

        if resp_obj:
            print_resp(resp_obj)
        else:
            print("Warning: No rename possibilities found at the location")


@app.command("execute")
@cli_syncify
async def rename_execute(
    rename_id: Annotated[
        str, typer.Argument(help="Rename ID from a previous preview.")
    ],
    exclude: Annotated[
        list[str] | None,
        typer.Option(
            "--exclude",
            help="File paths or glob patterns to exclude from the rename operation. Can be specified multiple times.",
        ),
    ] = None,
    workspace: op.WorkspaceOpt = None,
):
    """
    Execute a rename operation using the ID from a previous preview.
    """
    if workspace is None:
        workspace = Path.cwd()

    async with managed_client(workspace) as client:
        resp_obj = await client.post(
            "/capability/rename/execute",
            RenameExecuteResponse,
            json=RenameExecuteRequest(
                rename_id=rename_id,
                exclude_files=exclude or [],
            ),
        )

        if resp_obj:
            print_resp(resp_obj)
        else:
            raise RuntimeError("Failed to execute rename")
