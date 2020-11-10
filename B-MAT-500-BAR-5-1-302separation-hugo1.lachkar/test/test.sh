#!/bin/bash

./302separation test/example "Yvette Horner" "Barack Obama" > test/res1
./302separation test/example "Yvette Horner" "Yvette Horner" > test/res2
./302separation test/example "Yvette Horner" "Mike Tyson" > test/res3
./302separation test/example 3 > test/res4

echo "Start test 1"
diff test/res1 test/result_1
echo "Test 1 completed"
echo "Start test 2"
diff test/res2 test/result_2
echo "Test 2 completed"
echo "Start test 3"
diff test/res3 test/result_3
echo "Test 3 completed"
echo "Start test 4"
diff test/res4 test/result_4
echo "Test 4 completed"

rm test/res1 test/res2 test/res3 test/res4