This tries to use the python timeit module to measure serialization times.

To run the tests:

`python run_test.py`

or

`python3 run_test.py`

On my laptop:

# python 2.7:


    Test data file: listanddict.py
    ./pickle.in
    result: 101.349500179 seconds
    ./json.in
    result: 17.721873045 seconds
    ./cpickle.in
    result: 21.393556118 seconds
    ./msgpack.in
    result: 4.27751708031 seconds
    Test data file: lists.py
    ./pickle.in
    result: 49.931540966 seconds
    ./json.in
    result: 4.17448091507 seconds
    ./cpickle.in
    result: 7.87679219246 seconds
    ./msgpack.in
    result: 0.957564115524 seconds


# python 3.5:


    Test data file: listanddict.py
    ./pickle.in
    result: 5.616457188967615 seconds
    ./json.in
    result: 11.391341902315617 seconds
    ./cpickle.in
    ERROR: No module named 'cPickle'
    ./msgpack.in
    result: 7.006749976892024 seconds
    Test data file: lists.py
    ./pickle.in
    result: 2.2143266620114446 seconds
    ./json.in
    result: 2.1372002298012376 seconds
    ./cpickle.in
    ERROR: No module named 'cPickle'
    ./msgpack.in
    result: 2.0084542869590223 seconds
