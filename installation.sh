#!/bin/bash

# List all the exercise folders you want to iterate over
exercises=("exercise2" "exercise3" "exercise5")  # Add all your task directories here

# Iterate over each folder and run 'poetry install'
for exercise in "${exercises[@]}"; do
  echo "Installing dependencies for $exercise..."
  cd "$exercise"
  poetry install
  cd ..
done
