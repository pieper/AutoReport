# Research Report: Liver-Kidney-Data
*Generated: 2026-03-30 UTC*

## Executive Summary

This report details freely available datasets for liver and kidney research, focusing on high-quality scans, patient numbers, annotation availability, and clinical data. Several new resources have emerged, including the Blood–Liver–Kidney Tri-Organ Imaging Dataset and enhancements to existing platforms like the NCI Imaging Data Commons. Emphasis is placed on datasets with non-restrictive licenses, particularly CC-BY. The Duke Liver Dataset and ATLAS dataset are highlighted for their comprehensive annotations of liver conditions, while the C4KC-KITS dataset provides valuable kidney tumor segmentations. The ongoing development of AI in medical imaging continues to drive the creation of larger, more annotated datasets.

## Key Announcements by Organization

### NCI Imaging Data Commons (IDC)

*   **Expansion and Licensing:** As of Spring 2025, the IDC houses over 85 TB of data, including radiology and pathology images, with accompanying annotations, segmentations, and clinical data. A significant majority (>95%) of the data is available under the permissive CC-BY license, facilitating commercial reuse.
*   **Data Types:** IDC includes clinical and preclinical imaging, such as CT, MRI, and PET scans, alongside digital pathology, multispectral microscopy, annotations, parametric maps, radiomics features, and expert assessments.
*   **Integration:** IDC serves as a node within the NCI Cancer Research Data Commons (CRDC) infrastructure, providing harmonized data in DICOM format.

### The Cancer Imaging Archive (TCIA)

*   **CPTAC-CCRCC-TUMOR-ANNOTATIONS:** This dataset provides annotations for the Clear Cell Renal Cell Carcinoma Collection, with rigorous review by radiologists to ensure accuracy.
*   **C4KC-KITS:** This collection includes CT scans and segmentations for 210 patients from the Kidney and Kidney Tumor Segmentation Challenge (KiTS19), featuring manual segmentations of kidneys and tumors.
*   **Licensing:** Most datasets on TCIA are freely available for commercial, scientific, and educational purposes under Creative Commons Attribution licenses (3.0 Unported or 4.0 International).

### Kaggle

*   **Blood–Liver–Kidney Tri-Organ Imaging Dataset:** Released with an MIT License (public domain), this dataset is designed for object detection and tissue classification, featuring blood cell detection, liver tissue analysis, and kidney tissue analysis. It aims to support multi-sample correlation analysis across different tissue types.

### University of Florida (IC3)

*   **Kidney Image Datasets:** IC3 offers digital whole slide images (WSIs) of periodic-acid Schiff stained brightfield microscopy and corresponding spatial omics labeled fluorescence microscopy WSIs of kidney tissue.

## Notable Papers and Datasets

*   **ATLAS Dataset:** This dataset provides contrast-enhanced MRI (CE-MRI) of Hepatocellular Carcinoma (HCC) with annotations for liver and liver tumors, making it the first public dataset of its kind for HCC CE-MRI.
*   **Duke Liver Dataset:** Containing 2146 abdominal MRI series from 105 patients, this dataset includes over 113,000 images and provides manually segmented liver masks for 310 series, supporting liver segmentation model development.
*   **CancerLivER:** This resource integrates 115 annotated datasets for liver cancer, encompassing expression profiles with clinical information for 9611 samples, and provides information on 594 potential biomarkers.
*   **LiMT (Liver Multi-Task Dataset):** This publicly available 3D CT dataset includes 150 cases annotated for both anatomy and lesion types, supporting multi-task analysis for liver-related tasks like segmentation, classification, and detection.
*   **Primary Liver Cancer CECT Imaging Dataset:** This dataset comprises 278 cases of liver cancer (HCC, ICC, cHCC-CCA) and 83 non-liver cancer subjects, with annotated liver and lesion regions across complete CT phases (Plain, Arterial, Venous, Delayed).
*   **Kidney Cancer RNA-seq Dataset (TCGA):** The TCGA Kidney Cancers Dataset is a bulk RNA-seq dataset with transcriptome profiles of 1024 patients diagnosed with three different subtypes of kidney cancers.
*   **Dartmouth Kidney Cancer Histology Dataset:** This dataset consists of 563 H&E-stained whole-slide images of renal cell carcinoma (RCC), labeled for predominant histological patterns.

## What to Watch

*   **NCI Imaging Data Commons (IDC):** Continued expansion and addition of new collections are expected, with a focus on maintaining the CC-BY license for broad accessibility.
*   **CARE-Liver:** This initiative focuses on liver fibrosis staging and segmentation using multi-phase MRI data. The CARE2024 dataset included 610 patients, with an anticipated increase in cases for future iterations.
*   **PYCAD:** This platform aims to curate medical imaging datasets, with specific datasets for kidney CT and MRI segmentation listed for release in 2026.

## Possible Clinical Relevance

The availability of high-quality, annotated datasets is crucial for advancing AI in medical diagnostics and treatment planning. Datasets like ATLAS and the Duke Liver Dataset are instrumental for developing automated liver and tumor segmentation tools, which can aid in treatment planning for liver cancer patients. Similarly, datasets such as C4KC-KITS and the Dartmouth Kidney Cancer Histology Dataset support the development of AI models for kidney tumor segmentation and classification, respectively, potentially leading to earlier and more accurate diagnoses. The inclusion of comprehensive clinical data, as seen in the IDC and some PLCO datasets, enables the development of predictive models for disease progression and patient outcomes, facilitating personalized medicine approaches for both liver and kidney diseases. The Blood-Liver-Kidney Tri-Organ Imaging Dataset offers a unique opportunity to explore multi-organ correlations in disease.

## Sources

*   CancerLivER: a database of liver cancer gene expression resources and biomarkers - PMC.
*   A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma - MDPI.
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC.
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset.
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels.
*   Imaging Data Commons | CRDC.
*   CPTAC-CCRCC-TUMOR-ANNOTATIONS - The Cancer Imaging Archive (TCIA).
*   Medical Imaging Datasets - PYCAD.
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset.
*   LiMT: a multi-task liver image benchmark dataset - arXiv.
*   Liver - Datasets - PLCO - The Cancer Data Access System. https://cdas.cancer.gov/plco/datasets/liver/
*   Primary Liver Cancer CECT Imaging Dataset.
*   Data Usage Policies and Restrictions - The Cancer Imaging Archive (TCIA).
*   TCGA Kidney Cancers - UCI Machine Learning Repository.
*   Public Medical Image Datasets for Segmentation Foundation Models. 
*   m-aryayi/Medical-Imaging-Datasets: Publicly available medical imaging datasets for research and analysis. - GitHub. https://github.com/m-aryayi/Medical-Imaging-Datasets
*   Medical Imaging Datasets - Intelligent Clinical Care Center (IC3) » » University of Florida.
*   Open Kidney Dataset | kidneyUS. 
*   CPTAC-CCRCC-TUMOR-ANNOTATIONS - The Cancer Imaging Archive (TCIA).
*   usage examples for datasets listed in this registry tagged with medical image computing. 
*   Multi-modality medical image dataset for medical image processing in Python lesson. https://zenodo.org/record/14032428
*   Public Data in Nephrology: A Researcher's Roadmap - PMC - NIH.
*   C4KC-KITS - The Cancer Imaging Archive (TCIA).
*   GitHub - cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification. https://github.com/cradleai/LKS-Dataset
*   18 Open Healthcare Datasets — 2025 Update | by ODSC. https://www.datasciencecentral.com/18-open-healthcare-datasets-2025-update/
*   Medical Imaging Datasets: 2026 Resource Guide - Collective Minds.
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series LabelsRadiology: Artificial Intelligence - RSNA Journals.
*   A synthetic dataset of liver disorder patients - PMC - NIH. 
*   CARE-Liver.
*   20 Best Free Healthcare Datasets for ML in 2026 - Unidata.
*   Best Public Datasets for Health Data Science Projects - Health Innovation Newsletter.
*   Diagnosing and Characterizing Chronic Kidney Disease with Machine Learning: The Value of Clinical Patient Characteristics as Evidenced from an Open Dataset - MDPI.
*   (PDF) Public Data in Nephrology: A Researcher's Roadmap - ResearchGate.