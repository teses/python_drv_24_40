
## normale funktion
def first_n_normal(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

# als generator funktion
def first_n_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_first_n_normal = sum(first_n_normal(1000))
print(sum_first_n_normal)

sum_first_n_generator = sum(first_n_generator(1000))
print(sum_first_n_generator)

## Speicherverbrauch vergleichen:
import sys
list_size = sys.getsizeof(first_n_normal(100000))
gen_size = sys.getsizeof(first_n_generator(10000))
gespart = (list_size - gen_size) / list_size*100
print(f"Liste Verbrauch: {list_size}")
print(f"Generator VErbrauch: {gen_size}")
print(f"gespart: {gespart:.2f} %")

