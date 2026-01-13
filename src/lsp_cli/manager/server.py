from __future__ import annotations

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from functools import cached_property
from pathlib import Path
from typing import Self, final, override

import httpx
from attrs import define
from lsp_client.jsonrpc.types import (
    RawNotification,
    RawRequest,
    RawResponsePackage,
)
from lsp_client.server import Server, ServerRuntimeError
from lsp_client.server.types import ServerRequest
from lsp_client.utils.channel import Sender
from lsp_client.utils.workspace import Workspace

from lsp_cli.utils.socket import wait_socket


@final
@define
class ManagerServer(Server):
    uds_path: Path

    @cached_property
    def client(self) -> httpx.AsyncClient:
        transport = httpx.AsyncHTTPTransport(uds=self.uds_path.as_posix())
        return httpx.AsyncClient(
            transport=transport,
            base_url="http://localhost",
            timeout=None,
        )

    @override
    async def check_availability(self) -> None:
        if not self.uds_path.exists():
            raise ServerRuntimeError(self, f"Server socket not found: {self.uds_path}")
        try:
            await self.client.get("/health")
        except httpx.HTTPError as e:
            raise ServerRuntimeError(
                self, f"Managed server at {self.uds_path} is not responding: {e}"
            ) from e

    @override
    async def request(self, request: RawRequest) -> RawResponsePackage:
        response = await self.client.post("/request", json=request)
        response.raise_for_status()
        return response.json()

    @override
    async def notify(self, notification: RawNotification) -> None:
        response = await self.client.post("/notify", json=notification)
        response.raise_for_status()

    @override
    async def kill(self) -> None:
        await self.client.post("/shutdown")

    async def wait_requests_completed(self, timeout: float | None = None) -> None:
        return

    @override
    @asynccontextmanager
    async def run(
        self, workspace: Workspace, sender: Sender[ServerRequest]
    ) -> AsyncGenerator[Self]:
        await wait_socket(self.uds_path, timeout=10.0)
        yield self
