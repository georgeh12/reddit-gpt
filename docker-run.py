import subprocess

subprocess.Popen(['mlflow', 'ui', '-h', '0.0.0.0'])

for file in ['sentiment-analysis.ipynb', 'model-training.ipynb']:
    subprocess.run(['jupyter', 'nbconvert', '--execute', '--to', 'notebook', '--inplace', file])

