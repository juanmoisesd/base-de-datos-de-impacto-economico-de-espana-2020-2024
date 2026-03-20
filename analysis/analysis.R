# analysis.R — Base de Datos de Impacto Económico de España (2020-2024)
# DOI: 10.5281/zenodo.18879794
# Author: de la Serna Tuya, Juan Moisés · ORCID: 0000-0002-8401-8018
# License: CC0 1.0

# ── SETUP ──────────────────────────────────────────────────────────────────
# Install required packages if needed:
# install.packages(c("readr","ggplot2","dplyr","tidyr"))

library(readr)
library(ggplot2)
library(dplyr)

# ── LOAD DATA ──────────────────────────────────────────────────────────────
# Download dataset from: https://doi.org/10.5281/zenodo.18879794
# df <- read_csv("dataset.csv")

# Example with synthetic data
set.seed(42)
years <- 2000:2023
df <- data.frame(
  year = years,
    españa = rnorm(length(years), 50, 15),
  macroeconomí = rnorm(length(years), 50, 15),
  pib = rnorm(length(years), 50, 15),
  inflación = rnorm(length(years), 50, 15),
  stringsAsFactors = FALSE
)

cat("Dataset: Base de Datos de Impacto Económico de España (2020\n")
cat("DOI: 10.5281/zenodo.18879794\n")
cat("Dimensions:", nrow(df), "x", ncol(df), "\n\n")
print(head(df))
print(summary(df))

# ── VISUALIZATION ──────────────────────────────────────────────────────────
# Temporal trend
p1 <- df %>%
  tidyr::pivot_longer(-year, names_to="variable", values_to="value") %>%
  ggplot(aes(x=year, y=value, color=variable)) +
  geom_line(size=0.8) +
  geom_point(size=1.5) +
  labs(title="Base de Datos de Impacto Económico de España (2020-2024",
       subtitle="DOI: 10.5281/zenodo.18879794",
       x="Year", y="Value",
       caption="de la Serna Tuya, Juan Moisés · 2026") +
  theme_minimal() +
  theme(legend.position="bottom")

ggsave("figures/analysis_output_r.png", p1, width=10, height=6, dpi=150)
cat("\nFigure saved: figures/analysis_output_r.png\n")

# ── CITATION ───────────────────────────────────────────────────────────────
cat("\nCitation:\n")
cat("de la Serna Tuya, Juan Moisés (2026). Base de Datos de Impacto Económico de España (2020-2024). Zenodo. https://doi.org/10.5281/zenodo.18879794\n")
