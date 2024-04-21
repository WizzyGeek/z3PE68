import z3

# https://stackoverflow.com/a/67060889/10540048
def min(vs):
  m = vs[0]
  for v in vs[1:]:
    m = z3.If(v < m, v, m)
  return m

n = 10
d = z3.IntVector('x', n)
sol = z3.Optimize()

sol.add(z3.Distinct(d))
for i in d: sol.add(i > 0, i < n+1)

s = z3.Int('s')
# sol.add(s >= 6, s <= 27)
sol.add(s == 14) # Only sum for which 6 was in front

sol.add(d[8] + d[0] + d[1] == s)
for i in range(0, 7, 2): sol.add(d[i] + d[i + 2] + d[i + 3] == s)

groups = []
groups.append(d[8] + d[0] * 10 + d[1] * 100 - 111)
for i in range(0, 7, 2): groups.append(d[i] + d[i + 2] * 10 + d[i + 3] * 100 - 111)

l = len(groups)
b = [0] * l
for i in range(l):
    for j in range(l):
        b[i] = (b[i] * 1000) + groups[(i - j) % l]

sol.maximize(min(b))

sol.check()
m = sol.model()
print(m)
mp = m.eval(min(b))
c = mp.as_string()
print("".join(map(lambda k: str(int(k) + 1), c)))
