# Notes: Testing

- Process of evaluating computer code to ensure it does what it's supposed to do.

- As programs become more and more complicated, strange errors are inevitable.

## Fundamental testing concepts

- Manual testing: Test functions with different params, or scripts with different cmdline args. Not formal way of testing.

- Automatic testing: Write code to automatically test if a return value matches expectation.
    - The more test cases, the more you can guarantee the code works reliably.
    - Automatically raises error when returned result isn't what's expected.

## Unit tests

- Tests run on individual components or units of code to ensure correctness.
- Preparation refers to as **test fixture**
- Test suite: collection of test cases and/or test suites that should be exec'd together.
- Test runner: runs the test and provides devs with outcome data, either textually or graphically. also provides a special value to devs to communicate the test results.
- Python `unittest.TestCase` class contains **test methods** which are run sequentially. Within each test method, assertion functions like `self.assertEqual` or `self.assertIn` are used to check if a variable has expected value. 

- Unit tests are run with: `unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(<testcase_class>))` or `unittest.main()` for all tests.

- Whenever a new test is run or torn down, `self.setUp()` or `self.tearDown()` is called. You can override those with your own preparations.


## `pytests` (external module)

- Test conditions use `assert <condition>, <fail_message>`

- `@pytest.fixture` function decorator for marking fixtures

## White-box vs Black-box testing

- **White-box** (clear-box/transparent testing): Relies on test creator's knowledge of the software being tested to construct test cases.

- **Black-box**: Written with a knowledge of what the program should do, not how it does it.

## Other test types

- Integration test: Verify if the whole system (or set of connected components) work together.

- Regression test: Verify if an issue or error has been fixed. Part of the debugging process. 

- Smoke test / Build verification test: Sanity check to find major bugs (i.e. program not starting). Does not replace more fine-grained tests.

- Load test: Tests if a system can handle heavy load (e.g lots of concurrent requests) without performance degradation.

## Test-Driven Development

- **Create test BEFORE writing code.**

- Basic steps:
    - Write a Test (which will fail at first because there's no code yet)
    - Write and edit the Code until all tests pass.
    - Repeat as new features are added

- Pros: Helps you think about ways the program will fail or break before jumping into writing the code, allowing the problem you're solving to be well thought out.

- Cons: Increase completion time.