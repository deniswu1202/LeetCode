#!/bin/bash

echo "Add modified files... ..."
git add --all > /dev/null 2>&1

echo "Commit changes... ..."
git commit -m "auto" > /dev/null 2>&1

echo "Push to origin... ..."
git push origin master > /dev/null 2>&1
