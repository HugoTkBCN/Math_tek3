#!/bin/bash

./304pacman test/map1 '+' ' '  > test/res1
./304pacman test/map2 '@' ' ' > test/res2
./304pacman -h > test/resHelp

echo "Start Test Help"
diff test/resHelp test/result_help
echo "Test Help completed"
echo "Start test 1"
diff test/res1 test/result_1
echo "Test 1 completed"
echo "Start test 2"
diff test/res2 test/result_2
echo "Test 2 completed"
./304pacman > /dev/null
ret=$(echo $?)
if [ $ret == 84 ]
then
echo "Good Return"
else
echo "Bad Return"
fi

rm test/res1 test/res2 test/resHelp