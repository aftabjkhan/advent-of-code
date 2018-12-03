#!/usr/bin/env python3
import sys


"""
Challenge:
https://adventofcode.com/2018/day/2
"""


def get_two_three_char_count(box_id):

  box_chars = list(box_id)

  char_frequencies = {}

  # for each char in the box id, increment frequency in the char map
  for c in box_chars:
    if c in char_frequencies:
      char_frequencies[c] += 1
    else:
      char_frequencies[c] = 1

  two_instances = 0
  three_instances = 0

  # for each char that occurs 2 or 3 times, increment 2 & 3 instance counters
  for value in char_frequencies.values():
    if value == 2:
      two_instances += 1
    if value == 3:
      three_instances += 1

  # return number of chars that occur 2 and 3 times as a tuple
  return (two_instances, three_instances);



def calculate_boxes_checksum(box_id_list):
  
  boxes_with_two_instances = 0
  boxes_with_three_instances = 0

  for box_id in box_id_list:
    char_count = get_two_three_char_count(box_id)

    if char_count[0] > 0:
      boxes_with_two_instances += 1
    if char_count[1] > 0:
      boxes_with_three_instances += 1

  return (boxes_with_two_instances * boxes_with_three_instances)


def test(case):
  #tests input is single line, comma separated. Convert to list
  test_strings = case.split(",")

  return calculate_boxes_checksum(test_strings);



if __name__ == '__main__':
  
  #check arg count
  if len(sys.argv) != 2:
    print("Usage: part1.py input_file_path")
    exit(1)

  #get frequency strings list
  input_file_path = sys.argv[1]
  file = open(input_file_path, "r")
  lines = [line.rstrip('\n') for line in file]

  print(calculate_boxes_checksum(lines))