#!/bin/bash

./301dannon test/list1 > test/res1
./301dannon test/list2 > test/res2

diff test/res1 test/result_1
diff test/res2 test/result_2

rm test/res1 test/res2