from modules.invoice import Invoice
from modules.status import Status


class InvoiceController:

    def validate(self, invoice: Invoice):
        """Validate invoice before processing."""

        if invoice.invoice_id <= 0:
            raise ValueError("Invoice ID must be greater than 0.")

        if not invoice.customer_name:
            raise ValueError("Customer name cannot be empty.")

        if invoice.total <= 0:
            raise ValueError("Invoice total must be greater than 0.")

        if not isinstance(invoice.status, Status):
            raise ValueError("Invalid invoice status.")

        print("Invoice validation successful.")

    def submit(self, invoice: Invoice):
        self.validate(invoice)
        invoice.status = Status.COMPLETED
        print(f"Invoice {invoice.invoice_id} submitted successfully.")

    def cancel(self, invoice: Invoice):
        invoice.status = Status.CANCELED
        print(f"Invoice {invoice.invoice_id} cancelled successfully.")