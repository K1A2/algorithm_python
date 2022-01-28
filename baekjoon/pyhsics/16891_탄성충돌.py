from fractions import Fraction
m1, m2 = 1, int(input()) ** 2
v1, v2 = 0, -1
count = 0
while v1 < 0 or v2 < 0 or v1 > v2:
    nv1 = Fraction(m1 - m2, m1 + m2) * v1 + Fraction(2 * m2, m1 + m2) * v2
    nv2 = Fraction(2 * m1, m1 + m2) * v1 - Fraction(m1 - m2, m1 + m2) * v2
    v1, v2 = nv1, nv2
    count += 1
    if v1 < 0:
         v1 *= -1
         count += 1
print(count)