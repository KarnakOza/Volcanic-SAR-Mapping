# Volcanic-SAR-Mapping
Volcanic Deformation &amp; Eruption mapping using Sentinel-1 SAR


![SAR](https://img.shields.io/badge/SAR-Sentinel--1-orange)
![Volcano](https://img.shields.io/badge/Volcanic-eruption-blue)
![OpenScience](https://img.shields.io/badge/Open-Science-green)

Overview
This project focuses on the detection and mapping of volcanic eruption events using Sentinel-1 C-band Synthetic Aperture Radar (SAR) data.
Understanding and monitoring surface deformation is crucial for analyzing volcanic activity, identifying underground pressure sources, and assessing associated geophysical processes.

This repository demonstrates the workflow for mapping volcanic deformation in Pico do Fogo an active stratovolcano lying on the islands of Fogo. using multi-temporal Sentinel-1 imagery. The analysis cover the period of 3rd Nov to 27th Nov 2014, aimed at identifying patterns of crustal movement and eruption-related deformation.

![image alt](https://github.com/KarnakOza/Volcanic-SAR-Mapping/blob/3687b220763ffee9ec5d41fd72aa56e818f40c1b/Volcanic-result-1.png)

# Why DInSAR?

Differential Synthetic Aperture Radar Interferometry (DInSAR) is a powerful microwave remote sensing techniques that enables the detection of Earth surface displacement with centimeters to millimeters level accuracy across large spatial scales.

DInSAR works by computing the phase differences (interferometry) between two SAR images acquired at different times over the same region. This phase difference reflects ground deformation projected along the radar Line of Sight (LOS).

Key advantages of using DInSAR include:
High spatial resolution deformation mapping,
All-weather, day-night monitoring capability,
Ability to analyze deformation trends over time,
Suitability for volcanic, seismic, and tectonic applications,

In this project, DInSAR is used to investigate the temporal evolution of surface displacement, enabling the creation of deformation time series for monitoring volcanic activity.
