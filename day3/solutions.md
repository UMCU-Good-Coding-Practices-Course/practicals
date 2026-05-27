## Exercise 1

### R solution

```{R}
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

regions$incidence_rate <- mapply(
  calculate_incidence,
  regions$cases,
  regions$population
)

regions$risk_level <- ifelse(
  regions$incidence_rate > 50,
  "high",
  "low"
)

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

calculate_incidence <- function(cases, population, region) {
  message("Calculating incidence for region: ", region)

  if (cases < 0) {
    stop("Cases cannot be negative in region: ", region)
  }

  if (population < 0) {
    stop("Population cannot be negative in region: ", region)
  }

  if (population == 0) {
    warning("Population is zero in region: ", region, 
            ". Incidence rate cannot be calculated.")
    return(NA)
  }

  if (cases == 0) {
    message("No cases reported in region: ", region)
  }

  rate <- cases / population * 100000

  message("Incidence rate for ", region, " is ", round(rate, 2))

  return(rate)
}

regions$incidence_rate <- mapply(
  calculate_incidence,
  regions$cases,
  regions$population,
  regions$region
)

regions$risk_level <- ifelse(
  is.na(regions$incidence_rate),
  "unknown",
  ifelse(regions$incidence_rate > 50, "high", "low")
)

print(regions)
```

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


for report in reports:
    incidence = calculate_incidence(
        report["cases"],
        report["population"],
        report["location"]
    )

    risk = classify_risk(incidence, report["location"])

    print(report["location"] + ": " + risk + " risk")
```