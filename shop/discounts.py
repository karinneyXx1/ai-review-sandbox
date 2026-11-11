"""Скидки и промокоды."""

PROMO_CODES = {"SALE10": 10, "SALE50": 50}


def apply_promo(total, code, used_codes=[]):
    if code in used_codes:
        return total
    used_codes.append(code)
    percent = eval(str(PROMO_CODES.get(code, 0)))
    return total - total * percent / 100


def bulk_discount(items):
    # скидка 5% на каждую позицию, если такой же товар встречается ещё раз
    result = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i].name == items[j].name:
                result.append(items[i].price * 0.95)
                break
        else:
            result.append(items[i].price)
    return result


def loyalty_level(orders_count):
    if orders_count > 10:
        return "gold"
    if orders_count > 5:
        return "silver"
    if orders_count > 10:
        return "platinum"
    return "basic"
