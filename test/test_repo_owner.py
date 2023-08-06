#!/bin/bash

PROGRAM="$(dirname $0)/../tool/repo_owner.py"
USERNAME="4ngelf"

report(){
    RESULT="$1"
    INFO="$2"

    echo "[TEST $RESULT]: $INFO"
}

test(){
    EXPECTED="$2"
    ACTUAL=$($PROGRAM "$USERNAME" "$1")
    
    if [[ "$ACTUAL" == "$EXPECTED" ]]; then
        report "PASSED" "$ACTUAL == $EXPECTED"
    else
        report "FAILED" "$ACTUAL == $EXPECTED"
        echo "ARG: $1"
        exit 1
    fi
}

test_fail(){
    EXPECTED=1

    $PROGRAM "$USERNAME" "$1" &>/dev/null
    ACTUAL=$?
    
    if [[ $ACTUAL -eq $EXPECTED ]]; then
        report "PASSED" "$ACTUAL == $EXPECTED"
    else
        report "FAILED" "$ACTUAL == $EXPECTED"
        echo "ARG: $1"
        exit 1
    fi
}


echo "------------------------------------------------------------"
echo "TESTING $PROGRAM"
echo "------------------------------------------------------------"

test "git@gitlab.com:volian/nala.git" "third"
test "https://gitlab.com/volian/nala.git" "third"
test "git@github.com:4ngelf/mysite.git" "personal"
test "https://github.com/4ngelf/mysite.git" "personal"
test_fail "" 
test_fail "github.com:4ngelf/mysite.git"
test_fail "https://github.com/mysite.git" 
test_fail "git@gitlab.com:volian/nala"

echo "------------------------------------------------------------"
echo "ALL PASSED!"
echo "------------------------------------------------------------"

exit 0
