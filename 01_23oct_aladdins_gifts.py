from collections import deque

materials = [int(el) for el in input().split()]
magic = deque([int(el) for el in input().split()])


def check_what_gift(material, func_magic):
    gift_value = material + func_magic
    if gift_value < 100 and gift_value % 2 == 0:
        gift_value = (material * 2) + (func_magic * 3)
    elif gift_value < 100 and gift_value % 2 != 0:
        gift_value = (material + func_magic) * 2
    if gift_value >= 500:
        gift_value //= 2
    if 100 <= gift_value < 200:
        return "Gemstone"
    if 200 <= gift_value < 300:
        return "Porcelain Sculpture"
    if 300 <= gift_value < 400:
        return "Gold"
    if 400 <= gift_value < 500:
        return "Diamond Jewellery"


gifts = {}
for turn in range(min(len(magic), len(materials))):
    current_material = materials.pop()
    current_magic = magic.popleft()
    gift = check_what_gift(current_material, current_magic)
    if gift not in gifts.keys():
        gifts[gift] = 1
    else:
        gifts[gift] += 1


has_succeeded = False
if "Gemstone" in gifts.keys() and "Porcelain Sculpture" in gifts.keys():
    has_succeeded = True
if "gold" in gifts.keys() and "Diamond Jewellery" in gifts.keys():
    has_succeeded = True

if has_succeeded:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if magic:
    print(f'Magic left: {", ".join(str(el) for el in magic)}')
elif materials:
    print(f'Materials left: {", ".join(str(el) for el in materials)}')
for gift, quantity in gifts.items():
    if gift is not None:
        print(f'{gift}: {quantity}')



