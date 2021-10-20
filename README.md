# Practical Entropy-Compressed Rank/Select Dictionary

У меня есть ощущение, что это очень важно, посмотрим.

B - bitvector, |B| = n

__rank(x, S)__ - number of ones in B[0, x]

__select(i, S)__ - the position of the i-th one from left in B

nH0(S) = mlog(n/m) + (n-m)log(n/(n-m)) - "zero-th order empirical entropy" - просто посчитали число единиц (m), прикинули вероятности как отношения #(1)/n и #(2)/n 

Kак вывод, они хранят enumerativeCodes, rank-directories для LB, SB и указатели на SLB в явном виде + такая же таблица, как у Jacobson'а. Итого расход по памяти как в Якобсоне, только доп поинтеры (n/(log(n)^2)) для SLB, но зато хранится не оригинальный битмап, а nH0.

## Source

https://arxiv.org/pdf/cs/0610001.pdf

[2] T. Cover. Enumerative source encoding.
