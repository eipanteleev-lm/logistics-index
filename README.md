# logistics-index

[![Build Status](https://travis-ci.com/eipanteleev-lm/logistics-index.svg?branch=master)](https://travis-ci.com/eipanteleev-lm/logistics-index)

Dashboard app for product ordering decision making.

## Summary

Determining the economic order quantity has always been one of the most important issues in inventory management. This repository proposes a data-driven custom model and dashboard app for ordering decision making, which takes into account actual for large retail companies problems, such as thefts, defects and poor data quality. 

## Repository structure

```
.
|-queries
|  |-operations.sql
|  |-operations_weekly.sql
|  |-price.sql
|-src
|  |-stats
|  |  |-distributions.py
|  |  |-negative_stock_expected_value.py
|  |  |-stock_optimum.py
|  |-app.py
|  |-config.py
|  |-connections.py
|-tests
|  |-unit
|  |  |-test_connections.py
|  |  |-test_distributions.py
|  |  |-test_negative_expected_value.py
|  |  |-test_stock_optimum.py
|  |-conftest.py
|-.dockerignore
|-.gitignore
|-.travis.yml
|-Dockerfile
|-README.md
|-requirements.txt
|-tox.ini
|-waitforweb.sh
```

## Testing

You can use `tox` for testing:

```sh
tox
```

or pytest:

```sh
python -m pytest tests/unit -vv
```

or ...

```sh
docker build -t logistics-index .
docker run --rm logistics-index -m pytest tests/unit -vv
```

## Links

App database code repository <https://github.com/eipanteleev-lm/logistics-index-db>.
