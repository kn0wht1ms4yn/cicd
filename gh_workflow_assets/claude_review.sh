#!/bin/bash
set -x
RESULT=$(npx --yes @anthropic-ai/claude-code -p "Review the python code in this project for vulnerabilities. If no security vulnerabilities are found then just respond 0")

echo "$RESULT"

if [ "$RESULT" != "0" ]; then
  exit 1
fi