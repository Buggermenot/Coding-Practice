import json, time

class Tests:
    """
    params: testFilename -> str, .json filename
    params: tests_json   -> list, list of test cases in json
    params: tests        -> list, list of test cases as type Test
    """
    def __init__(self):
        self.testFilename = "Test_Cases/tests.json"
        self.tests = []

    def loadTests(self, target_func) -> list:
        """Read and Loads all Test Cases from json"""
        with open(self.testFilename) as tf:
            self.tests_json = json.load(tf)['TestCases']
        
        for test in self.tests_json:
            Ttest = SingleTest(test, target_func)
            self.tests.append(Ttest)
        
        return self.tests
    

class SingleTest:
    def __init__(self, test_params, target_func):
        self.input_params = test_params['Input']
        self.output_params = test_params['Output']
        self.target_func = target_func

    def test(self, verbose=False) -> bool:
        # Specify Input properly
        start = time.time()
        output = self.target_func(self.input_params['nums'],
                                  self.input_params['target'])
        end = time.time()
        result = self.output_params['solution'] == output

        if verbose:
            print(f"\tInput:")
            for k, v in self.input_params.items():
                print(f'\t\t{k}: {v}')

            print(f"\tExpected Output:\n\t\t{self.output_params['solution']}")
            print(f"\tYour Output:\n\t\t{output}")
            print(f"\tTest: {'Passed' if result else 'Failed'}\n")
            print(f"\tTime Taken: {round((end - start) * 1000, 4)} ms")
        
        return result
