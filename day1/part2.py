#!/usr/bin/env python3
import sys


"""
Challenge:
https://adventofcode.com/2018/day/1#part2
"""


def find_first_duplicate(frequency_strings_list):
  frequency_deltas = [ int(x) for x in frequency_strings_list ]

  # initial frequency = 0
  frequency = 0
  # frequencies reached thus far. Using set type for O(1) lookup and value uniqueness
  answers = set()
  # start at begining of list of deltas
  deltas_iterator = iter(frequency_deltas);

  # apply all deltas to the frequency
  while frequency not in answers:

    try:
      # try to get the next item from the list of deltas
      delta = next(deltas_iterator)
    except StopIteration as e:
      # if all items are exhausted from the list of deltas, restart at the begining
      deltas_iterator = iter(frequency_deltas);
      #print("restarting...")
      continue
    else:
      answers.add(frequency)
      #print(answers)
      frequency = frequency + delta
      #print("Current freq: " + str(frequency))

  # once dup is found, return
  return frequency



def test(case):

  # tests input is single line, comma separated. Convert to list
  test_strings = case.split(",")

  return find_first_duplicate(test_strings);



if __name__ == '__main__':
  
  # check arg count
  if len(sys.argv) != 2:
    print("Usage: part1.py input_file_path")
    exit(1)

  #get frequency strings list
  input_file_path = sys.argv[1]
  file = open(input_file_path, "r")
  lines = [line.rstrip('\n') for line in file]

  print(find_first_duplicate(lines))