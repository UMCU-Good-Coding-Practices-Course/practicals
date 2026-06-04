## Exercise 1

### R solution

```{R}
# Debugging exercise: incidence rates by region

regions <- data.frame(
  region = c("North", "South", "East", "West"),
  cases = c(120, 85, 0, 200),
  population = c(500000, 250000, 0, 800000)
)

calculate_incidence <- function(cases, population) {
  if (population == 0) {
    return(NA)
  }
  rate <- cases / population * 100000
  return(rate)
}

classify_risk <- function(rate) {
  risk_level <- ifelse(rate > 50, "high", "low")

  return(risk_level)
}

regions$incidence_rate <- mapply(calculate_incidence, regions$cases, regions$population)
regions$risk <- classify_risk(regions$incidence_rate)

print(regions)
```

### Python solution

```{python}
reports = [
    {"location": "North", "cases": 120, "population": 500000},
    {"location": "South", "cases": 85, "population": 250000},
    {"location": "East", "cases": 0, "population": 0},
    {"location": "West", "cases": 200, "population": 800000},
]


def calculate_incidence(cases, population):
    if population == 0:
        return None

    incidence = cases / population * 100000
    return incidence


def classify_risk(incidence):
    if incidence is None:
        return "unknown"

    if incidence > 50:
        return "high"
    else:
        return "low"


for report in reports:
    incidence = calculate_incidence(report["cases"], report["population"])
    risk = classify_risk(incidence)

    print(report["location"] + ": " + risk + " risk")
```

## Exercise 2

### R solution

```{R}
regions <- data.frame(
  region = c("North", "South", "East", "West"),
  cases = c(120, 85, 0, 200),
  population = c(500000, 250000, 0, 800000)
)

calculate_incidence <- function(cases, population) {
  message("Calculating incidence")

  if (cases < 0) {
    stop("Cases cannot be negative")
  }

  if (population < 0) {
    stop("Population cannot be negative")
  }

  if (population == 0) {
    warning("Population is zero. Incidence rate cannot be calculated.")
    return(NA)
  }

  if (cases == 0) {
    message("No cases reported in region")
  }

  rate <- cases / population * 100000

  message("Incidence rate for is ", round(rate, 2))

  return(rate)
}

classify_risk <- function(rate) {
  risk_level <- ifelse(rate > 50, "high", "low")

  return(risk_level)
}

regions$incidence_rate <- mapply(calculate_incidence, regions$cases)
regions$risk <- classify_risk(regions$incidence_rate)

print(regions)
```

### Python solution
```{python}
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


reports = [
    {"location": "North", "cases": 120, "population": 500000},
    {"location": "South", "cases": 85, "population": 250000},
    {"location": "East", "cases": 0, "population": 0},
    {"location": "West", "cases": 200, "population": 800000},
]


def calculate_incidence(cases, population, location):
    """Compute incidence per 100k people"""
    logging.info("Calculating incidence for location: %s", location)

    if cases < 0:
        logging.error("Cases cannot be negative in location: %s", location)
        raise ValueError("Cases cannot be negative")

    if population < 0:
        logging.error("Population cannot be negative in location: %s", location)
        raise ValueError("Population cannot be negative")

    if population == 0:
        logging.warning(
            "Population is zero in location: %s. Incidence cannot be calculated.",
            location
        )
        return None

    if cases == 0:
        logging.info("No cases reported in location: %s", location)

    incidence = cases / population * 100000

    logging.info("Incidence for %s is %.2f", location, incidence)

    return incidence


def classify_risk(incidence, location):
    logging.info("Classifying risk for location: %s", location)

    if incidence is None:
        logging.warning("Risk level is unknown for location: %s", location)
        return "unknown"

    if incidence > 50:
        logging.info("Risk level for %s is high", location)
        return "high"
    else:
        logging.info("Risk level for %s is low", location)
        return "low"


if __name__ == "__main__":
    for report in reports:
        incidence = calculate_incidence(
            report["cases"],
            report["population"],
            report["location"]
        )
    
        risk = classify_risk(incidence, report["location"])
    
        print(report["location"] + ": " + risk + " risk")
```

## Exercise 3
### R solution

You can find an example R solution `solution_test_R`


```
<project_folder>/
├── my_file.R  # where you placed your code
│
└── tests/
    └── testthat/
        └── test-my_file.R
```

```{r}
install.packages("devtools")
install.packages("testthat")
````


```{r}
# File: tests/testthat/test-my_file.R

source("../../my_file.R")

test_that("calculate_incidence works", {
  expect_equal(calculate_incidence(5, 1e6), 0.5)
  expect_equal(calculate_incidence(0, 1), 0)
  expect_warning(result <- calculate_incidence(0, 0), "Population is zero. Incidence rate cannot be calculated.")
  expect_true(is.na(result))
})

test_that("classify_risk works", {
  expect_equal(classify_risk(NA_real_), NA)
  expect_equal(classify_risk(5), "low")
  expect_equal(classify_risk(50), "low")
  expect_equal(classify_risk(100), "high")
})

```

Run tests from `<project_folder>` with:

```{r}
testthat::test_dir("tests/testthat")
```

Or open the test file and press "Run Tests"

### Python solution
You can find an example solution in the folder `solution_test_python`. 
It contains two files, one for which the test fails (`my_file_bad.py`) and one for which it passes (`my_file.py`).

```
<project_folder>/
├── my_file.py  # where you placed your code
│
├── tests/
│   ├── __init__.py
│   └── test_my_file.py
```

```{python}
# File: tests/test_my_file.py

from my_file import calculate_incidence, classify_risk

def test_calculate_incidence():
    assert calculate_incidence(5, 1e6) == 0.5
    assert calculate_incidence(0, 1) == 0
    assert calculate_incidence(0, 0) is None

def test_classify_risk():
    assert classify_risk(None) == "unknown"
    assert classify_risk(5) == "low"
    assert classify_risk(50) == "low"
    assert classify_risk(100) == "high" 
```
