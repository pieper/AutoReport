# Research Report: Liver-Kidney-Data
*Generated: 2026-04-06 UTC*

## Executive Summary

This report outlines freely available liver and kidney datasets, focusing on those relevant to cancer research, with high patient and scan counts, quality scans, available annotations, and clinical data. The Cancer Genome Atlas (TCGA) initiative remains a primary source for comprehensive genomic and clinical data for various cancers, including liver (hepatocellular carcinoma) and kidney (clear cell renal cell carcinoma, papillary renal cell carcinoma, chromophobe renal cell carcinoma). Newer initiatives and specialized datasets are emerging, particularly in medical imaging, offering detailed annotations for segmentation and classification tasks. Licensing for these datasets varies, with many being open for non-commercial use, while some are more broadly accessible under permissive licenses like CC-BY.

## Key Announcements

### The Cancer Genome Atlas (TCGA) Program

The TCGA program continues to be a cornerstone for large-scale cancer genomics and clinical data. While not a recent announcement, its ongoing availability and integration with The Cancer Imaging Archive (TCIA) provide extensive resources for liver and kidney cancers.

*   **TCGA Liver Hepatocellular Carcinoma (TCGA-LIHC):** This dataset includes clinical, genetic, and pathological data for liver cancer patients. It is integrated with TCIA for radiological data, allowing for correlations between genotype, radiological phenotype, and patient outcomes. The dataset contains summary data visualizations and clinical data from a broad sampling of liver hepatocellular carcinomas.
*   **TCGA Kidney Cancers:** This encompasses several subtypes, including:
    *   **Kidney Renal Clear Cell Carcinoma (TCGA-KIRC):** Provides matched clinical, genetic, pathological, and radiological data.
    *   **Kidney Renal Papillary Cell Carcinoma (TCGA-KIRP):** Offers similar comprehensive data for this subtype.
    *   **Kidney Chromophobe (TCGA-KICH):** Includes clinical, genetic, pathological, and radiological data.
    *   **TCGA Kidney Cancers (general):** A bulk RNA-seq dataset with transcriptome profiles for patients diagnosed with three different subtypes of kidney cancers.

### Specialized Imaging Datasets

*   **ATLAS (Tumour and Liver Automatic Segmentation) Dataset:** This is a newly highlighted dataset specifically designed for liver and liver tumor segmentation on contrast-enhanced MRI scans. It provides systematic annotations for hepatocellular carcinoma (HCC) and is available as part of the ATLAS challenge.
*   **Open Kidney Dataset:** This dataset offers fine-grained annotated ultrasound images for medical image analysis, focusing on the kidney. It includes over 500 images with polygon annotations for four classes, though it is restricted to non-commercial use (CC BY-NC-SA license).
*   **RenSeg-KidneyCT Dataset:** This dataset comprises kidney CT scans with annotations for Renal Calculi and Renal Carcinoma, along with normal kidney cases. It is intended for segmentation and classification research.
*   **Duke Liver Dataset (DLDS):** This dataset contains a large number of abdominal MRI series with manual liver segmentations, suitable for training classification and segmentation models. It also notes potential for transfer learning to other abdominal organs like kidneys.
*   **C4KC-KiTS (Kidney Kidney Tumor Segmentation Challenge):** This dataset includes CT scans and segmentations from the KiTS19 challenge, focusing on kidneys and tumors.
*   **MMIST ccRCC Dataset:** This dataset is curated from CPTAC-CCRCC and TCGA-KIRC, focusing on clear cell renal cell carcinoma (ccRCC) and developed for multi-modal systems.
*   **Kidney Stone Images with Bounding Box Annotations:** This dataset provides CT scan images with bounding box annotations specifically for kidney stone detection, useful for object detection algorithms. It is available under a CC BY 4.0 license.
*   **Blood–Liver–Kidney Tri-Organ Imaging Dataset:** This comprehensive dataset includes sub-datasets for blood cell detection (object detection), liver tissue analysis (classification), and kidney tissue analysis (classification). However, its license is noted as "Restricted."

## Notable Papers

*   **"Comprehensive and Integrative Genomic Characterization of Hepatocellular Carcinoma"**: This paper, part of The Cancer Genome Atlas (TCGA) network, presents a large-scale multi-platform analysis of HCC, including somatic mutations, DNA copy number, methylation, and expression data.
*   **"The Cancer Genome Atlas Comprehensive Molecular Characterization of Renal Cell Carcinoma"**: This publication details the molecular characterization of various renal cell carcinoma (RCC) subtypes, including clear cell RCC, papillary RCC, and chromophobe RCC, using TCGA data.
*   **"A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma"**: This paper introduces the ATLAS dataset, the first publicly available dataset with systematic annotations of liver and liver tumors on HCC CE-MRI scans, facilitating automated segmentation tool development.
*   **"Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels"**: This study describes the Duke Liver Dataset, a large collection of abdominal MRI series with manual liver segmentations, useful for developing segmentation and classification models.

## What to Watch

*   **Emerging Imaging Datasets:** Continued development in medical imaging AI is leading to more specialized and annotated datasets for organs like the liver and kidneys. Researchers should monitor challenge-based datasets (e.g., from MICCAI workshops) and institutional releases.
*   **Data Integration Efforts:** Initiatives that integrate multi-modal data (genomics, imaging, clinical data) will become increasingly important for comprehensive cancer research. The TCGA program's integration with TCIA is a prime example.
*   **Advancements in Annotation Quality and Quantity:** The trend towards more detailed and expert-generated annotations for segmentation and classification tasks is expected to continue, enhancing the utility of these datasets for complex AI models.

## Possible Clinical Relevance

The datasets described offer significant potential for clinical relevance by enabling the development and validation of AI tools for:

*   **Early Disease Detection and Diagnosis:** Improved algorithms for detecting liver and kidney cancers, as well as conditions like kidney stones and liver fibrosis, can lead to earlier diagnosis and intervention.
*   **Prognosis and Treatment Planning:** Detailed genomic and imaging data can help in predicting patient outcomes and tailoring treatment strategies, particularly for cancers like HCC and RCC.
*   **Surgical and Interventional Guidance:** Precise segmentation of organs and tumors, as provided by datasets like ATLAS and C4KC-KiTS, can aid in surgical planning and image-guided interventions.
*   **Drug Discovery and Development:** Molecular profiling data from TCGA can accelerate the identification of therapeutic targets and the development of new drugs for liver and kidney cancers.
*   **Monitoring Disease Progression and Treatment Response:** Longitudinal imaging and clinical data can be used to develop models that track disease progression and assess the effectiveness of treatments.

## Sources

Liver Hepatocellular Carcinoma (TCGA, PanCancer Atlas) - MSK Data Catalog.
TCGA Kidney Cancers - UCI Machine Learning Repository.
Open Kidney Dataset | kidneyUS.
TCGA-KIRC | The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma Collection.
Kidney Renal Papillary Cell Carcinoma (TCGA, PanCancer Atlas) - MSK Data Catalog.
TCGA-LIHC | The Cancer Genome Atlas Liver Hepatocellular Carcinoma Collection.
Annotated Ultrasound Liver images Dataset - Kaggle.
The Cancer Genome Atlas Liver Hepatocellular Carcinoma Collection (TCGA-LIHC).
A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma - MDPI.
PragyaSpn/GCD1: Genomic censored dataset of the Liver Cancer from TCGA database - GitHub.
RenSeg-KidneyCT - Mendeley Data.
LiMT: a multi-task liver image benchmark dataset - arXiv.
Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC.
Liver - Datasets - PLCO - The Cancer Data Access System.
Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series LabelsRadiology: Artificial Intelligence - RSNA Journals.
Kidney Stone Images with Bounding Box Annotations - GitHub.
Comprehensive and Integrative Genomic Characterization of Hepatocellular Carcinoma - PMC.
Dataset Roundup - Noteworthy Datasets on Liver Diseases - Elucidata.
The Cancer Genome Atlas Comprehensive Molecular Characterization of Renal Cell Carcinoma - PMC.
Renal - Datasets - PLCO - The Cancer Data Access System.
Kidney Stone Images with Bounding Box Annotations - Kaggle.
TCGA-KICH - The Cancer Imaging Archive (TCIA).
C4KC-KITS - The Cancer Imaging Archive (TCIA).
MMIST ccRCC Dataset.
Blood–Liver–Kidney Tri-Organ Imaging Dataset.
CancerLivER: a database of liver cancer gene expression resources and biomarkers - PMC.
CancerLivER: Home Page.
Kidney stone detection via axial CT imaging: A dataset for AI and deep learning applications.
Blood–Liver–Kidney Tri-Organ Imaging Dataset.
Liver cancer Datasets - BioGPS.
Program Report: KidneyPRO, a Web-based Training Module for Patient Engagement in Kidney Research - PMC.
Medical Imaging Resource for AI (MIRA).
KIDNEY PRO: Promoting Kidney Research in Canada.
GitHub - cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification.
CARE-Liver.
A preclinical CT and MRI Liver Imaging Dataset with Anatomical, Functional and Segmentation Data - PubMed.
ProKidney - Pioneers in the Treatment of Chronic Kidney Disease.
Kidney Health.
About Us - ProKidney.