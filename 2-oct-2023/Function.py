def calculate_tax(bill,tax_rate):
    a= (bill * tax_rate) / 100.00
    print('Total Tax:',a)
    return a
calculate_tax(170.00,15)
