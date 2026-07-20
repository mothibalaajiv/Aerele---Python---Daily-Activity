from modules.invoice import Invoice
from modules.status import Status
from controllers.invoice_controller import InvoiceController
from utils.calculations import calculate_tax, calculate_discount


invoice = Invoice(invoice_id=101, customer_name="Mothi Balaaji", total=10000.0, status=Status.PENDING)

print("Invoice Details:")
print(invoice)

controller = InvoiceController()
print("\nValidating Invoice...")
controller.validate(invoice)

total_final = calculate_tax(invoice)
print(f"\nTotal after 18% Tax: Rs.{total_final:.2f}")

total_after_discount = calculate_discount(invoice, 10)
print(f"Total after 10% Discount: Rs.{total_after_discount:.2f}")
    
print("\nSubmitting Invoice...")
controller.submit(invoice)

print(f"Current Status: {invoice.status.value}")

print("\nCancelling Invoice...")
controller.cancel(invoice)

print(f"Current Status: {invoice.status.value}")
