import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'

result = re.match('AC', s)
print(result)

result = re.search('DC', s)
print(result[0])

result = re.findall('DC', s)
print(result)

result = re.split('/', s, maxsplit=3)
print(result)

result = re.sub('A', 'D', s)
print(result)

result = re.fullmatch('AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC', s)
print(result)

s = "324040204023+0303020930320         --- nfekfjkfkj$JKJR#kd3k3rjnNJI#R3JJFHEHIFUEHNNRIU##RR"

result = re.search(r"k.r", s)
print(result)

result = re.search(r"k..r", s)
print(result)

result = re.search(r"\d\d\d", s)
print(result)

result = re.search(r"\D", s)
print(result)

result = re.search(r"\s", s)
print(result)

result = re.search(r"\S", s)
print(result)

result = re.search(r"\W", s)
print(result)

result = re.search(r"\bnfe", s)
print(result)

result = re.search(r"\Bnfe", s)
print(result)

result = re.search(r"\d*", s)
print(result)

result = re.search(r"\d+", s)
print(result)

result = re.search(r"[nfekf]", s)
print(result)

result = re.search(r"[4-8]", s)
print(result)

result = re.search(r"H|f", s)
print(result)

result = re.search(r"\d{3}", s)
print(result)

result = re.search(r"\d{1,3}", s)
print(result)

result = re.search(r"\d{4,}", s)
print(result)

result = re.search(r"\d{,4}", s)
print(result)

test_string = 'Привет! Как дела? А у меня нормально.'
result = re.findall(r"[бвгджзклмнпрстфхчшщБВГДЖЗКЛМНПРСТФХЧШЩ]\w+", test_string)
print(result)