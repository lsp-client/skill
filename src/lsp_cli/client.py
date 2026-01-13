from pathlib import Path
from typing import NamedTuple

from lsp_client.client import Client
from lsp_client.clients.lang import lang_clients


class TargetClient(NamedTuple):
    project_path: Path
    client_cls: type[Client]


def find_client(path: Path) -> TargetClient | None:
    candidates = lang_clients.values()

    for client_cls in candidates:
        lang_config = client_cls.get_language_config()
        if root := lang_config.find_project_root(path):
            return TargetClient(project_path=root, client_cls=client_cls)
