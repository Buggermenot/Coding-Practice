import json

class Tests:
    """
    params: testFilename -> str, .json filename
    params: tests_json   -> list, list of test cases in json
    params: tests        -> list, list of test cases as type Test
    """
    def __init__(self):
        self.testFilename = "tests.json"
        self.tests = []

    def loadTests(self, target_func: function):
        """Loads all Test Cases"""
        with open(self.testFilename) as tf:
            self.tests_json = json.load(tf)['TestCases']
        
        for test in self.tests_json:
            Ttest = SingleTest(test, target_func)
            self.tests.append(Ttest)
    

class SingleTest:
    def __init__(self, test_params, target_func: function):
        self.input_params = test_params['Input']
        self.output_params = test_params['Output']
        self.target_func = target_func

    def test(self, verbose=False) -> bool:
        output = self.target_func(self.input_params['nums'],
                                  self.input_params['target'])
        
        result = self.output_params['solution'] == output

        if verbose:
            print(f"Input:")
            for k, v in self.input_params:
                print(f'\t{k}: {v}')

            print(f"Expected Output:\n\t{self.output['solution']}")
            print(f"Your Output:\n\t{output}")
            print(f"Test: {'Passed' if result else 'Failed'}")
        
        return result
