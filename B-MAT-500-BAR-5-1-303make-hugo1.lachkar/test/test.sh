#!/bin/bash

./303make test/MakefileTest  > test/res1
./303make test/MakefileTest tty.c > test/res2
./303make test/MakefileTest fc.h > test/res3
./303make test/MakefileTest tty > test/res4
./303make -h > test/resHelp

echo "Start Test Help"
diff test/resHelp test/result_help
echo "Test Help completed"
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
./303make test/MakefileTest tty > /dev/null
ret=$(echo $?)
if [ $ret == 0 ]
then
echo "Good Return"
else
echo "Bad Return"
fi
./303make test/MakefileTest totoy > /dev/null
ret=$(echo $?)
if [ $ret == 84 ]
then
echo "Good Return"
else
echo "Bad Return"
fi

rm test/res1 test/res2 test/res3 test/res4 test/resHelp