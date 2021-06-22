# miss_hit-gallery
Crawls matlab repo. Runs static analysis. Diplays the results.

```
git clone https://github.com/spm/spm12 tmp/spm12

mh_metric --html tmp.html tmp/spm12
mh_metric --json tmp.json tmp/spm12


```

## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.
