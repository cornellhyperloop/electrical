#include <gtest/gtest.h>
// Write a factorial function and then test it using Google Tests

int Factorial(int n)
{
  if (n == 0)
  {
    return 1;
  }
  return n * Factorial(n - 1);
}