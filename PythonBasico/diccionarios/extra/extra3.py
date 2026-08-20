def total_by_category(products):
    result = {}
    for product in products:
        category = product['category']
        result[category] = result.get(category, 0) + product['price']
    return result


products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

result = total_by_category(products)
print(result)