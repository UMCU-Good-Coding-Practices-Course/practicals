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
