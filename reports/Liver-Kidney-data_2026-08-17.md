# Research Report: Liver-Kidney-Data
*Generated: 2026-08-17 UTC*

**Executive Summary**

This report identifies key freely available datasets for liver and kidney research, with a particular focus on cancer-related data. Several comprehensive datasets offer high-quality scans and varying degrees of annotations and clinical data. Recent developments include new, larger datasets for kidney cancer histology and advancements in liver tumor segmentation. The availability of these resources, coupled with their non-restrictive licenses, is crucial for accelerating AI-driven medical diagnostics and treatment planning.

## Key Announcements by Organization

### The Cancer Imaging Archive (TCIA)
*   **C4KC-KITS:** This collection comprises CT scans and segmentations from the 2019 Kidney and Kidney Tumor Segmentation Challenge (KiTS19). It includes data for 210 patients with manual semantic segmentations of kidneys and tumors, providing a valuable resource for 3D semantic segmentation research.

### Duke University
*   **Duke Liver Dataset (DLDS):** This MRI dataset contains 2146 abdominal MRI series from 105 patients, many with cirrhotic features. It includes 310 image series with corresponding manually segmented liver masks. The DLDS is well-suited for training series classification or liver segmentation models and can be supplemented with other datasets like CHAOS or LiTS.

### Kaggle
*   **Liver Cancer Multiclass Dataset:** This dataset categorizes liver MRI scans into five classes: malignant and benign liver tumors, and non-cancerous liver scans. All images are standardized for deep learning analysis.
*   **Blood–Liver–Kidney Tri-Organ Imaging Dataset:** A multi-modal medical imaging dataset designed for object detection and tissue classification, including blood cell, liver, and kidney components.

### National Cancer Institute (NCI) / Cancer Data Access System (CDAS)
*   **Prostate, Lung, Colorectal, and Ovary (PLCO) Study Datasets:**
    *   **Liver Dataset:** Contains data for approximately 155,000 participants related to liver cancer incidence and mortality analyses.
    *   **Renal Dataset:** Contains data for approximately 155,000 participants related to renal cancer incidence and mortality analyses.

### University of California, Irvine (UCI) Machine Learning Repository
*   **TCGA Kidney Cancers Dataset:** A bulk RNA-seq dataset providing transcriptome profiles for patients with three different kidney cancer subtypes. It's useful for predicting subtypes based on transcriptome data and for practicing with large, sparse genomic information.

### Preprints.org / ResearchGate
*   **Dartmouth Kidney Cancer Histology Dataset:** Released in November 2024, this dataset includes 563 whole-slide images (WSIs) stained with hematoxylin and eosin (H&E), covering various kidney cancer subtypes. It's a large collection essential for digital pathology and machine learning applications in medical diagnostics.

## Notable Papers

*   **CancerLivER:** A database that maintains gene expression datasets of liver cancer along with putative biomarkers, comprising 115 datasets with gene-expression profiles of 9611 samples.
*   **Tumour and Liver Automatic Segmentation (ATLAS) Dataset:** This dataset provides systematic annotations of liver and liver tumors on contrast-enhanced magnetic resonance imaging (CE-MRI) scans for 90 patients with unresectable hepatocellular carcinoma (HCC).

## What to Watch

*   The **ATLAS challenge**, organized in conjunction with the REMIA2 workshop at MICCAI 2023, aims to facilitate the development of automated tools for liver and liver tumor segmentation using the ATLAS dataset.
*   Newer releases of the **TCGA (The Cancer Genome Atlas)** data collections, such as **TCGA-KIRC** for kidney renal clear cell carcinoma, continue to be updated and made available through platforms like TCIA, providing matched clinical, genetic, pathological, and radiological data.

## Possible Clinical Relevance

These datasets are crucial for advancing AI-driven solutions in medical imaging. For liver cancer, datasets like ATLAS and the Liver Cancer Multiclass Dataset can accelerate the development of automated segmentation and classification tools, aiding in treatment planning and diagnosis. For kidney cancer, the Dartmouth Kidney Cancer Histology Dataset and the C4KC-KITS dataset from TCIA are vital for improving digital pathology and 3D segmentation accuracy, respectively. The PLCO datasets offer large-scale epidemiological data for incidence and mortality analyses. The availability of diverse datasets with detailed annotations and clinical information will enable the creation of more robust and generalizable AI models, ultimately leading to earlier and more accurate diagnoses, personalized treatment strategies, and improved patient outcomes.

## Sources

*   
*   
*   
*   
*   https://cdas.cancer.gov/learn/plco/
*   https://cdas.cancer.gov/learn/plco/
*   
*   https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10757073/
*   
*   https://medicalsegmentation.com/ATLAS/
*   
*   https://www.cancerimagingarchive.net/collections/tcga-kirc/