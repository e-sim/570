#!/bin/sh
#author: Erica Sim
# $1 = fsm file $2 = word list

while read curr; do
   
	RESULT="$(echo $curr | sed -e 's/\(.\)/\1 /g' | carmel -sli $1 2>&1)"
	if [[ $RESULT =~ .*Empty.* ]] #stderr says "Empty or invalid..." w/ no match
	then
		echo "$curr => *NONE*" 
	else
        RESULT="$(echo "\"$RESULT\""  | grep -e '\*e\*' | sed -r 's/\([0-9]+ \([0-9]+ (.*)\)\)/\1/g')"
        RESULT="$(echo "$RESULT"  | sed -r 's/ \*e\*$//g' | sed -r 's/^\*e\* (.*)$/\/\1 /g' | tr -d '\n')"
		echo "$curr => $RESULT"
	fi
done < $2