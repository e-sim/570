#!/bin/sh
#author: Erica Sim
# $1 = fsm file $2 = word list

while read curr; do
   
	RESULT="$(echo $curr | sed -e 's/\(.\)/\1 /g' | carmel -sli $1 2>&1)"
	if [[ $RESULT =~ .*Empty.* ]] #stderr says "Empty or invalid..." w/ no match
	then
        #echo "$RESULT"
		echo "$curr => no" 
	else
        #echo "$RESULT"
		echo "$curr => yes"
	fi
done < $2