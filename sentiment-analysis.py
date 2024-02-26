import subprocess

file = 'sentiment-analysis.ipynb'
subprocess.run(['jupyter', 'nbconvert', '--execute', '--to', 'notebook', '--inplace', file])