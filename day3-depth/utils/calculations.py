from modules.invoice import Invoice
from modules.status import Status

def calculate_tax(invoice: Invoice):
    tot = invoice.total

    if tot <= 0:
        raise ValueError("Invalid invoice total amount")

    tax = tot * 0.18
    return tot + tax



def calculate_discount(invoice: Invoice, discount: float):
    if discount >= 100 or discount < 0:
        raise ValueError("Invalid discount percentage")

    tot = invoice.total

    if tot <= 0:
        raise ValueError("Invalid invoice total amount")

    disc = tot * (discount / 100)

    return tot - disc