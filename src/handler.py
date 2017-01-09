tax_rate = 0.0815

def handle(event, context):
    subtotal = event['subtotal']

    taxes = tax_rate * subtotal
    total = taxes + subtotal

    return {
        'taxRate': tax_rate,
        'taxes': taxes,
        'total': total
    }
