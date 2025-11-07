from __future__ import annotations
from typing import Any
from flask import Flask

class Bcrypt:
    app: Flask | None

    def __init__(self, app: Flask|None = ...) -> None: ...
    def init_app(self, app: Flask) -> None: ...

    def generate_password_hash(
            self,
            password: str|bytes,
            rounds: str|None,
            prefix: str|None
    ) -> bytes: ...

    def check_password_hash(
            self,
            pw_hash: str|bytes,
            password: str|bytes,
    ) -> bool: ...

def generate_password_hash(password: str|bytes, rounds: int|None) -> bytes: ...
def check_password_hash(pw_hash: str|bytes, rounds: int|None) -> bool: ...