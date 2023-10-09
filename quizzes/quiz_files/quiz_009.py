def powers_ten(s: str) -> str:
    num = s.split(" ")[0]
    unit = " ".join(s.split()[1:])
    prefixes = ['tera', 'giga', 'mega', 'kilo', '', 'milli', 'micro', 'nano', 'pico']
    powers = [12, 9, 6, 3, 0, -3, -6, -9, -12]
    out = [f'{s} is equal to:']
    count = 8
    for power in powers:
        if power < 0:
            temp = f"0.{('000 ' * (abs(power) // 3))[:-2]}{num}"
        elif power > 0:
            temp = f"{num}{' 000' * (abs(power) // 3)}"
        else:
            temp = num
        temp = temp.ljust(20)
        out.append(f"{temp}{prefixes[count]}{unit}")
        count -= 1
    return "\n".join(out)

# Check that it works:
print(powers_ten(input("Input a number with unit: ")))



