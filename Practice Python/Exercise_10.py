# Similar to exercise 5, but instead its executed through one line
import random
print([x for x in sorted(random.sample(range(100), k = (random.randint(8,12)))) if x in sorted(random.sample(range(100), k = (random.randint(8,12))))])