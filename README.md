# logistics-index

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
|  |  |-index.py
|  |  |-negative_stock_expected_value.py
|  |  |-stock_optimum.py
|  |-app.py
|  |-config.py
|  |-connections.py
|  |-test.py
|-.dockerignore
|-.gitignore
|-Dockerfile
|-README.md
|-requirements.txt
```

## Links

App database code repository <https://github.com/eipanteleev-lm/logistics-index-db>.
