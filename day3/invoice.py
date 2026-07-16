from dataclasses import dataclass


@dataclass
class Invoice:
    customer: str
    amount: float