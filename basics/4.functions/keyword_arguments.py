# Keyword Arguments make the order of the arguments you pass to the function less relevant

def get_net_price(price, discount):
    return price - price * (discount / 100)

print(f'Net Price: {get_net_price(100, 5)}')
print(f'Net Price: {get_net_price(5, 100)}')

better_get_net_price_call = get_net_price(discount=6, price=1280)
print(f'Net Price: {better_get_net_price_call}')


