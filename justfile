init:
    @pip install -r requirements.txt >/dev/null 2>&1

generate-requirements:
    @pip freeze > requirements.txt

setup:
    #!/usr/bin/env bash
    if [ "$(which direnv)" == "" ]; then
        echo "direnv is not installed"
    fi

test: init
    @python -m pytest -s

coverage: init
    @python -m coverage report --omit="*/test*"

coverage-html: init
    @python -m coverage html --omit="*/test*"

lint: init
    @python -m pylint src

prospector: init
    @python -m prospector
