from typing import Optional

class PyEvm:
    """Example Type Stub"""

    def call(self): ...
    def simulate(self): ...
    def deploy(self): ...
    def transact(self): ...
    @staticmethod
    def from_fork(url: str, blocknumber: Optional[int] = None) -> PyEvm: ...
    @staticmethod
    def from_snapshot(snapshot: str) -> PyEvm: ...
    def create_snapshot(self) -> str: ...
    def create_account(self, address: str, balance: Optional[int] = None) -> str: ...
    def get_balance(self, address: str) -> int: ...
    def transfer(self, caller: str, to: str, amount: int): ...

class PyAbi:
    """Example Type Stub"""

    def bytecode(self):...
    def encode_constructor(self):...
    def encode_function(self):...
    def from_abi_bytecode(self):...
    def from_full_json(self):...
    def from_human_readable(self):...
    def has_fallback(self):...
    def has_function(self):...
    def has_receive(self):...