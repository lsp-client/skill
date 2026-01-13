import uvicorn

from lsp_cli.settings import MANAGER_UDS_PATH

from .manager import app

if __name__ == "__main__":
    MANAGER_UDS_PATH.unlink(missing_ok=True)
    MANAGER_UDS_PATH.parent.mkdir(parents=True, exist_ok=True)
    uvicorn.run(app, uds=str(MANAGER_UDS_PATH))
