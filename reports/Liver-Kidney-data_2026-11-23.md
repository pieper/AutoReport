# Research Report: Liver-Kidney-Data
*Generated: 2026-11-23 UTC*

## Liver and Kidney Datasets: A Comprehensive Report

### Executive Summary

This report details the current landscape of publicly available liver and kidney imaging datasets, focusing on their suitability for AI-driven medical research, particularly in the area of cancer detection and analysis. Several high-quality datasets have emerged, offering substantial numbers of scans, detailed annotations, and valuable clinical data. Key developments include advancements in multi-task learning datasets and the increasing availability of ultrasound data. While many datasets adhere to non-restrictive licenses, careful review is always recommended. The availability of these resources is crucial for advancing diagnostic and prognostic capabilities in liver and kidney diseases.

### Key Announcements

**Duke University**
*   **Duke Liver Dataset (DLDS):** This dataset continues to be a significant resource, offering 2146 abdominal MRI series from 105 patients, with a majority exhibiting cirrhotic features. A notable subset includes 310 image series with manually segmented liver masks. Recent updates (v2) have restored previously withheld data for completeness. The dataset is well-suited for training series classification and liver segmentation models. While some versions are available under a CC BY-NC-ND 4.0 license, custom licenses for commercial use may be available upon request.

**University of British Columbia**
*   **Open Kidney Dataset:** This dataset provides over 500 two-dimensional B-mode abdominal ultrasound images with fine-grained polygon annotations for four classes. It aims to address the scarcity of open ultrasound data for kidney analysis and is available for non-commercial use under a CC BY-NC-SA license. Registration is required for data access due to privacy considerations.

**University of California San Diego & others**
*   **LiMT (Multi-task Liver Image Benchmark Dataset):** This dataset offers CT volumes from 150 cases, annotated for liver and tumor segmentation, multi-label lesion classification, and lesion detection. It is designed to support multi-task learning and explores correlations between these tasks. The dataset includes four types of liver diseases and normal cases, with annotations calibrated by experienced clinicians. It is available via Google Drive.

**The Cancer Imaging Archive (TCIA)**
*   **Renal Cell Carcinoma (RCC) Collections:** TCIA hosts several datasets related to kidney cancer, including the **C4KC-KITS** collection, which contains CT scans and segmentations for 210 patients from the Kidney and Kidney Tumor Segmentation Challenge (KiTS19). Additionally, the **RCC-AID** project aims to create a reliable dataset of voxel-wise annotations for solid kidney tumors and cysts from TCGA data, intended for AI research.

### Notable Papers and Datasets

*   **Duke Liver Dataset (DLDS):** This dataset is well-suited for training series classification models or liver segmentation models for abdominal MRI.
*   **Open Kidney Dataset:** Aims to standardize ultrasound segmentation benchmarking for kidneys and reduce interpretation efforts.
*   **LiMT:** Aims to address the limitation of existing datasets typically supporting only single tasks by providing a multi-task liver dataset for segmentation, detection, and classification.
*   **Annotated Ultrasound Liver Images Dataset (Kaggle/Zenodo):** Contains ultrasound images of the liver with annotations for liver and mass regions, classified into benign, malignant, and normal cases.
*   **C4KC-KITS:** A dataset of CT scans and segmentations for kidney and kidney tumor segmentation.
*   **MMIST ccRCC Dataset:** Curated from CPTAC-CCRCC and TCGA-KIRC, this dataset focuses on ccRCC (kidney cancer) using CT, MRI, and Whole Slide Images (WSIs).
*   **LiverHccSeg:** Provides liver and HCC tumor segmentations on multiphasic contrast-enhanced MRI, with an analysis of inter-rater agreement between two radiologists.

### What to Watch

*   **Ongoing advancements in multi-organ datasets:** Datasets like **AbdomenAtlas** and those integrated into challenges like **FLARE** continue to expand with more comprehensive abdominal organ segmentations.
*   **Increased availability of ultrasound data:** The **Open Kidney Dataset** is a step towards addressing the underrepresentation of ultrasound data in public repositories. Future releases may focus on broader organ coverage and more diverse pathologies.
*   **AI-generated annotations:** Projects exploring AI-generated annotations, such as those mentioned in the **RCC-AID** dataset context, may lead to more rapidly scalable annotation efforts for large datasets.

### Possible Clinical Relevance

The datasets highlighted offer significant potential for advancing clinical practice through AI.

*   **Improved Cancer Detection and Diagnosis:** Datasets like DLDS, LiMT, LiverHccSeg, and the TCIA kidney cancer collections are crucial for developing and validating AI models that can detect and classify liver and kidney cancers with higher accuracy and consistency. This can lead to earlier diagnoses and more precise treatment planning.
*   **Enhanced Segmentation Accuracy:** The availability of detailed annotations for organs like the liver and kidneys in datasets such as DLDS, Open Kidney Dataset, and C4KC-KITS enables the development of robust segmentation algorithms. Accurate segmentation is fundamental for quantitative analysis, surgical planning, and treatment response monitoring.
*   **Understanding Disease Progression:** Datasets focusing on conditions like liver cirrhosis (DLDS) or various kidney diseases can aid in building models that predict disease progression, identify risk factors, and personalize patient management strategies.
*   **Advancing Diagnostic Modalities:** The inclusion of diverse imaging modalities (CT, MRI, Ultrasound) across these datasets allows for the development of AI tools that can work across different imaging techniques, potentially improving diagnostic efficiency and accessibility.

### Sources

*   Open Kidney Dataset. (n.d.). Retrieved from https://arxiv.org/abs/2010.00211
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels. (n.d.). Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10503808/
*   Annotated Ultrasound Liver images Dataset. (n.d.). Retrieved from 
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels | Radiology: Artificial Intelligence - RSNA Journals. (2023, July 26). Retrieved from 
*   LiMT: a multi-task liver image benchmark dataset. (2025, November 25). Retrieved from https://arxiv.org/abs/2308.04712
*   halleewong/biomedical-imaging-datasets. (n.d.). Retrieved from https://github.com/halleewong/biomedical-imaging-datasets
*   Annotated Ultrasound Liver images. (2022, November 2). Retrieved from https://zenodo.org/records/7272660
*   Human Kidney Benchmark Dataset | v1.0. (2025, September 15). Retrieved from 
*   The Liver Kidney Stomach Dataset - COVE - Computer Vision Exchange. (2020, August 24). Retrieved from 
*   The Open Kidney Ultrasound Data Set. (n.d.). Retrieved from https://arxiv.org/abs/2010.00211
*   Kidney Datasets - BioGPS. (n.d.). Retrieved from 
*   cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification. (n.d.). Retrieved from https://github.com/cradleai/LKS-Dataset
*   Public Data in Nephrology. (n.d.). Retrieved from 
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset - Mendeley Data. (2026, September 15). Retrieved from https://data.mendeley.com/datasets/b2v9ht3g8n
*   Duke Liver Dataset (MRI) v2. (2023, April 4). Retrieved from https://zenodo.org/records/7774566
*   RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research. (2026, August 5). Retrieved from 
*   C4KC-KITS - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from https://www.cancerimagingarchive.net/collection/c4kc-kits/
*   MMIST ccRCC Dataset. (n.d.). Retrieved from https://www.dropbox.com/sh/5d98tqv7g9h7p4l/AAAn0hJzI8qJ0N7zK2UfK3pRa?dl=0
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis. (n.d.). Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10503808/
*   Medical Imaging Datasets - Intelligent Clinical Care Center (IC3) » » University of Florida. (n.d.). Retrieved from 
*   Liver Cancer Multiclass Dataset - Kaggle. (n.d.). Retrieved from 
*   halleewong/biomedical-imaging-datasets - GitHub. (2025, November 15). Retrieved from https://github.com/halleewong/biomedical-imaging-datasets
*   Artificial Intelligence in Renal Imaging: A Multi-Dataset Study for Kidney Disease Classification. (2026, May 14). Retrieved from 
*   Imaging of liver cancer. (2009, March 21). Retrieved from https://pubmed.ncbi.nlm.nih.gov/19298010/
*   Advances in the imaging of liver cancer. (n.d.). Retrieved from https://pubmed.ncbi.nlm.nih.gov/36657789/
*   Liver cancer imaging: role of CT, MRI, US and PET. (2026, May 7). Retrieved from 
*   Advances in the imaging of liver cancer. (n.d.). Retrieved from 
*   Imaging of liver cancer. (2009, March 21). Retrieved from https://pubmed.ncbi.nlm.nih.gov/19298010/
*   Comprehensive Medical Imaging Datasets Repository. (2025, November 15). Retrieved from 