#!/bin/bash

find ~/Workspace/Stacking-Audio-Tag/ -name "*.pyc" -exec rm {} \;
find ~/Workspace/Stacking-Audio-Tag/ -name "*.DS_Store" -exec rm {} \;
find ~/Workspace/Stacking-Audio-Tag/ -name "*__pycache__" -exec rm -rf {} \;
