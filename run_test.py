import glob
import sys

import timeit

if len(sys.argv) == 1:
    testdata_paths = ['listanddict.py', 'lists.py']
else:
    testdata_paths = sys.argv[1:]
for testdata_path in testdata_paths:
    with open(testdata_path) as testfile:
        testdata=testfile.read()
    print('Test data file: {}'.format(testdata_path))
    for test_script in glob.glob('./*.in'):
        pyscript = ''
        print(test_script)
        with open(test_script) as input_script:
            for line in input_script:
                pyscript = '{}{}'.format(pyscript, line.replace('@DATA@',
                                                                testdata))
        try:
            result = timeit.timeit(pyscript, number=10000)
            print("result: {} seconds".format(result))
        except ImportError as e:
            print("ERROR: {}".format(str(e)))
