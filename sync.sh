#!/bin/bash
# Sync vault content into Quartz and push
rsync -a --delete \
  --exclude='.DS_Store' \
  --exclude='.obsidian' \
  --exclude='vc-sourcing' \
  "/Users/dani/Library/Mobile Documents/iCloud~md~obsidian/Documents/Main/pd-pipeline-research/" \
  ~/Repos/pd-pipeline-quartz/content/

# Re-copy Excel
cp ~/Downloads/PD_Pipeline_Atomic_Notes.xlsx ~/Repos/pd-pipeline-quartz/content/ 2>/dev/null

# Pre-render Dataview queries to static markdown tables
/opt/homebrew/Caskroom/miniconda/base/bin/python3 ~/Repos/pd-pipeline-quartz/prerender-dataview.py

cd ~/Repos/pd-pipeline-quartz
git add -A
git commit -m "Sync vault content $(date +%Y-%m-%d)" && git push
