"""
Test basic usability for each supported language.

This module tests that LSP CLI works correctly with all supported languages:
- Python
- Go
- Rust
- TypeScript
- JavaScript
- Deno

Each test verifies that the CLI can:
1. Start a language server for the project
2. List the running server
3. Stop the server cleanly
"""

from pathlib import Path

import pytest
from conftest import BaseLSPTest


@pytest.fixture(scope="module")
def fixtures_dir():
    """Return the path to the test fixtures directory."""
    return Path(__file__).parent / "fixtures"


class TestLanguageSupport(BaseLSPTest):
    """Test that each supported language works with LSP CLI."""

    def test_python_support(self, fixtures_dir):
        """Test basic LSP operations with Python project."""
        # Use the actual source code as a Python project
        python_file = fixtures_dir.parent.parent / "src" / "lsp_cli" / "__init__.py"
        assert python_file.exists(), "Python test file does not exist"

        try:
            # Start server
            result = self.run_lsp_command("server", "start", str(python_file))
            assert result.returncode == 0, (
                f"Failed to start Python server: {result.stderr}"
            )

            # List servers - should show Python server
            result = self.run_lsp_command("server", "list")
            assert result.returncode == 0, f"Failed to list servers: {result.stderr}"
            assert "python" in result.stdout.lower(), "Python server not listed"
        finally:
            # Stop server
            result = self.run_lsp_command("server", "stop", str(python_file))
            assert result.returncode == 0, (
                f"Failed to stop Python server: {result.stderr}"
            )

    def test_go_support(self, fixtures_dir):
        """Test basic LSP operations with Go project."""
        go_file = fixtures_dir / "go_project" / "main.go"
        assert go_file.exists(), "Go test file does not exist"

        try:
            # Start server
            result = self.run_lsp_command("server", "start", str(go_file))
            assert result.returncode == 0, f"Failed to start Go server: {result.stderr}"

            # List servers - should show Go server
            result = self.run_lsp_command("server", "list")
            assert result.returncode == 0, f"Failed to list servers: {result.stderr}"
            assert "go" in result.stdout.lower(), "Go server not listed"
        finally:
            # Stop server
            result = self.run_lsp_command("server", "stop", str(go_file))
            assert result.returncode == 0, f"Failed to stop Go server: {result.stderr}"

    def test_rust_support(self, fixtures_dir):
        """Test basic LSP operations with Rust project."""
        rust_file = fixtures_dir / "rust_project" / "src" / "main.rs"
        assert rust_file.exists(), "Rust test file does not exist"

        try:
            # Start server
            result = self.run_lsp_command("server", "start", str(rust_file))
            assert result.returncode == 0, (
                f"Failed to start Rust server: {result.stderr}"
            )

            # List servers - should show Rust server
            result = self.run_lsp_command("server", "list")
            assert result.returncode == 0, f"Failed to list servers: {result.stderr}"
            assert "rust" in result.stdout.lower(), "Rust server not listed"
        finally:
            # Stop server
            result = self.run_lsp_command("server", "stop", str(rust_file))
            assert result.returncode == 0, (
                f"Failed to stop Rust server: {result.stderr}"
            )

    def test_typescript_support(self, fixtures_dir):
        """Test basic LSP operations with TypeScript project."""
        ts_file = fixtures_dir / "typescript_project" / "index.ts"
        assert ts_file.exists(), "TypeScript test file does not exist"

        try:
            # Start server
            result = self.run_lsp_command("server", "start", str(ts_file))
            assert result.returncode == 0, (
                f"Failed to start TypeScript server: {result.stderr}"
            )

            # List servers - should show TypeScript server
            result = self.run_lsp_command("server", "list")
            assert result.returncode == 0, f"Failed to list servers: {result.stderr}"
            # Note: TypeScript may be identified as "typescript" or abbreviated form
            # We check for both to handle different language server implementations
            stdout_lower = result.stdout.lower()
            assert "typescript" in stdout_lower or "tsserver" in stdout_lower, (
                f"TypeScript server not listed. Output: {result.stdout}"
            )
        finally:
            # Stop server
            result = self.run_lsp_command("server", "stop", str(ts_file))
            assert result.returncode == 0, (
                f"Failed to stop TypeScript server: {result.stderr}"
            )

    def test_javascript_support(self, fixtures_dir):
        """Test basic LSP operations with JavaScript project."""
        js_file = fixtures_dir / "javascript_project" / "index.js"
        assert js_file.exists(), "JavaScript test file does not exist"

        try:
            # Start server
            result = self.run_lsp_command("server", "start", str(js_file))
            assert result.returncode == 0, (
                f"Failed to start JavaScript server: {result.stderr}"
            )

            # List servers - should show JavaScript server
            result = self.run_lsp_command("server", "list")
            assert result.returncode == 0, f"Failed to list servers: {result.stderr}"
            # Note: JavaScript may be identified as "javascript" or abbreviated form
            # We check for both to handle different language server implementations
            stdout_lower = result.stdout.lower()
            assert "javascript" in stdout_lower or "jsserver" in stdout_lower, (
                f"JavaScript server not listed. Output: {result.stdout}"
            )
        finally:
            # Stop server
            result = self.run_lsp_command("server", "stop", str(js_file))
            assert result.returncode == 0, (
                f"Failed to stop JavaScript server: {result.stderr}"
            )

    def test_deno_support(self, fixtures_dir):
        """Test basic LSP operations with Deno project."""
        deno_file = fixtures_dir / "deno_project" / "main.ts"
        assert deno_file.exists(), "Deno test file does not exist"

        try:
            # Start server
            result = self.run_lsp_command("server", "start", str(deno_file))
            assert result.returncode == 0, (
                f"Failed to start Deno server: {result.stderr}"
            )

            # List servers - should show Deno server
            result = self.run_lsp_command("server", "list")
            assert result.returncode == 0, f"Failed to list servers: {result.stderr}"
            assert "deno" in result.stdout.lower(), "Deno server not listed"
        finally:
            # Always attempt to stop the server to avoid leaking processes
            stop_result = self.run_lsp_command("server", "stop", str(deno_file))
            assert stop_result.returncode == 0, (
                f"Failed to stop Deno server: {stop_result.stderr}"
            )


class TestLanguageServerLifecycle(BaseLSPTest):
    """Test language server lifecycle for all supported languages."""

    def test_multiple_language_servers(self, fixtures_dir):
        """Test running multiple language servers simultaneously."""
        # Start servers for different languages
        python_file = fixtures_dir.parent.parent / "src" / "lsp_cli" / "__init__.py"
        go_file = fixtures_dir / "go_project" / "main.go"
        rust_file = fixtures_dir / "rust_project" / "src" / "main.rs"

        servers = []
        try:
            if python_file.exists():
                result = self.run_lsp_command("server", "start", str(python_file))
                if result.returncode == 0:
                    servers.append(("python", python_file))

            if go_file.exists():
                result = self.run_lsp_command("server", "start", str(go_file))
                if result.returncode == 0:
                    servers.append(("go", go_file))

            if rust_file.exists():
                result = self.run_lsp_command("server", "start", str(rust_file))
                if result.returncode == 0:
                    servers.append(("rust", rust_file))

            # List should show multiple servers
            result = self.run_lsp_command("server", "list")
            assert result.returncode == 0, f"Failed to list servers: {result.stderr}"

            # Verify each started server is listed
            for lang, _ in servers:
                assert lang in result.stdout.lower(), f"{lang} server not found in list"
        finally:
            # Stop all servers
            for _, file_path in servers:
                result = self.run_lsp_command("server", "stop", str(file_path))
                assert result.returncode == 0, f"Failed to stop server for {file_path}"

    def test_language_server_reuse(self, fixtures_dir):
        """Test that starting a server twice reuses the same server."""
        python_file = fixtures_dir.parent.parent / "src" / "lsp_cli" / "__init__.py"
        assert python_file.exists(), "Python test file does not exist"

        server_started = False
        try:
            # Start server first time
            result1 = self.run_lsp_command("server", "start", str(python_file))
            assert result1.returncode == 0, (
                f"Failed to start server first time: {result1.stderr}"
            )
            server_started = True

            # Get server list
            list1 = self.run_lsp_command("server", "list")
            assert list1.returncode == 0

            # Start server second time (should reuse)
            result2 = self.run_lsp_command("server", "start", str(python_file))
            assert result2.returncode == 0, (
                f"Failed to start server second time: {result2.stderr}"
            )

            # Get server list again
            list2 = self.run_lsp_command("server", "list")
            assert list2.returncode == 0

            # Should have the same number of servers for this specific Python file
            python_file_str = str(python_file)
            python_servers1 = [
                line for line in list1.stdout.splitlines() if python_file_str in line
            ]
            python_servers2 = [
                line for line in list2.stdout.splitlines() if python_file_str in line
            ]
            assert len(python_servers1) == len(python_servers2), "Server was not reused"
        finally:
            # Cleanup
            if server_started:
                self.run_lsp_command("server", "stop", str(python_file))


class TestLanguageServerErrors(BaseLSPTest):
    """Test error handling for language servers."""

    def test_invalid_file_path(self):
        """Test that invalid file paths are handled gracefully."""
        invalid_file = Path("/nonexistent/path/file.py")

        # Invalid path should result in a non-zero exit code, not a successful run
        result = self.run_lsp_command("server", "start", str(invalid_file))
        assert result.returncode != 0, (
            "Expected non-zero exit code for invalid file path.\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )

    def test_unsupported_language(self, fixtures_dir):
        """Test that unsupported file types are handled gracefully."""
        # Create a temporary file with unsupported extension
        unsupported_file = fixtures_dir / "test.unsupported"
        unsupported_file.parent.mkdir(parents=True, exist_ok=True)
        unsupported_file.write_text("test content")

        try:
            # Should handle gracefully by returning a non-zero exit code
            result = self.run_lsp_command("server", "start", str(unsupported_file))
            # Unsupported file types should not start a server successfully
            assert result.returncode != 0, (
                f"Expected non-zero exit code for unsupported file type, "
                f"got {result.returncode}. stdout: {result.stdout!r} stderr: {result.stderr!r}"
            )
        finally:
            # Cleanup
            if unsupported_file.exists():
                unsupported_file.unlink()
