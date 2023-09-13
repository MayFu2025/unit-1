def powers_ten(num: int) -> str:
    prefix = ['Tera', 'Giga', 'Mega', 'Kilo', 'Unit', 'Mli', 'Micro', 'Nano', 'Pico']
    power = [12, 9, 6, 3, 0, -3, -6, -9, -12]
    out = ''
    for i in range(len(prefix)):
        out += f'{num} {"0" * power[i]}\n'
    return out

print(powers_ten(1))

# So hard???



