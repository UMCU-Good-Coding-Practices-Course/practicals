# Day 3 tutorial: Solving issues

## Exercise 1 - Debugging

Find out what is going wrong with the following code in either R or Python, using the debugger and stepping through the variables.

Where does the code break and what should you fix, to make the code work again?

### R code

```{R}
# Debugging exercise: incidence rates by region

regions <- data.frame(
  region = c("North", "South", "East", "West"),
  cases = c(120, 85, 0, 200),
  population = c(500000, 250000, 0, 800000)
)

calculate_incidence <- function(cases, population) {
  rate <- cases / population * 100000

  if (rate > 50) {
    risk_level <- "high"
  } else {
    risk_level <- "low"
  }

  return(risk_level)
}

regions$incidence_rate <- calculate_incidence(regions$cases, regions$population)

print(regions)
```

### Python code

```{python}
# Debugging exercise: outbreak report

reports = [
    {"location": "North", "cases": 120, "population": 500000},
    {"location": "South", "cases": 85, "population": 250000},
    {"location": "East", "cases": 0, "population": 0},
    {"location": "West", "cases": "200", "population": 800000},
]


def calculate_incidence(cases, population):
    incidence = cases / population * 100000
    return incidence


def classify_risk(incidence):
    if incidence > 50:
        return "high"
    else:
        return "low"


for report in reports:
    incidence = calculate_incidence(report["cases"], report["population"])
    risk = classify_risk(incidence)

    print(report["location"] + ": " + risk + " risk")
```

## Exercise 2 - Logging

Add some useful logging to the previous code (either in R or Python).
Make sure to include information in the logs and use different log levels.

### Bonus (optional)
Write the log lines to a file (requires a third party package in R)

## Exercise 3 - Testing

Write unit tests for the functions in the previous code. Add those to a separate folder called tests. Make sure all tests succeed and all functions are tested.

## Exercise 4 - Writing efficient code

TBD



