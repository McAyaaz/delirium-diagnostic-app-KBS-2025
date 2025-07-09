#!/bin/bash
# Automatically add, commit, and push changes to GitHub

# Add all changes
git add .

# Commit with a timestamp
git commit -m "Auto-update: $(date)"

# Push to the main branch
git push origin main
