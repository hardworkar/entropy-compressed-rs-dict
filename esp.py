#!/usr/bin/env python3
import numpy as np
import math
from math import log2
from scipy.special import comb
import itertools

n = 65536
B = np.random.randint(low=0, high=2, size=n)
print(B[:10])

k = int(math.log2(n)**3)
l = int(math.log2(n)**2)
s = int(math.log2(n)//2)

# в каждом l-блоке содержится l/s = 4*s s-блоков
nums_in_l = int(math.ceil(l / s))


nslb = int(math.ceil(n / k))
nlb = int(math.ceil(n / l))
nsb = int(math.ceil(n / s))

print("len of splar block: %d" % k)
print("len of large block: %d" % l)
print("len of small block: %d" % s)

def enumerative_code(bit_block):
  t = len(bit_block)
  u = sum(bit_block)
  pu = [idx for idx, e in enumerate(bit_block) if e == 1]
  s = sum([comb(t-pu[i]-1, (u-i), exact = True) for i in range(0, u)])
  return s

# Rl[0..n/l] - ranks of large blocks, each ceil(log(n)) bits
# Rs[0..n/s] - ranks of small blocks, each ceil(log(log(n))) bits
# SB

Rl = [0] * nlb
for i in range(0, nlb):
  Rl[i] = sum(B[:(i+1)*l])

Rs = [0] * nsb
for i in range(0, nsb):
  idx_large = i // nums_in_l
  il = i % nums_in_l
  left = idx_large * l
  right = left + (il+1) * s
  Rs[i] = sum(B[left:right])

SB = []
for i in range(0, n, s):
  SB.append(enumerative_code(B[i:i+s]))

def plog2(x):
  return 0 if x == 0 else log2(x)
def rank(x):
  xl = x//l
  xs = x//s

  lr = Rl[xl]
  sr = Rs[xs]

  lp = lr * plog2(l*xl/lr) + (l*xl - lr) * plog2((l*xl) / (l*xl-lr))
  sp = sr * plog2(s*xs/sr) + (s*xs - sr) * plog2((s*xs) / (s*xs-sr))

  return lp+sp

print(rank(258))
