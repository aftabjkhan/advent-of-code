#!/usr/bin/env python3
import sys


"""
Challenge:
https://adventofcode.com/2018/day/2#part2
"""

def find_similar_box_ids(box_id_list):
  
  # for each box id
  for index, current_id in enumerate(box_id_list):
    
    # compare to remaining box ids
    for test_match in box_id_list[(index+1):len(box_id_list)]:

      """ for each character in the two box IDs being compared, track count of 
      mismatched chars (must be only one), and index at which mismatch occurred
      """
      mismatched_char_count = 0
      mismatched_char_index = 0
      t = list(test_match)

      for char_index, c in enumerate(list(current_id)):
        if t[char_index] != c:
          mismatched_char_count += 1
          mismatched_char_index = char_index
        if mismatched_char_count > 1:
          mismatched_char_index = None
          break

      # if only 1 mismatch, remove mismatch and return remaining chars
      if mismatched_char_count == 1:
        t.pop(mismatched_char_index)
        return (''.join(t))




def test(case):
  # tests input is single line, comma separated. Convert to list
  test_strings = case.split(",")

  return find_similar_box_ids(test_strings);



if __name__ == '__main__':
  
  #check arg count
  if len(sys.argv) != 2:
    print("Usage: part1.py input_file_path")
    exit(1)

  #get frequency strings list
  input_file_path = sys.argv[1]
  file = open(input_file_path, "r")
  lines = [line.rstrip('\n') for line in file]

  print(find_similar_box_ids(lines))