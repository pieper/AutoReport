# Research Report: Liver-Kidney-Data
*Generated: 2026-03-30 UTC*

**Executive Summary**

This report outlines current, freely available datasets for liver and kidney research, with a focus on datasets containing well-described diseases such as cancers. Key considerations include the number of patients and scans, scan quality, annotation availability, and accompanying clinical data. Emphasis is placed on datasets with non-restrictive licenses, particularly CC-BY. The NCI Imaging Data Commons (IDC) stands out for its extensive collection and commercial-friendly CC-BY licensing. Newer datasets like the Primary Liver Cancer CECT Imaging Dataset and the "Tumour and Liver Automatic Segmentation" (ATLAS) dataset offer valuable resources with detailed annotations. For kidney research, the Kidney Tumor Segmentation Challenge (KiTS19) dataset and TCGA Kidney Cancers Dataset are notable.

## Key Announcements and Datasets

### NCI Imaging Data Commons (IDC)

*   The IDC is a cloud-based repository offering a vast collection of cancer imaging data, including CT, MRI, and PET scans, alongside image-derived data and clinical information.
*   Over 95% of the data in IDC is covered by the permissive CC-BY license, allowing for commercial reuse.
*   It hosts data from projects like The Cancer Genome Atlas (TCGA) and The Cancer Imaging Archive (TCIA), providing access to harmonized DICOM data.

### Primary Liver Cancer CECT Imaging Dataset

*   This dataset comprises 278 primary liver cancer cases with full four-phase contrast-enhanced CT (CECT) imaging and clinician-verified liver and lesion masks.
*   It includes over 50,000 manually annotated lesion sections and 83 non-liver cancer control cases.
*   The dataset facilitates the development of diagnostic classification and segmentation models for liver cancer.
*   Associated Python code for data loading and processing is available on GitHub.

### "Tumour and Liver Automatic Segmentation" (ATLAS) Dataset

*   The ATLAS dataset contains 90 contrast-enhanced MRI (CE-MRI) scans of the liver from patients with unresectable Hepatocellular Carcinoma (HCC), along with corresponding liver and tumor segmentation masks.
*   It is noted as the first public dataset providing CE-MRI of HCC with annotations, aiming to facilitate automated segmentation tools for treatment planning.
*   Data includes image resolution, contrast phase, MRI sequence, and manufacturer information.

### Kidney Tumor Segmentation Challenge (KiTS19) Dataset

*   This collection includes CT scans and segmentations from 210 patients with kidney tumors, featuring manual semantic segmentations of kidneys and tumors.
*   The imaging was collected during routine care and exhibits heterogeneity in scanner manufacturers and acquisition protocols.
*   Segmentations were performed by supervised students, ensuring quality.
*   The dataset is available under a CC BY 3.0 license.

### Duke Liver Dataset (DLDS)

*   The DLDS contains 2146 abdominal MRI series from 105 patients, with a focus on liver cirrhosis.
*   It includes binary masks for whole-organ liver segmentations for 310 image series.
*   The dataset is suitable for training series classification or liver segmentation models and can be used for segmenting other abdominal organs like kidneys through transfer learning.

### TCGA Kidney Cancers Dataset

*   This is a bulk RNA-seq dataset containing transcriptome profiles of patients with three different subtypes of kidney cancers.
*   It allows for predictions of specific kidney cancer subtypes based on normalized transcriptome profiles.
*   The data is part of The Cancer Genome Atlas (TCGA) effort, with radiological data available on The Cancer Imaging Archive (TCIA).

### Blood–Liver–Kidney Tri-Organ Imaging Dataset

*   This multimodal dataset includes separate components for blood cell detection, liver tissue analysis, and kidney tissue analysis.
*   It contains 1,000 images for liver tissue classification (3 classes) and 1,000 images for kidney tissue classification (2 classes).
*   The dataset is intended for object detection and tissue classification tasks, with capabilities for multi-sample correlation analysis.

## Notable Papers

*   **Primary Liver Cancer CECT Imaging Dataset:** This dataset, featuring 278 primary liver cancer cases with full four-phase imaging and annotations, aims to advance AI diagnostics for liver cancer.
*   **ATLAS Dataset:** This dataset provides the first public collection of CE-MRI scans for HCC with liver and tumor annotations, facilitating automated segmentation for treatment planning.
*   **Duke Liver Dataset:** This large MRI dataset with liver segmentation masks can serve as a foundation for training segmentation models for various abdominal organs, including the kidneys.
*   **KiTS19 Dataset:** This dataset of CT scans with kidney and tumor segmentations aids in the development of automatic 3D semantic segmentation for kidney cancer.

## What to Watch

*   **NCI Imaging Data Commons (IDC):** Continual expansion of data, with over 85 TB available as of Spring 2025, and a strong commitment to CC-BY licensing for commercial usability.
*   **LiMT Dataset:** This multi-task liver image benchmark dataset, planned for release around November 2025, aims to include CT volumes from 150 cases with annotations for liver diseases and normal cases.
*   **Blood–Liver–Kidney Tri-Organ Imaging Dataset:** This dataset is listed with a release date of December 31, 2025, and includes components for liver and kidney tissue analysis.

## Possible Clinical Relevance

The datasets discussed hold significant potential for clinical relevance by enabling the development and validation of AI-driven tools for:

*   **Early Disease Detection and Diagnosis:** Datasets with detailed annotations and diverse patient populations can train models to identify subtle signs of liver and kidney diseases, including various cancer subtypes, at earlier stages.
*   **Improved Treatment Planning:** Accurate segmentation of tumors and organs, as provided by datasets like ATLAS and KiTS19, is crucial for precise surgical planning, radiation therapy, and other targeted treatments.
*   **Personalized Medicine:** Datasets with extensive clinical data, such as those from TCGA or the Duke Liver Dataset, can help researchers identify biomarkers and correlations that lead to more personalized diagnostic and treatment strategies.
*   **Streamlined Workflow:** Automated segmentation and classification tools developed using these datasets can reduce the time and effort required by radiologists and clinicians, freeing them to focus on more complex cases and patient interaction.
*   **Enhanced Understanding of Disease Progression:** Datasets with longitudinal data or detailed clinical histories can contribute to a better understanding of disease progression and treatment response.

## Sources

1.  Primary Liver Cancer CECT Imaging Dataset. (n.d.). Retrieved from 
2.  A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma - MDPI. (n.d.). Retrieved from 
3.  Liver Cancer Multiclass Dataset - Kaggle. (n.d.). Retrieved from 
4.  Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC. (n.d.). Retrieved from 
5.  Blood–Liver–Kidney Tri-Organ Imaging Dataset. (n.d.). Retrieved from 
6.  Dataset Roundup - Noteworthy Datasets on Liver Diseases - Elucidata. (n.d.). Retrieved from 
7.  NCI Imaging Data Commons | CRDC. (n.d.). Retrieved from https://imaging.datacommons.cancer.gov/
8.  Kidney Disease Dataset - Kaggle. (n.d.). Retrieved from 
9.  C4KC-KITS - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from 
10. 22 Free and Open Healthcare Datasets for Machine Learning and AI Development in 2025. (n.d.). Retrieved from 
11. LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC. (n.d.). Retrieved from 
12. Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics | Radiology. (n.d.). Retrieved from 
13. AI in Medical Imaging: The Kidney Tumor Segmentation Challenge | Banook. (n.d.). Retrieved from https://banook.com/ai-in-medical-imaging-the-kidney-tumor-segmentation-challenge/
14. Blood–Liver–Kidney Tri-Organ Imaging Dataset. (n.d.). Retrieved from 
15. Top Kidney Datasets and Models - Roboflow Universe. (n.d.). Retrieved from 
16. MMIST ccRCC Dataset. (n.d.). Retrieved from 
17. Open Kidney Dataset | kidneyUS. (n.d.). Retrieved from 
18. Datasets - UCI Machine Learning Repository. (n.d.). Retrieved from https://archive.ics.uci.edu/datasets
19. Shared Datasets | Center for Artificial Intelligence in Medicine & Imaging. (n.d.). Retrieved from 
20. Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels Radiology: Artificial Intelligence - RSNA Journals. (n.d.). Retrieved from 
21. Liver - Datasets - PLCO - The Cancer Data Access System. (n.d.). Retrieved from https://cdas.cancer.gov/plco/datasets/
22. Liver Disease Patient Dataset 30K train data - Kaggle. (n.d.). Retrieved from 
23. TCGA-KIRC | The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma Collection. (n.d.). Retrieved from 
24. Annotated Medical Image Dataset - Emergent Mind. (n.d.). Retrieved from 
25. Kidney Tumor Detection and Classification Based on Deep Learning Approaches: A New Dataset in CT Scans - PMC. (n.d.). Retrieved from 
26. Public Medical Image Datasets for Segmentation Foundation Models. (n.d.). Retrieved from 
27. GitHub - cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification. (n.d.). Retrieved from https://github.com/cradleai/LKS-Dataset
28. NIDDK Data or Sample Repositories - dkNET. (n.d.). Retrieved from 
29. LiMT: a multi-task liver image benchmark dataset - arXiv. (n.d.). Retrieved from https://arxiv.org/abs/2402.19251
30. DrNote: An open medical annotation service - PMC. (n.d.). Retrieved from 
31. 18 Open Healthcare Datasets — 2025 Update | by ODSC. (n.d.). Retrieved from 
32. An Open-Source Clinical Case Dataset for Medical Image Classification and Multimodal AI Applications - MDPI. (n.d.). Retrieved from 
33. The MultiCaRe Dataset: A Multimodal Case Report Dataset with Clinical Cases, Labeled Images and Captions from Open Access PMC Articles - Zenodo. (n.d.). Retrieved from https://zenodo.org/records/10709323
34. Dataset of clinical cases, images, image labels and captions from open access case reports from PubMed Central (1990–2023) - PMC. (n.d.). Retrieved from 
35. How to Use Digital Medic Content. (n.d.). Retrieved from https://www.digitalmedic.org/
