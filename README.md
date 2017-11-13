# InterPop

## Introduction
InterPop is API for render graph of internet usage in Thailand.
It's convert excel file (.xlsx) to CSV file, then return rendered csv to graph.
That make you easy to do data analysis.


## Requirement
* Python 3 with follow modules
  * Pandas
  * Pygal
  * Django

## Plan

### Function

| # | Function Name | Parameter         | Note |
| - | ------------- | ----------------- | ---- |
| 1 | main          | use, year, filter | Main |
| 2 | com           | filter, year      | Sub  |
| 3 | internet      | filter, year      | Sub  |
| 4 | mobile        | filter, year      | Sub  |

### Server API

Using Django
