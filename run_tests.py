#!/usr/bin/env python3
import sys
import os.path
import importlib.util

if __name__ == "__main__":
  
  if len(sys.argv) < 3:
    print("Usage: run_tests.py day.part test1 [test2...]")
    print("Ex: run_tests.py day1.part2 ./day1/p1test3.txt")
    exit(1)

  # import module to test
  module = importlib.import_module(sys.argv[1])
  
  tests = sys.argv[2:len(sys.argv)]
  
  test_count = 0
  passed = 0
  failed = 0


  while len(tests) > 0:
    input_file_path = tests.pop()
    file = open(input_file_path, "r")
    lines = [line.strip('\n ') for line in file]

    test_input = lines[0]
    expected = lines[1]
    answer = str(module.test(test_input))
    test_count += 1

    if answer == expected:
      print("Test " + str(test_count) + " Passed. Answer = " + str(answer))
      passed += 1
    else:
      print("Test " + str(test_count) + " Failed. Test: " + input_file_path)
      print("  Input = " + test_input)
      print("  Answer = " + str(answer) + ". Expected = " + expected)
      failed += 1


  print("\nTest Summary:")
  print("+ Pass: " + str(passed) + " of " + str(test_count))
  print("- Fail: " + str(failed) + " of " + str(test_count))