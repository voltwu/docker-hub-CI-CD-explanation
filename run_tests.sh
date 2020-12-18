#! /bin/bash

# run all unit test files that file name start with "unittest" under "test" dir.
for dir in $(ls tests -1FA | grep "^unittest"); 
    do python3 tests/$dir; 
done
