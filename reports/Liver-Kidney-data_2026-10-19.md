# Research Report: Liver-Kidney-Data
*Generated: 2026-10-19 UTC*

## Executive Summary

This report synthesizes information on freely available liver and kidney datasets for research, focusing on datasets with a high number of patients, scans, and annotations, particularly for cancer-related research. Key datasets identified include those from The Cancer Genome Atlas (TCGA) for both liver (TCGA-LIHC) and kidney cancers (TCGA-KIRC), the Liver Tumor Segmentation Benchmark (LiTS), and the Kidney and Kidney Tumor Segmentation Challenge (KiTS19). These datasets offer varying degrees of clinical data, scan quality, and annotation detail, with some requiring specific access protocols. Recent developments include the expansion of the Human Cell Atlas initiative to include liver and kidney data and the application of advanced AI for annotation.

## Key Announcements and Datasets

### The Cancer Genome Atlas (TCGA) Program

TCGA provides comprehensive multi-omic data, including clinical, genomic, and imaging data, for numerous cancer types.

*   **TCGA Liver Hepatocellular Carcinoma (TCGA-LIHC):** This dataset offers summary data, visualizations, and clinical information for a broad sampling of liver hepatocellular carcinomas. It includes demographic data, disease status, tumor typing, and detailed clinical information such as mutation counts and gene information. Access is generally free, with some features requiring login.
*   **TCGA Kidney Cancers (TCGA-KIRC):** This dataset is a bulk RNA-seq dataset for kidney cancer patients, providing transcriptome profiles for three subtypes. It can be used for subtype prediction and offers hands-on experience with large genomic data. Clinical, genetic, and pathological data is available via the Genomic Data Commons (GDC) Data Portal, while radiological data is on The Cancer Imaging Archive (TCIA).

### Liver Tumor Segmentation Benchmark (LiTS)

The LiTS dataset is a well-established benchmark for liver and liver tumor segmentation in contrast-enhanced CT scans.

*   **LiTS:** Organized in conjunction with ISBI and MICCAI conferences, LiTS includes CT volumes with primary and secondary liver tumors. It provides segmentation masks for both the liver and tumors, making it valuable for training segmentation models. The dataset has been used in multiple challenge events, with ongoing public evaluation. Licenses are typically CC BY-NC-SA 4.0.

### Kidney and Kidney Tumor Segmentation Challenge (KiTS19)

KiTS19 focuses on semantic segmentation of kidneys and kidney tumors from CT scans.

*   **KiTS19:** This challenge dataset provides CT scans and manual semantic segmentations of kidneys and tumors for a number of patients. It was collected during routine care for patients undergoing nephrectomy. The data is available for model training and validation, with licenses often being CC BY-NC-SA.

### Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI)

While focused on lung nodules, LIDC-IDRI is a significant example of a high-quality annotated imaging dataset.

*   **LIDC-IDRI:** This database contains thoracic CT scans with annotated lung nodules, created through a rigorous process involving multiple radiologists. It serves as a reference for developing and evaluating computer-aided diagnostic methods for lung cancer detection. Annotations include nodule characteristics and malignancy likelihood.

### Human Cell Atlas (HCA)

The HCA initiative is expanding its data offerings to include liver and kidney.

*   **HCA Liver and Kidney Atlases:** As part of its expansion, HCA is making data from its Liver, Gut, Kidney, Immune, and Developmental Atlases available through the AWS Open Data Program. This initiative aims to provide broad, long-term, and free access to cell-level data.

## Notable Papers

*   **The Cancer Genome Atlas Pan-Cancer analysis project:** This foundational paper describes the initial comprehensive analysis of TCGA data, laying the groundwork for understanding cancer genomics.
*   **TCGA Liver Hepatocellular Carcinoma (TCGA-LIHC):** Datasets from this project provide extensive clinical and genomic data for liver cancer research, enabling genotype-phenotype correlations.
*   **TCGA Kidney Cancers:** This dataset provides transcriptome profiles of kidney cancer patients, facilitating subtype classification and genomic analysis.
*   **The Liver Tumor Segmentation Benchmark (LiTS):** Papers describing LiTS detail the setup and results of segmentation challenges, highlighting performance metrics and the dataset's value for research.
*   **The KiTS19 Challenge Data:** This paper introduces the KiTS19 dataset, emphasizing its utility for training and benchmarking automatic kidney tumor segmentation models, and includes clinical context and outcomes.
*   **LIDC-IDRI:** Publications related to LIDC-IDRI demonstrate its use in developing and validating AI systems for lung nodule detection and classification.
*   **CancerLivER:** This database integrates gene expression datasets and biomarkers for liver cancer, offering a comprehensive resource for research.
*   **LiverHccSeg:** This dataset provides multiphasic MRI scans with liver and HCC tumor segmentations, aiming to advance segmentation algorithm development and benchmarking.
*   **Duke Liver Dataset:** This MRI dataset includes liver segmentation masks and series labels, suitable for training generalized segmentation models and for multimodality training with datasets like LiTS.

## What to Watch

*   **Human Cell Atlas (HCA) Liver and Kidney Atlases:** Keep an eye on the full release and accessibility of these new atlases, which are expected to provide a significant volume of single-cell data.
*   **Ongoing LiTS and KiTS challenges:** The continued use and evolution of LiTS and KiTS as benchmarks suggest ongoing development and potential for new iterations or related challenges in liver and kidney image segmentation.
*   **Advancements in AI-powered annotation:** With models like SAM (Segment Anything Model) showing promise for medical data annotation, expect to see more datasets leveraging AI for faster and more efficient annotation creation.

## Possible Clinical Relevance

The datasets discussed are highly relevant for advancing clinical practice in several ways:

*   **Improved Diagnostics:** High-quality, annotated imaging datasets are crucial for training AI models that can detect and classify liver and kidney cancers with greater accuracy and speed, potentially leading to earlier diagnosis.
*   **Personalized Treatment:** The availability of rich clinical and genomic data alongside imaging (e.g., from TCGA) allows for a deeper understanding of disease subtypes and patient prognoses, paving the way for more personalized treatment strategies.
*   **Enhanced Surgical Planning:** Segmentation datasets like LiTS and KiTS19 are vital for developing tools that can precisely delineate organs and tumors, aiding surgeons in pre-operative planning and intra-operative guidance.
*   **Biomarker Discovery:** Gene expression and other molecular data available in datasets like CancerLivER and TCGA can help identify novel biomarkers for early detection, prognosis, and therapeutic targeting of liver and kidney diseases.
*   **Reduced Healthcare Costs:** AI tools developed from these datasets could automate tedious tasks, reduce inter-observer variability, and potentially decrease the cost of medical image analysis.

## Sources

*   TCGA Kidney Cancers - UCI Machine Learning Repository. (2023, September 25).
*   Liver Hepatocellular Carcinoma - MSK Data Catalog.
*   LIDC-IDRI - The Cancer Imaging Archive (TCIA).
*   The Liver Tumor Segmentation Benchmark (LiTS).
*   The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A Completed Reference Database of Lung Nodules on CT Scans | NIST. (2011, January 28).
*   The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A Completed Reference Database of Lung Nodules on CT Scans - PMC.
*   Subset of LiTS Dataset for Liver and Tumor Segmentation | Zenodo. (2026, March 22).
*   The Liver Tumor Segmentation Benchmark (LiTS) - PMC - NIH.
*   Datasets - UCI Machine Learning Repository.
*   TCGA-KIRC | The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma Collection.
*   C4KC-KiTS - The Cancer Imaging Archive (TCIA).
*   TCGA-LIHC - The Cancer Imaging Archive (TCIA).
*   Liver Hepatocellular Carcinoma (TCGA, PanCancer Atlas) - MSK Data Catalog.
*   The Cancer Genome Atlas Liver Hepatocellular Carcinoma Collection (TCGA-LIHC).
*   [1904.00445] The KiTS19 Challenge Data: 300 Kidney Tumor Cases with Clinical Context, CT Semantic Segmentations, and Surgical Outcomes - arXiv. (2019, March 31).
*   0004_lits/README_0004_lits.md · huggingface/CADS-dataset at main. (2025, December 17).
*   [1901.04056] The Liver Tumor Segmentation Benchmark (LiTS) - arXiv. (2019, January 13).
*   Enhanced Pulmonary Nodule Detection and Classification Using Artificial Intelligence on LIDC-IDRI Data - Xia & He Publishing Inc. (2026, January 15).
*   GitHub - ziyangwang007/Awesome-Medical-Image-Segmentation-Dataset: A list of publicly available medical image segmentation dataset.
*   KITS 19 - Kidney Tumor Segmentation - Kaggle.
*   TCGA Kidney Renal Clear Cell Carcinoma (KIRC) Clinical Data - Zenodo. (2023, July 27).
*   Kidney Renal Clear Cell Carcinoma (TCGA, PanCancer Atlas) - MSK Data Catalog.
*   Best Medical Image Segmentation Datasets for Training Clinical AI Models - DataVLab. (2026, August 03).
*   Noteworthy Datasets on Liver Diseases - Elucidata. (2022, May 25).
*   Liver - Datasets - PLCO - The Cancer Data Access System.
*   Challenge Data - KiTS19.
*   The state of the art in kidney and kidney tumor segmentation in contrast-enhanced CT imaging: Results of the KiTS19 challenge - PMC.
*   Comprehensive and Integrative Genomic Characterization of Hepatocellular Carcinoma - PMC.
*   Digital Pathology and Ensemble Deep Learning for Kidney Cancer Diagnosis: Dartmouth Kidney Cancer Histology Dataset - Preprints.org. (2024, November 21).
*   CancerLivER: a database of liver cancer gene expression resources and biomarkers - PMC. (2020, March 07).
*   Renal - Datasets - PLCO - The Cancer Data Access System.
*   CancerLivER: Home Page.
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC.
*   Dartmouth Kidney Cancer Histology Dataset.
*   Annotated Medical Image Dataset - Emergent Mind. (2026, January 02).
*   Medical Image Datasets and Annotations.
*   Open Kidney Dataset | kidneyUS.
*   cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification. · GitHub.
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC.
*   Medical Imaging Resource for AI (MIRA).
*   HCA Data now freely available on AWS - Human Cell Atlas. (2025, June 24).
*   [2409.20253] Medical Image Segmentation with SAM-generated Annotations - arXiv. (2024, September 30).
*   Medical Imaging Datasets - Intelligent Clinical Care Center (IC3) » » University of Florida.
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels | Radiology: Artificial Intelligence - RSNA Journals. (2023, July 26).
*   LiMT: a multi-task liver image benchmark dataset - arXiv. (2025, November 25).
*   Liver MRI Raw Data Acquired with Free-Breathing 3D Multi-Echo Cones MRI - Zenodo | NLM Dataset Catalog.