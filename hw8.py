def buy(dict):
    print("[구입]")
    item = input("상품명? ")
    
    if item:
        quantity = int(input("수량은? "))
        dict[item] = quantity
        print(f'장바구니에 {item} {quantity}개가 담겼습니다.\n')
        return True
    else:
        print()
        return False

def show(dict):
    print(f">>> 장바구니 보기: {dict}\n")

def find(dict):
    print("[검색]")
    item = input("장바구니에서 확인하고자 하는 상품은? ")

    if item in dict:
        print(f"{item}은(는) {dict[item]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {item}은(는) 없습니다.")


shopping_bag = {}

while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)
