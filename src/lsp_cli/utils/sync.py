from functools import partial

from asyncer import syncify

cli_syncify = partial(syncify, raise_sync_error=False)
