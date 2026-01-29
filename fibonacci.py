import argparse
from functools import lru_cache

#!/usr/bin/env python3
"""Naive recursive Fibonacci implementation with a memoized variant."""

def fib(n: int) -> int:
  """Return the nth Fibonacci number (naive recursive)."""
  if n < 0:
    raise ValueError("n must be non-negative")
  if n <= 1:
    return n
  return fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
  """Return the nth Fibonacci number using memoization.

  This function mirrors `fib`'s behavior but is much faster for larger `n`.
  """
  if n < 0:
    raise ValueError("n must be non-negative")
  if n <= 1:
    return n
  return fib_memo(n - 1) + fib_memo(n - 2)


if __name__ == "__main__":
  print(fib(10))
