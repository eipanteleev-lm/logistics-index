#!/bin/bash

http_code="400"
n=$2
while [ ${http_code} != "200" ] && [ $n -gt 0 ]
do
    http_code=$(curl -LI $1 -o /dev/null -w '%{http_code}\n' -s)

    if [ ${http_code} -eq "200" ]; then
        exit 0
    fi

    n=`expr $n - 1`
    sleep 1
done

exit 1
