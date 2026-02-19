#!/bin/bash
# This script calculates halal profit sharing (no interest).
# Based on a Mudarabah-style model.
# Sample purpose only.

# Input:
# c = capital invested
# p = total profit generated
# s = investor's profit share percentage

echo "Enter the capital invested:"
read c

echo "Enter the total profit generated:"
read p

echo "Enter investor profit share percentage (e.g. 60 for 60%):"
read s

investor_profit=$(expr $p \* $s / 100)

echo "----------------------------------"
echo "Halal Profit-Sharing Result"
echo "Capital Invested: $c"
echo "Total Profit Generated: $p"
echo "Investor Share (%): $s"
echo "Investor Profit (Halal): $investor_profit"
