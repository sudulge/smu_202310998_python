def get_fixed_price(rate, discounted_price):
    return discounted_price / ((100-rate) * 0.01)

rate = int(input("할인율은? "))

A_discounted_price = int(input("A 상품의 할인된 가격은? "))
B_discounted_price = int(input("B 상품의 할인된 가격은? "))

print("A 상품의 정가는", get_fixed_price(20, A_discounted_price), "원")
print("B 상품의 정가는", get_fixed_price(20, B_discounted_price), "원")