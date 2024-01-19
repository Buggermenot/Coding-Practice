import sys
sys.path.append('..')
from YourSolution import Solution
from Test_Cases import tests

def testAll(tests: list, verbose=False):
    passCount = 0
    failedOn = []
    total_test = len(tests)

    for i in range(total_test):
        res = tests[i].test(verbose)
        if res:
            passCount += 1
        else:
            failedOn.append(i)
    
    print('Test Results:')
    print(f'\tScore: {(passCount * 100) / total_test}')
    print(f'\tPassed: {passCount} / {total_test}')
    print(f'\tTests Failed on: {failedOn}')

if __name__ == "__main__":
    allTests = tests.Tests().loadTests(target_func=Solution.twoSum)
    testAll(allTests)