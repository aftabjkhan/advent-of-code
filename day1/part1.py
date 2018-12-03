#!/usr/bin/env python3
import sys


"""
Challenge:
https://adventofcode.com/2018/day/1
"""


def calculate_final_frequency(frequency_strings_list):
  frequency_deltas = [ int(x) for x in frequency_strings_list ]

  #initial frequency = 0
  frequency = 0;

  #apply all deltas to the frequency
  for delta in frequency_deltas:
    frequency = frequency + delta

  return frequency;



def test(case):

  #tests input is single line, comma separated. Convert to list
  test_strings = case.split(",")

  return calculate_final_frequency(test_strings);



if __name__ == '__main__':
  
  #check arg count
  if len(sys.argv) != 2:
    print("Usage: part1.py input_file_path")
    exit(1)

  #get frequency strings list
  input_file_path = sys.argv[1]
  file = open(input_file_path, "r")
  lines = [line.rstrip('\n') for line in file]

  print(calculate_final_frequency(lines))