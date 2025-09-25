def normalize_name(name):
    name = ' '.join(name.split())
    return ' '.join(word.capitalize() for word in name.split())

def normalize_phone(phone):
    digits = ''.join(filter(str.isdigit, phone))
    
    if digits.startswith('0'):
        digits = '+84' + digits[1:]
    elif not digits.startswith('+'):
        digits = '+84' + digits
    return digits

name = "   nGuYeN   vaN   naM  "
phone = "0912 345 678"
normalized_name = normalize_name(name)
normalized_phone = normalize_phone(phone)
print("Normalized Name:", normalized_name)
print("Normalized Phone:", normalized_phone)