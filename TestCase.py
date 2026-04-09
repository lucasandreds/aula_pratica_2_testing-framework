class TestCase:

    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self, result):
        result.test_started()
        self.set_up()
        try:
            test_method = getattr(self, self.test_method_name)
            test_method()
        except AssertionError as e:
            result.add_failure(self.test_method_name)
        except Exception as e:
            result.add_error(self.test_method_name)
        self.tear_down()

    def set_up(self):
        pass

    def tear_down(self):
        pass

class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')
        

if __name__ == '__main__':
    test = MyTest('test_a')
    test.run()
    
    test = MyTest('test_b')
    test.run()
    
    test = MyTest('test_c')
    test.run()
    
    