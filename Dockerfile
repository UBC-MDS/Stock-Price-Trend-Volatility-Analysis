# Docker file for the stocks prices and trends volatility analysis
# Group 30 - MDS UBC - Helin Wang, Amir Abbas Shojakhani, Julien Gordon, Dec, 2021

# Add miniconda as the base image
FROM jupyter/scipy-notebook

# Set up shell and user
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
USER root

# Update
RUN apt-get update -y

# Install mamba
RUN conda install mamba -n base -c conda-forge

# Add the required python libraries using mamba
RUN mamba install --quiet -y -c conda-forge \
    "numpy=1.21.*" \
    "pandas=1.3.*" \
    "pandas-profiling>=3.1.*" \
    "requests=2.26.*" \
    "selenium=3.141.0" \
    "altair=4.1.*" \
    "altair_saver" \
    "ipykernel=6.5.*" \
    "docopt=0.6.*" \
    "vega-cli" \
    "vega-lite-cli" && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Add the required python libraries using pip
RUN pip install \
    "altair-data-server==0.4.*"

# R pre-requisites
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    fonts-dejavu \
    gfortran \
    gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install the required R packages through mamba
RUN mamba install --quiet --yes \
    'r-base' \
    'r-docopt' \
    'r-kableExtra' \
    'r-stargazer' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Installing These R packages through mamba are not easy under arm
RUN set -x && \
    arch=$(uname -m) && \
    if [ "${arch}" == "x86_64" ]; then \
    mamba install --quiet --yes \
    'r-rmarkdown' \
    'r-tidymodels' \
    'r-tidyverse' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"; \
    fi;

# To run the analysis please install docker and run the below command at the terminal/command line
# docker run --rm -v /$(pwd):/home/analysis/stock_price_volatility_analysis stock_price_volatility_analysis make -C /home/analysis/stock_price_volatility_analysis all

# To reset the repo and remove all result files, run the below command at the terminal/command line
# docker run --rm -v /$(pwd):/home/analysis/stock_price_volatility_analysis stock_price_volatility_analysis make -C /home/analysis/stock_price_volatility_analysis clean
