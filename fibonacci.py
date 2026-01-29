import argparse

#!/usr/bin/env python3
"""Naive recursive Fibonacci implementation."""

def fib(n: int) -> int:
  """Return the nth Fibonacci number (naive recursive)."""
  if n < 0:
    raise ValueError("n must be non-negative")
  if n <= 1:
    return n
  return fib(n - 1) + fib(n - 2)

print(fib(10))
