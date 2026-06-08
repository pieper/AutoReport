# Research Report: Liver-Kidney-Data
*Generated: 2026-06-08 UTC*

**Executive Summary**

This report details freely available liver and kidney imaging datasets suitable for research, with a focus on those containing data on cancers and well-described diseases. The datasets vary in size, scan quality, and annotation availability, with a general trend towards increasing multimodal data and advanced annotations. Licensing is predominantly Creative Commons (CC BY, CC BY-NC, CC BY-NC-SA), with a growing number of datasets adopting the more permissive CC BY license. Recent advancements include larger datasets with multiphase imaging and multi-organ segmentation capabilities.

**Key Announcements**

**The Cancer Imaging Archive (TCIA)**
TCIA continues to be a primary source for de-identified cancer imaging data. As of July 2025, it offers a wide range of radiology and histopathology images, often linked with clinical, genomic, and pathology data. Many datasets on TCIA are under permissive Creative Commons licenses (CC BY, CC BY-NC). Recent additions and updates to existing collections provide more comprehensive data for AI development.

**Imaging Data Commons (IDC)**
As of Spring 2025, IDC hosts over 85 TB of data, including radiology and digital pathology images, with accompanying clinical data. Over 95% of the data is licensed under CC BY, supporting commercial reuse. IDC harmonizes data from various sources, including TCIA and TCGA, making it a centralized repository for cancer research data.

**Kaggle**
Kaggle hosts several relevant datasets, including the "Blood–Liver–Kidney Tri-Organ Imaging Dataset" which contains object detection and tissue classification data. Additionally, the "Kidney Disease Dataset" offers clinical and laboratory data for chronic kidney disease analysis.

**Notable Papers and Datasets**

*   **LiMT: a multi-task liver image benchmark dataset:** This dataset comprises 201 abdominal CT scans for primary and metastatic liver cancers, with detailed annotations for liver and tumors.
*   **Duke Liver Dataset (DLDS):** Contains 2146 abdominal MRI series from 105 patients, with a focus on liver cirrhosis. It includes 310 series with hand-drawn liver segmentation masks and is suitable for training segmentation and classification models.
*   **Large-Scale CT Dataset with Complete Phase Coverage:** A dataset of 278 primary liver cancer cases with full four-phase contrast-enhanced CT (CECT) imaging and clinician-verified annotations, also including 83 non-liver cancer controls.
*   **Kidney Tumor Segmentation Dataset (KiTS):** This dataset consists of 300 contrast-enhanced CT scans with labeled tumor tissue and healthy kidney tissue, created for a segmentation challenge. The Cancer Imaging Archive also hosts a version of this dataset (C4KC-KiTS) with CT scans and segmentations from the KiTS19 challenge.
*   **CT-ORG:** This dataset includes 140 CT scans with labeled lung, bones, liver, kidneys, and bladder, often featuring liver lesions.
*   **Open Kidney Dataset:** This dataset offers over 500 2D B-mode abdominal ultrasound images with expert annotations for kidney analysis, licensed under CC BY-NC-SA.
*   **LiverHccSeg:** A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis.
*   **ATLAS Dataset:** Comprises 90 T1 CE-MRI scans of the liver from patients with unresectable HCC, with corresponding liver and tumor segmentation masks.
*   **MMIST-ccRCC Dataset:** Curated from CPTAC and TCGA-KIRC, this dataset includes CT, MRI, Whole Slide Images (WSI), genomics, and clinical data for clear cell renal cell carcinoma (ccRCC).
*   **TCGA-KIRC:** The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma collection, part of TCIA, provides CT and MR images matched with clinical, genomic, and pathological data.

**What to Watch**

*   **Ongoing Data Curation:** TCIA and IDC are continuously updating and expanding their archives. Researchers should monitor these platforms for new collections and updates, especially those with multimodal data and comprehensive clinical annotations.
*   **Advancements in Multiphase and Multi-Organ Imaging:** Datasets like the "Large-Scale CT Dataset with Complete Phase Coverage" and "CT-ORG" highlight a trend towards multiphase imaging and multi-organ segmentation, which are crucial for more complex diagnostic tasks.
*   **Increased Availability of Multi-modal Data:** The MMIST-ccRCC dataset is an example of datasets integrating imaging with genomics and clinical data, a trend likely to grow.

**Possible Clinical Relevance**

The datasets described offer significant potential for advancing AI in medical diagnostics. Specifically:

*   **Cancer Detection and Segmentation:** Datasets focused on liver and kidney cancers (e.g., LiMT, KiTS, ATLAS, LiverHccSeg, TCGA-KIRC) can train models for more accurate and automated tumor detection, segmentation, and characterization. This can aid in early diagnosis, treatment planning, and monitoring.
*   **Disease Classification and Prediction:** Datasets like the "Kidney Disease Dataset" and those with extensive clinical data can be used to develop predictive models for disease progression and patient outcomes.
*   **Surgical Planning:** High-quality segmentation masks for organs and tumors (e.g., Duke Liver Dataset, KiTS, ATLAS) are essential for developing tools that assist in surgical planning, particularly for minimally invasive procedures.
*   **Understanding Disease Mechanisms:** Datasets incorporating multi-omics data (e.g., MMIST-ccRCC) can help researchers investigate the molecular underpinnings of liver and kidney diseases, potentially leading to novel therapeutic targets.

## Sources

*   Blood–Liver–Kidney Tri-Organ Imaging Dataset - Kaggle: 
*   LiMT: a multi-task liver image benchmark dataset - arXiv: https://arxiv.org/abs/2203.11620
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8393135/
*   Kidney Disease Dataset - Kaggle: 
*   Dataset Roundup - Noteworthy Datasets on Liver Diseases - Elucidata: 
*   Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics - PMC: 
*   CT-ORG - The Cancer Imaging Archive (TCIA): 
*   Imaging Data Commons | CRDC: https://datascience.cancer.gov/data-commons
*   AI in Medical Imaging: The Kidney Tumor Segmentation Challenge - Banook: 
*   halleewong/biomedical-imaging-datasets: GitHub: 
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset - Kaggle: 
*   C4KC-KITS - The Cancer Imaging Archive (TCIA): 
*   Open Kidney Dataset | kidneyUS: 
*   Liver - Datasets - PLCO - The Cancer Data Access System: https://cdas.cancer.gov/plco/
*   Liver Cell Atlas: https://www.ebi.ac.uk/gxa/home
*   Liver Disease Patient Dataset 30K train data - Kaggle: 
*   m-aryayi/Medical-Imaging-Datasets: GitHub: https://github.com/m-aryayi/Medical-Imaging-Datasets
*   LiverHccSeg: A Publicly Available Multiphasic MRI Dataset with Liver and HCC Tumor Segmentations and Inter-Rater Agreement Analysis - Zenodo: https://zenodo.org/record/6779747
*   Data Usage Policies and Restrictions - The Cancer Imaging Archive (TCIA): https://www.cancerimagingarchive.net/about/data-usage-policies/
*   MMIST ccRCC Dataset: 
*   TCGA-KIRC | The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma Collection: 
*   Kidney Other - The Cancer Imaging Archive (TCIA): 
*   B-MODE-AND-CEUS-LIVER - The Cancer Imaging Archive (TCIA): 
*   ATLAS - Welcome to the atlas challenge: 
*   Kidney Research Data Portal: https://www.kidneyresearch.org/data-portal
*   Image Sources - ASCCC Open Educational Resources Initiative: 
*   Cancer Imaging Archive - NCI: 
*   Medical Imaging Resource for AI (MIRA): 
*   GitHub - liver-cancer-segmentation/LITS: Liver Tumor Segmentation (LiTS) Dataset: 
*   Cancer datasets and tissue pathways - Royal College of Pathologists: 
*   liver disorders - Kaggle: 
*   TCGA Kidney Cancers - UCI Machine Learning Repository: 
*   GitHub - cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification.: https://github.com/cradleai/LKS-Dataset