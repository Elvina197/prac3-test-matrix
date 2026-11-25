from service import check

N = 16  
K = 8 + N % 5  

def report(case, expected, actual):
    status = "PASS" if actual == expected else "FAIL"
    print(case, expected, actual, status, sep=" | ")

# Матрица тест-кейсов (из таблицы)
cases = [
    ([0, 60], "OK"),
    ([30] * K, "OK"),
    (None, "TYPE"),
    ([], "EMPTY"),
    ([30, True], "BAD_ITEM"),
    ([61], "BAD_ITEM"),
    ([-1], "BAD_ITEM"),
    ([None] * (K + 1), "OVERLOAD")
]

for i, (values, expected) in enumerate(cases, 1):
    # Для вывода, чтобы не печатать длинные списки целиком
    display_val = values
    if isinstance(values, list) and len(values) > 5:
        display_val = f"list of len {len(values)}"
    
    report(f"Б-{i:02d}", expected, check(values, K))

# Стресс-тест (Б-09)
# 1000 * K элементов
big_packet = [30] * (1000 * K) 
actual = (check(big_packet, K), check([30], K))
report("Б-09", ("OVERLOAD", "OK"), actual)