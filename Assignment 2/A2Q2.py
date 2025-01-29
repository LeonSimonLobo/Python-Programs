products = {}
while True:
    product_name=input("Enter product name (or type 'done' to finish): ")
    if product_name.lower()=='done':
        break
    product_price=float(input(f"Enter price for {product_name}: "))
    products[product_name]=product_price
while True:
    query=input("Enter a product name to see the price (or type 'exit' to quit): ")
    if query.lower()=='exit':
        break
    if query in products:
        print(f"The price of {query} is Rs.{products[query]:.2f}")
    else:
        print(f"Sorry, {query} is not in the product list.")

