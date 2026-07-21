from dataclasses import dataclass
from modules.status import Status

@dataclass
class Invoice:
    invoice_id : int
    customer_name : str
    total : int
    status : Status