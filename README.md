[![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-blueviolet.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

The material in this repository was used for the [Physics Project Days 2023](https://uclouvain.be/fr/facultes/sc/physics-project-days.html). This is a 3-day project for high-school students, where they have an introduction to programming in Python and perform a first analysis of IceCube data. It can also be combined with some activities related to the [IceCube Masterclass](https://masterclass.icecube.wisc.edu/).

The project was intially developed for the [Université Catholique de Louvain](https://uclouvain.be/en/research-institutes/irmp/cp3) in Belgium, so the instructions are written in French, but the CC BY-NC-SA license allows for any free translations to a most convenient language if you plan to use in a different context.

**Credits:** see `codemeta.json`.

# Overview

There are three main notebooks:
- `introduction_python.ipynb` contains a basic introduction to Python programming
- `project_work.ipynb` is the main notebook for students, with cells to fill
- `project_solution.ipynb` is a proposed solution to questions in `project_work.ipynb`

The slides in `slides/PPD_2023_IceCube.pdf` are distributed as reference but are not part of the Copyright License. They should not be all presented immediately, as the final part of the slides are giving some important hints (or even solutions) for questions that may raise during the project.

# Input files

There are two inputs for the analysis:
- IceCube point-source data from 2008 to 2018m to be downloaded and copied in `inputs/icecube_10year_ps` (see `install/README.md`).
- List of astrophysical sources to be probed in `inputs/sources.csv` (same list as used in [IceCube analysis](https://doi.org/10.1103/PhysRevLett.124.051103)).