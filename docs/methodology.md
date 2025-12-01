# Methodology: Volcanic Deformation Mapping Using Sentinel-1 SAR

This document explains the complete processing workflow used to detect volcanic deformation and eruption-related changes using Sentinel-1 Synthetic Aperture Radar (SAR) data.

---

1. **Data Acquisition**
- Sentinel-1 IW SLC images  
- Pre-eruption and post-eruption acquisitions  
- Orbit files (Precise Orbit Ephemerides)

---

2. **SNAP Processing Workflow**
   
3. **TOPS Split**  
   - IW3 Subswath  
   - VV Polarization  
   - Bursts 1–2
     
4. **Apply Orbit File**
5. **Back Geocoding**  
   - DEM: SRTM 3Sec  
   - DEM Resampling: Bilinear  
   - Output: Deramp & Demod Phase  
   - Mask out areas with no elevation
     
6. **Enhanced Spectral Diversity (ESD)**  
   - Window width/height: 512  
   - Search accuracy range/azimuth: 16  
   - Oversampling: 128  
   - Thresholds: 0.1 (CC), 0.15 (coherence)  
   - Windows per overlap: 10  
   - Azimuth & Range Shift: 0
     
7. **Interferogram Formation**  
   - Subtract flat-earth phase  
   - Flat-earth polynomial degree: 5  
   - Estimation points: 501  
   - Orbit interpolation: degree 3  
   - Coherence estimation: range 10, azimuth 2
     
8. **TOPS Deburst** 
9. **Topographic Phase Removal**  
   - DEM: SRTM 3Sec  
   - Tile extension: 100
     
10. **Goldstein Phase Filtering**  
   - Adaptive filter factor: 1.0  
   - FFT Size: 64  
   - Coherence mask threshold: 0.2
     
11. **Range Doppler Terrain Correction**  
    - Source band: Phase & Coherence 
    - Output: Phase_ifg_VV & coh_IW3_VV






