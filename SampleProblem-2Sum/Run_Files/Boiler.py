import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..' )
solutions_dir = os.path.join(parent_dir, 'Solutions')

sys.path += [parent_dir, solutions_dir]

import time

# All Tests
from Test_Cases import tests

def testAll(tests: list, verbose=False):
    """Tests all """
    passCount = 0
    failedOn = []
    total_test = len(tests)

    start = time.time()
    if verbose:
        print("\nIndividual Test Results:")

    for i in range(total_test):
        if verbose:
            print(f"Test case {i+1}")
        res = tests[i].test(verbose)
        if res:
            passCount += 1
        else:
            failedOn.append(i)
    
    # Overall test stats
    print('\nTest Results:')
    print(f'\tScore: {round((passCount * 100) / total_test, 3)}%')
    print(f'\tPassed: {passCount} / {total_test}')
    print(f'\tTests Failed on: {failedOn if failedOn else None}')
    print(f'\tTime Taken: {round((time.time() - start) * 1000, 4)} ms\n')
 

if __name__ == "__main__":

    # Run file names. Update as needed. Do not add .py to the file.
    YourSolutionFile = "YourSolution"
    SampleSolutionFile = "SampleSolution"

    # Nothing to update beyond this #
    # Imports
    YourSolution = __import__(YourSolutionFile).Solution
    SampleSolution = __import__(SampleSolutionFile).Solution

    # Check for Arguments
    args = sys.argv[1:]
    if not args:
        allTests = tests.Tests().loadTests(target_func=YourSolution.twoSum)
    elif args[0] == 'verbose':
        allTests = tests.Tests().loadTests(target_func=YourSolution.twoSum)
    elif args[0] == 'sample':
        allTests = tests.Tests().loadTests(target_func=SampleSolution.twoSum)
    else:
        exit(f"Incorrect input parameter(s) {args}. Try make py or make py sample verbose")

    verbose = 'verbose' in args
    testAll(allTests, verbose=verbose)