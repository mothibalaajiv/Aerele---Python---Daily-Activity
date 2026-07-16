from invoice import Invoice


class InvoiceController:

    def validate(self, invoice: Invoice):

        if invoice.amount <= 0:
            print("Invalid Invoice Amount")
            return

        print("Invoice is Valid")


invoice = Invoice("Mothi", -500)

controller = InvoiceController()
controller.validate(invoice)