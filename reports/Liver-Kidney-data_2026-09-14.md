# Research Report: Liver-Kidney-Data
*Generated: 2026-09-14 UTC*

## Executive Summary

This report identifies and evaluates publicly available datasets for liver and kidney imaging, with a focus on cancer-related studies. Several datasets offer rich annotations, large patient cohorts, and diverse scan types, making them valuable resources for AI development. Recent datasets, particularly those focusing on specific cancer subtypes and incorporating multi-modal data, represent advancements in the field. The identified datasets generally have non-restrictive licenses, favoring CC-BY, aligning with the need for open research. Clinical relevance is high, as these datasets can drive the development of more accurate diagnostic and prognostic tools for liver and kidney diseases, including cancers.

## Key Announcements by Organization

### The Cancer Imaging Archive (TCIA)

TCIA hosts a significant number of medical imaging datasets, including those relevant to liver and kidney research. They provide access to datasets like the Lung Image Database Consortium (LIDC) / Image Database Resource Initiative (IDRI) for lung nodules, and collections related to kidney tumors such as KiTS19/21 and KiTS23. TCIA also houses the HCC-TACE-SEG dataset for hepatocellular carcinoma and the TCGA Liver Hepatocellular Carcinoma (LIHC) collection. These datasets are crucial for developing and validating AI models.

### National Institutes of Health (NIH) / The Cancer Genome Atlas (TCGA)

TCGA provides extensive genomic and clinical data, often paired with imaging data available through TCIA. Datasets derived from TCGA, such as those for renal cell carcinoma (RCC), are highlighted. The RCC-AID dataset, for instance, offers annotated CT scans for segmentation, detection, and classification of RCC subtypes. Similarly, TCGA-LIHC is a collection of liver hepatocellular carcinoma data, and TCGA Kidney Cancers dataset offers bulk RNA-seq data for kidney cancer subtypes.

### Kaggle and Zenodo

These platforms host a variety of datasets, often curated by researchers. Kaggle features datasets like the Liver Cancer Multiclass Dataset, Annotated Ultrasound Liver images Dataset, Kidney Failure Ultrasound (Clinical Images), and CT KIDNEY DATASET. Zenodo hosts the RCC-AID dataset with links to annotations. These platforms offer accessibility and ease of download for many research projects.

### Research Institutions and Universities (e.g., Duke University, UCSF, University of Florida)

Several institutions contribute high-quality, specialized datasets.
*   **Duke University** offers the Duke Liver Dataset, a large MRI dataset with liver segmentation masks for cirrhosis studies.
*   **University of California, San Francisco (UCSF)** provides the UCSF Renal Mass CT Dataset, a multiphase CT exam dataset for renal masses with annotations.
*   **University of Florida** (Intelligent Clinical Care Center - IC3) lists various medical imaging datasets, including kidney image datasets with spatial omics and labeled fluorescence microscopy.

## Notable Papers and Datasets

*   **Duke Liver Dataset:** A comprehensive MRI dataset with over 2000 series from 105 patients, including liver segmentation masks, useful for developing liver segmentation and classification models.
*   **LiverHccSeg:** This dataset focuses on hepatocellular carcinoma (HCC) and provides manual segmentations of the liver and HCC tumors by two radiologists, enabling robust algorithm evaluation.
*   **LIDC/IDRI:** A foundational dataset for lung nodule research, containing 1018 thoracic CT scans with detailed annotations from four radiologists, serving as a benchmark for CAD systems.
*   **RCC-AID:** A recent dataset providing voxel-level annotations of kidneys and lesions from CT scans of renal cell carcinoma patients, supporting AI research in detection and classification.
*   **ATLAS Dataset:** The "Tumour and Liver Automatic Segmentation" (ATLAS) dataset is highlighted as the first public dataset providing CE-MRI of HCC with both liver and tumor segmentations.
*   **LiMT:** A new multi-task liver image benchmark dataset with CT volumes from 150 cases, including four types of liver diseases and normal cases, with annotations by clinicians.
*   **KiTS Dataset (KiTS19/21/23):** Datasets for kidney and kidney tumor segmentation challenges, offering hundreds of CT scans with segmentations of kidneys and tumors, crucial for advancing AI in renal cancer treatment planning.
*   **UCSF Renal Mass CT Dataset:** Features 831 3D multiphase CT exams of renal masses with annotations and pathology metadata, valuable for developing classification models.
*   **NAFLD Ultrasound Dataset:** Includes ultrasound images and clinical data for classifying Non-Alcoholic Fatty Liver Disease (NAFLD) severity, notable for its multi-modal approach and CC BY 4.0 license.
*   **Open Kidney Dataset:** Provides over 500 2D B-mode abdominal ultrasound images with polygon annotations for kidney analysis, specifically addressing the lack of open ultrasound data.

## What to Watch

*   **Newer Cancer-Specific Datasets:** Datasets like RCC-AID and the UCSF Renal Mass CT Dataset represent a trend towards more specific cancer subtyping and detailed annotations, which will be crucial for advanced AI models.
*   **Multi-Modal Data Integration:** Datasets incorporating both imaging and clinical/genomic data (e.g., NAFLD Ultrasound Dataset, TCGA collections) are becoming more prevalent, enabling more holistic AI approaches.
*   **Ongoing Challenges:** Continued releases from challenges like KiTS (Kidney Tumor Segmentation) will provide updated and expanded datasets for specific tasks.

## Possible Clinical Relevance

The datasets discussed have significant clinical relevance, primarily in advancing **diagnostic accuracy and treatment planning** for liver and kidney diseases, especially cancers.

*   **Early Detection and Diagnosis:** Datasets with detailed annotations for various cancer subtypes (e.g., RCC subtypes in RCC-AID, HCC in ATLAS and LiverHccSeg) can train AI models to detect and classify lesions with higher precision, potentially at earlier stages.
*   **Treatment Planning and Guidance:** Segmentation datasets for tumors (e.g., KiTS, ATLAS) are vital for surgical planning, radiation therapy, and interventional procedures. The accuracy of these segmentations directly impacts treatment efficacy and patient outcomes.
*   **Prognosis and Outcome Prediction:** Datasets incorporating clinical and genomic data alongside imaging can help develop models that predict disease progression, treatment response, and patient survival, enabling personalized medicine approaches.
*   **Reducing Inter-Observer Variability:** Standardized, well-annotated datasets allow for the training of AI models that can provide consistent interpretations, reducing the variability often seen between human experts.
*   **Facilitating Research and Development:** The availability of diverse, high-quality, and openly licensed datasets accelerates research into novel AI algorithms and diagnostic tools, ultimately translating into improved patient care.

## Sources

*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC.
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC.
*   The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A Completed Reference Database of Lung Nodules on CT Scans - PMC.
*   RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research | medRxiv.
*   Liver Cancer Multiclass Dataset - Kaggle.
*   Dataset on NAFLD Severity Classification with Ultrasound Liver Image & Clinical Data.
*   Primary Liver Cancer CECT Imaging Dataset.
*   RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research - Zenodo.
*   A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma - MDPI.
*   LiMT: a multi-task liver image benchmark dataset - arXiv.
*   Publicly available medical imaging datasets for research and analysis. · GitHub.
*   Lung Nodule Segmentation (LIDC-IDRI) — Preparing Data for Inference | by Hannah Do.
*   LIDC-annot-NLST501 - The Cancer Imaging Archive (TCIA).
*   Medical Imaging Datasets - Intelligent Clinical Care Center (IC3) » » University of Florida.
*   Enhanced Pulmonary Nodule Detection and Classification Using Artificial Intelligence on LIDC-IDRI Data.
*   LIDC-IDRI - The Cancer Imaging Archive (TCIA).
*   Kidney Failure Ultrasound (Clinical Images) - Kaggle.
*   AI in Medical Imaging: The Kidney Tumor Segmentation Challenge | Banook.
*   Annotated Ultrasound Liver images Dataset - Kaggle.
*   LiMT: A Multi-task Liver Image Benchmark Dataset - GitHub.
*   C4KC-KITS - The Cancer Imaging Archive (TCIA).
*   MMIST ccRCC Dataset.
*   UCSF Renal Mass CT Dataset - Registry of Open Data on AWS.
*   HCC-TACE-SEG - The Cancer Imaging Archive (TCIA).
*   Open Kidney Dataset | kidneyUS.
*   UCSF RMaC: University of California San Francisco 3D Multi-Phase Renal Mass CT Dataset with Tumor Segmentations | medRxiv.
*   Axial CT Imaging Dataset for AI-Powered Kidney Stone Detection: A Resource for Deep Learning Research - Mendeley Data.
*   TCGA-LIHC | The Cancer Genome Atlas Liver Hepatocellular Carcinoma Collection.
*   CT KIDNEY DATASET: Normal-Cyst-Tumor and Stone - Kaggle.
*   Liver Cancer Diagnosis Project - GitHub.
*   Imaging-based deep learning in kidney diseases: recent progress and future prospects.
*   Liver - Datasets - PLCO - The Cancer Data Access System.
*   KiTS23 | The 2023 Kidney Tumor Segmentation Challenge.
*   KidneyNeXt: A Lightweight Convolutional Neural Network for Multi-Class Renal Tumor Classification in Computed Tomography Imaging - PMC.
*   Liver cancer Datasets - BioGPS.
*   Medical Imaging Datasets — PYCAD.
*   Public Medical Image Datasets for Segmentation Foundation Models.
*   TCGA Kidney Cancers - UCI Machine Learning Repository.
*   CancerLivER: a database of liver cancer gene expression resources and biomarkers - PMC.
*   Find Open Datasets and Machine Learning Projects - Kaggle.
*   Comprehensive Medical Imaging Datasets Repository - GitHub.
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset - Kaggle.
*   GitHub - cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification.