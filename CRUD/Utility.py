import random
import string

def random_string(length:int) -> str:
    output_string = ''.join(random.choice(string.ascii_letters) for i in range(6))
    return output_string