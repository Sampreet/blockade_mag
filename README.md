# Quantum Interference Induced Magnon Blockade and Antibunching in a Hybrid Quantum System

[![Manuscript Version](https://img.shields.io/badge/manuscript-v2.6-red?style=for-the-badge)](https://doi.org/10.1364/JOSAB.507012)
[![Toolbox Version](https://img.shields.io/badge/qom-v1.0.1-red?style=for-the-badge)](https://sampreet.github.io/qom-docs/v1.0.1)
[![Last Updated](https://img.shields.io/github/last-commit/sampreet/blockade_mag?style=for-the-badge)](https://github.com/sampreet/blockade_mag/blob/master/CHANGELOG.md)

> J. Opt. Soc. Am. B 41, 1 (2024)

Author | Affiliation
------------ | -------------
[Pooja Kumari Gupta](https://www.iitg.ac.in/stud/pooja.kumari/) | Indian Institute of Technology Guwahati, Guwahati-781039, India
[Sampreet Kalita](https://www.iitg.ac.in/stud/sampreet/) | Indian Institute of Technology Guwahati, Guwahati-781039, India
[Amarendra Kumar Sarma](https://www.iitg.ac.in/aksarma/) | Indian Institute of Technology Guwahati, Guwahati-781039, India

Contributing Part | PKG | SK
------------ | ------------ | -------------
Literature review | 90% | 10%
Idea and formulation | 100% | 0%
Derivations of expressions | 60% | 40%
Parameter sweeping | 90% | 10%
Illustrations and plots | 50% | 50%
Results and discussion | 60% | 40%
Manuscript preparation | 70% | 30%

## About the Work

In this work, we study the phenomena of quantum interference assisted magnon blockade and magnon antibunching in a weakly interacting hybrid ferromagnet-superconductor system.
The magnon excitations in two yttrium iron garnet spheres are indirectly coupled to a superconducting qubit through microwave cavity modes of two mutually perpendicular cavities.
We find that when one of the magnon mode is driven by a weak microwave field, the destructive interference between more than two distinct transition pathways restricts simultaneous excitation of two magnons.
We analyze the magnon correlations in the driven magnon mode for the case of zero detunings as well as finite detunings of the magnon modes and the qubit.
We show that the magnon antibunching can be tuned by changing the magnon-qubit coupling strength ratio and the driving detuning.
Our work proposes a possible scheme which have significant role in the construction of single magnon generating devices.

## Notebooks

* [Blockade Condition](notebooks/blockade_condition.ipynb)
* [Plots in the Latest Version of the Manuscript](notebooks/v2.6_qom-v1.0.1/plots.ipynb)

## Structure of the Repository

```
ROOT_DIR/
|
├───common/
│   ├───foo.py
│   └───...
|
├───notebooks/
│   ├───bar/
│   │   ├───baz.ipynb
│   │   └───...
│   │
│   ├───foo.ipynb
│   └───...
|
│───scripts/
│   ├───bar/
│   │   ├───baz.py
│   │   └───...
│   └───...
│
├───.gitignore
├───CHANGELOG.md
└───README.md
```

Here, `bar` represents the version.

## Installing Dependencies

All numerical values are calculated using [QuTiP](https://github.com/qutip/qutip), a Python framework for the dynamics of open quantum systems.
Refer to the [QuTiP documentation](https://qutip.org/docs/latest) for the steps to install this library.

All plots are obtained using the [Quantum Optomechanics Toolbox](https://github.com/sampreet/qom), an open-source Python framework to simulate optomechanical systems.
Refer to the [QOM toolbox documentation](https://sampreet.github.io/qom-docs/v1.0.1) for the steps to install this libary.

## Running the Scripts

To run the scripts, navigate *inside* the top-level directory, and execute:

```bash
python scripts/bar/baz.py
```

Here, `bar` is the name of the folder (containing the version information) inside `scripts` and `baz.py` is the name of the script (refer to the repository structure).