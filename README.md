# ProjectEuler - Problem 46 (Goldbach's other conjecture)
## Text
> It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
>
> `9 = 7 + 2×1²`
>
> `15 = 7 + 2×2²`
>
> `21 = 3 + 2×3²`
>
> `25 = 7 + 2×3²`
>
> `27 = 19 + 2×2²`
>
> `33 = 31 + 2×1²`
> 
> It turns out that the conjecture was false.
>
> What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

## Some math
The problem states that given and odd composite number `o` this can always be written as `p + 2*k^2` where `p` is a prime number.
A composite number is a positive integer that has at least one divisor other than 1 and itself, that means that `o` should be greater than 1 and nonprime. Actually the condition that `o` must be nonprime is redundant since every odd prime number is equal to the prime number itself so, basically, we have `o = p + 2*k^2` with `p = o` and `k = 0`. This means that the conjecture is always true even for prime numbers considering 0 as the square. Hence we can assume `o` to be a generic odd number greater than 1 that is `o = 2*n + 1` for `n = 1, 2, ...`.

There is a useful property of prime numbers:
> Every prime number greater than 3 is of the form `6*m ± 1` for some `m = 1, 2, ...`.

The viceversa is not true in general, for example 25 is not prime but it is equal to `6*4 + 1`. This is not a problem for our purposes as we can consider `p = 6*m ± 1` and check if it is a prime only if necessary.

This way, replacing `o = 2*n + 1` and `p = 6*m ± 1` we can reduce our problem to an equation:
> `2*n + 1 = 6*m ± 1 + 2*k^2`

This equation can be splitted in two other equations according to the `±` operator.
* If we have a `+` sign then we get `2*n + 1 = 6*m + 1 + 2*k^2` that leads to
  > `n - 3*m = k^2`
* Otherwise we get `2*n + 1 = 6*m - 1 + 2*k^2` that leads to
  > `n - 3*m + 1 = k^2`

Since the second member of the two equations above is always non negative we can bound `m` to be less than or equal to `n/3` and `(n + 1)/3` respectively. N.B. the second case is more general but it can lead to negative numbers when used in the first equation (`n - 3*(n + 1)/3 = -1 ≠ k^2`).

The only cases that remain excluded from the assumption that `p = 6*m ± 1` are when `p` is 2 or 3.
We can discuss easily the case `p = 2` since we would get `2*n + 1 = 2 + 2*k^2` that is never true since the first member is odd while the second is even. The case `p = 3` can be reduced to `n - 1 = k^2`.

At this point we fix `n` and start searching a counterexample for the conjecture:
1. Check the case `p = 3`:
  * If `sqrt(n - 1)` is an integer, this means that `n - 1 = k^2` so we can conclude that `o = 3 + 2*k^2` for some `k`. Then we pass to the next `n`.
  * Otherwise `o ≠ 3 + 2*k^2` for any `k` and so we must see if other primes `p` lead to confirm the conjecture.
2. If the case `p = 3` fails, we start looping through all possible `m` values (from 1 to `(n + 1)/3`), we now must check if `n - 3*m` or `n - 3*m + 1` are square. Let `x = n - 3*m`, we have 3 cases:
  * If `x` is nonnegative and `sqrt(x)` is an integer, this means that `n - 3*m = k²`, then this was the case where `p = 6*m + 1`. If `p` is prime then we have a case that confirms the conjecture so we must pass to the next `n`, otherwise we must look for other possibile value of `p` incrementing `m`.
  * Similarly to the previous case, when `sqrt(x + 1)` we get `p = 6*m - 1` that, as above, can be prime or nonprime.
  * When neither `sqrt(x)` nor `sqrt(x + 1)` are squares we must check the following value of `n`.

The algorithm ends when we find a number `n` such that the cases above fail for `p = 3` and for every `m = 1, ..., (n + 1)/3`.
