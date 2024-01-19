import json

class TestJson:
    """
    params: testFilename -> str, .json filename
    params: tests_json   -> list, list of test cases in json
    params: tests        -> list, list of test cases as type Test
    """
    def __init__(self):
        self.testFilename = "tests.json"
        self.tests = []

    def loadTests(self):
        """Loads all Test Cases"""
        with open(self.testFilename) as tf:
            self.tests_json = json.load(tf)['TestCases']
        
        for test in self.tests_json:
            Ttest = Test(test)
            self.tests.append(Ttest)
    

class Test:
    def __init__(self, test_params):
        self.input_params = test_params['Input']
        self.output_params = test_params['Output']
    
    def test(self, target_func: function) -> bool:
        output = target_func(self.input_params['nums'], self.input_params['target'])
        return output == self.output_params['solution']
