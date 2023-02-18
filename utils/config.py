from dataclasses import dataclass


@dataclass
class Connection:
    host: str
    port: str


@dataclass
class Config:
    connection: Connection
    name: str
