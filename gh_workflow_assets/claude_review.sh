#!/bin/bash
RESULT=$(claude -p "Review the python code in this project for vulnerabilities. If no security vulnerabilities are found then just respond 0")

echo "$RESULT"

if [ "$RESULT" != "0" ]; then
  exit 1
fi