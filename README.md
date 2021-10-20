# Practical Entropy-Compressed Rank/Select Dictionary

У меня есть ощущение, что это очень важно, посмотрим.

B - bitvector, |B| = n

rank(x, S) - number of ones in B[0, x]

select(i, S) - the position of the i-th one from left in B

nH0(S) = mlog(n/m) + (n-m)log(n/(n-m)) - "zero-th order empirical entropy" - просто посчитали число единиц (m), прикинули вероятности как отношения #(1)/n и #(2)/n 

### esp


## Source

https://arxiv.org/pdf/cs/0610001.pdf
