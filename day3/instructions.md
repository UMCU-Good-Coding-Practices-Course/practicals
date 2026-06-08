# Day 3 tutorial: Solving issues

## Exercise 1 - Debugging

Find out what is going wrong with the following code in either R or Python, using the debugger and stepping through the variables.

Where does the code break and what should you fix, to make the code work again?

### R code

```r
# Debugging exercise: incidence rates by region

regions <- data.frame(
  region = c("North", "South", "East", "West"),
  cases = c(120, 85, 0, 200),
  population = c(500000, 250000, 0, 800000)
)

calculate_incidence <- function(cases, population) {
  rate <- cases / population * 100000
  return(rate)
}

classify_risk <- function(rate) {
  if (rate > 50) {
    risk_level <- "high"
  } else {
    risk_level <- "low"
  }

  return(risk_level)
}

regions$incidence_rate <- calculate_incidence(regions$cases, regions$population)
regions$risk <- classify_risk(regions$incidence_rate)

print(regions)
```

### Python code

```python
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
Try to add errors to your code after you've written the tests. Do the tests still succeed?

## Exercise 4 - Writing efficient code

For the last exercise we're going to time different code snippets to see how much faster they run. Run the code below to see the runtime differences and write down the runtime and reason why code runs faster.
Again pick whichever language you prefer.

### 4.1 Vectorization

#### R Example

```r
# Vectorized vs non-vectorized code

x <- 1:1000000

# Non-vectorized: using a loop
y_loop <- numeric(length(x))

time_loop <- system.time({
  for (i in 1:length(x)) {
    y_loop[i] <- x[i] * 2
  }
})

# Vectorized: doing it all at once
time_vectorized <- system.time({
  y_vectorized <- x * 2
})

# Show the timings
time_loop
time_vectorized

# Check that the answers are the same
all.equal(y_loop, y_vectorized)
```

#### Python example

```python
import numpy as np
import time

x = np.arange(1_000_000)

# Non-vectorized: using a loop
y_loop = np.zeros(len(x))

start = time.time()

for i in range(len(x)):
    y_loop[i] = x[i] * 2

time_loop = time.time() - start


# Vectorized: doing it all at once
start = time.time()

y_vectorized = x * 2

time_vectorized = time.time() - start


# Show the timings
print("Loop time:", time_loop)
print("Vectorized time:", time_vectorized)

# Check that the answers are the same
print("Same answers:", np.allclose(y_loop, y_vectorized))
```

### 4.2 Caching intermediate files

#### R Example

```r
# Example: using an intermediate CSV file to avoid repeating a slow step

raw_data <- data.frame(
  age = c(23, 45, 31, 67, 52),
  smoker = c("yes", "no", "no", "yes", "no")
)

clean_data <- function(data) {
  Sys.sleep(2)  # pretend this is a slow step, e.g. cleaning a large dataset
  
  data$smoker_numeric <- ifelse(data$smoker == "yes", 1, 0)
  
  return(data)
}


# -----------------------------
# Approach 1: without intermediate file
# The slow step is done twice
# -----------------------------

start <- Sys.time()

mean_age <- mean(clean_data(raw_data)$age)
number_smokers <- sum(clean_data(raw_data)$smoker_numeric)

time_without_file <- Sys.time() - start


# -----------------------------
# Approach 2: with intermediate file
# The slow step is done once, then reused
# -----------------------------

start <- Sys.time()

cleaned <- clean_data(raw_data)
write.csv(cleaned, "cleaned_data.csv", row.names = FALSE)

cleaned_from_file <- read.csv("cleaned_data.csv")

mean_age <- mean(cleaned_from_file$age)
number_smokers <- sum(cleaned_from_file$smoker_numeric)

time_with_file <- Sys.time() - start


# Show results
time_without_file
time_with_file

mean_age
number_smokers
```

#### Python example

```python
# Example: using an intermediate CSV file to avoid repeating a slow step

import pandas as pd
import time

raw_data = pd.DataFrame({
    "age": [23, 45, 31, 67, 52],
    "smoker": ["yes", "no", "no", "yes", "no"]
})

def clean_data(data):
    time.sleep(2)  # pretend this is a slow step, e.g. cleaning a large dataset
    
    data = data.copy()
    data["smoker_numeric"] = (data["smoker"] == "yes").astype(int)
    
    return data


# -----------------------------
# Approach 1: without intermediate file
# The slow step is done twice
# -----------------------------

start = time.time()

mean_age = clean_data(raw_data)["age"].mean()
number_smokers = clean_data(raw_data)["smoker_numeric"].sum()

time_without_file = time.time() - start


# -----------------------------
# Approach 2: with intermediate file
# The slow step is done once, then reused
# -----------------------------

start = time.time()

cleaned = clean_data(raw_data)
cleaned.to_csv("cleaned_data.csv", index=False)

cleaned_from_file = pd.read_csv("cleaned_data.csv")

mean_age = cleaned_from_file["age"].mean()
number_smokers = cleaned_from_file["smoker_numeric"].sum()

time_with_file = time.time() - start


# Show results
print("Time without intermediate file:", time_without_file)
print("Time with intermediate file:", time_with_file)

print("Mean age:", mean_age)
print("Number of smokers:", number_smokers)
```
