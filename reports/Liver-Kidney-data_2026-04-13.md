# Research Report: Liver-Kidney-Data
*Generated: 2026-04-13 UTC*

## Liver and Kidney Datasets Report

### Executive Summary

This report details the landscape of freely available liver and kidney datasets, with a focus on those suitable for AI and machine learning applications. Key considerations include dataset size, scan quality, annotation availability, and licensing. Recent advancements have led to the creation of larger, more comprehensive datasets, particularly in medical imaging. Organizations like the NCI Imaging Data Commons (IDC) and efforts within the TCGA (The Cancer Genome Atlas) program are significant contributors. While many datasets offer valuable resources, their licenses and accessibility can vary, with a notable trend towards CC-BY licenses for broader research and commercial use.

### Key Announcements and Datasets

#### NCI Imaging Data Commons (IDC)

The NCI Imaging Data Commons (IDC) is a significant resource, providing access to over 85 TB of cancer imaging data as of Spring 2025. This cloud-based repository is a node within the NCI Cancer Research Data Commons (CRDC) and offers radiology, brightfield, and fluorescence slide microscopy images, along with image-derived data and clinical information. A key feature of IDC is its commercial-friendly licensing, with over 95% of its data covered by the CC-BY license. IDC ingests data from various sources, including TCGA and TCIA, and harmonizes it into DICOM format.

#### The Cancer Genome Atlas (TCGA) and Related Initiatives

TCGA is a massive undertaking that has molecularly characterized over 20,000 cancer samples across 33 cancer types. Datasets derived from TCGA are valuable for both liver and kidney research.

*   **TCGA Kidney Cancers:** This dataset is a bulk RNA-seq dataset containing transcriptome profiles of patients with three different subtypes of kidney cancers.
*   **Liver Hepatocellular Carcinoma (TCGA, PanCancer Atlas):** This dataset provides summary data visualizations and clinical data from 372 liver hepatocellular carcinomas. It includes clinical data such as mutation counts, patient demographics, and chromosomal gain or loss.
*   **Kidney Renal Papillary Cell Carcinoma (TCGA, PanCancer Atlas):** This dataset offers summary data and clinical data for 283 kidney renal papillary cell carcinomas, including information on mutations, demographics, and staging.

#### PLCO (Prostate, Lung, Colorectal, and Ovary Cancer Screening Trial)

The PLCO initiative provides datasets for liver and kidney cancer research.

*   **PLCO Liver Dataset:** This dataset contains comprehensive study data for liver cancer incidence and mortality analyses, with one record per participant. Access to the data in SAS or CSV format requires initiating a new PLCO project and project approval.
*   **PLCO Renal Dataset:** Similar to the liver dataset, this resource offers comprehensive study data for renal cancer incidence and mortality analyses, with each participant having one record.

#### Imaging-Focused Datasets

Several datasets specifically focus on medical imaging for liver and kidney conditions:

*   **Blood–Liver–Kidney Tri-Organ Imaging Dataset:** Released in December 2025, this dataset includes distinct subsets for blood cell detection, liver tissue analysis, and kidney tissue analysis, totaling 2,874 images with annotations.
*   **Dartmouth Kidney Cancer Histology Dataset:** This dataset comprises 563 H&E-stained whole-slide images of renal cell carcinoma (RCC), with labels for the predominant histological pattern. Access is granted by filling out a form.
*   **Duke Liver Dataset:** This dataset contains 2,146 abdominal MRI series (113,280 unique images) from 105 patients with cirrhotic features. It includes hand-drawn liver segmentation masks for 310 image series. The dataset is available for download from Zenodo.
*   **Kidney and Tumor Segmentation (KiTS) Dataset:** This dataset provides annotated CT scans of kidneys and kidney tumors, suitable for both organ-level and lesion-level segmentation tasks.
*   **Liver Tumor Segmentation (LiTS) Dataset:** A standard reference for liver and lesion segmentation in CT imaging, LiTS includes 201 abdominal CT scans with liver and tumor annotations.
*   **LiverHccSeg:** This dataset offers multiphasic MRI scans with liver and hepatocellular carcinoma (HCC) tumor segmentations, validated by two radiologists. It is available under a CC BY-NC-ND license.
*   **TRUSTED (Tridimensional Renal Ultra Sound TomodEnsitometrie Dataset):** This dataset comprises paired 3D ultrasound and CT kidney images from 48 human patients, including segmentation and landmark annotations.
*   **Open Kidney Dataset:** This dataset features over 500 2D B-mode abdominal ultrasound images with expert annotations for kidney segmentation. It is available for non-commercial use.
*   **CT KIDNEY DATASET: Normal-Cyst-Tumor and Stone:** This dataset contains 12,446 unique CT images of kidneys, categorized into normal, cyst, tumor, and stone findings.

#### Gene Expression and Omics Datasets

*   **CancerLivER:** This database maintains gene expression datasets for liver cancer, including 115 datasets with gene-expression profiles of 9,611 samples. It was last updated in 2020.
*   **Renal cell carcinoma Datasets (BioGPS):** BioGPS hosts various datasets related to renal cell carcinoma, including expression data from tumors, cell lines, and metastasis studies.

### Notable Papers and Descriptions

*   **"Blood–Liver–Kidney Tri-Organ Imaging Dataset"**: This dataset, released in late 2025, introduces a multi-modal imaging resource for object detection and tissue classification, covering blood cells, liver tissue, and kidney tissue.
*   **"Dartmouth Kidney Cancer Histology Dataset"**: This dataset provides 563 whole-slide images of renal cell carcinoma, useful for developing deep learning models for histology image analysis.
*   **"Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels"**: This publication describes a dataset of 2,146 abdominal MRI series from 105 patients, offering liver segmentation masks for training segmentation models.
*   **"LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis"**: This paper introduces a curated dataset for liver and HCC tumor segmentation on multiphasic contrast-enhanced MRI, including inter-rater agreement analysis.
*   **"TRUSTED: The Paired 3D Ultrasound and CT Human Data for Kidney Segmentation and Registration Research"**: This work proposes a dataset of paired 3D ultrasound and CT kidney images from 48 patients, annotated for segmentation and registration research.
*   **"Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics"**: This publication details a publicly available, multiphase 3D CECT dataset of 278 primary liver cancer patients with expert lesion annotations, aiming to support AI model development.
*   **"Kidney stone detection via axial CT imaging: A dataset for AI and deep learning applications"**: This article introduces a comprehensive CT scan image dataset for kidney stone detection, comprising over 3300 original CT images and over 35,000 augmented images.

### What to Watch

*   **NCI Imaging Data Commons (IDC):** Continuously expanding, IDC is a key resource to monitor for new cancer imaging datasets, with its CC-BY licensing making it highly accessible.
*   **New Releases from TCGA and PLCO:** These large-scale initiatives are ongoing sources for comprehensive clinical and genomic data, with new data releases expected.
*   **Emerging Imaging Datasets:** The trend towards specialized imaging datasets (e.g., multiphase CT for liver cancer, paired US/CT for kidneys) is likely to continue, offering more targeted resources. Datasets like the "Blood–Liver–Kidney Tri-Organ Imaging Dataset" (December 2025) indicate a move towards multi-organ and multi-modal data integration.

### Possible Clinical Relevance

The availability of these diverse datasets has significant clinical implications:

*   **Improved Diagnostics:** High-quality, annotated imaging datasets enable the development of AI models for earlier and more accurate detection of liver and kidney diseases, including cancers and stones.
*   **Enhanced Segmentation and Characterization:** Datasets with detailed segmentation masks (e.g., Duke Liver Dataset, LiTS, KiTS) are crucial for precise tumor volume measurement, treatment planning, and monitoring treatment response.
*   **Personalized Medicine:** Genomic and clinical data from TCGA and similar projects, combined with imaging data, can facilitate research into personalized treatment strategies for liver and kidney cancers.
*   **Surgical Planning:** Datasets with detailed anatomical annotations (e.g., TRUSTED) can aid in the development of tools for pre-operative planning and simulation.
*   **Non-Commercial Research Advancement:** Datasets with permissive licenses like CC-BY foster wider collaboration and accelerate research across academic institutions globally.

## Sources

*   Blood–Liver–Kidney Tri-Organ Imaging Dataset. (n.d.). Kaggle. Retrieved from 
*   Dartmouth Kidney Cancer Histology Dataset. (n.d.). Retrieved from 
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels. (n.d.). Radiology: Artificial Intelligence. Retrieved from 
*   Kidney and Tumor Segmentation (KiTS) Dataset. (n.d.). Retrieved from 
*   Kidney stone detection via axial CT imaging: A dataset for AI and deep learning applications. (n.d.). Springer Nature. Retrieved from https://link.springer.com/article/10.1007/s10462-025-11310-x
*   Liver Cancer Expression Resource (CancerLivER). (n.d.). Retrieved from https://webs.iiitd.edu.in/raghava/cancerliver/
*   Liver Hepatocellular Carcinoma (TCGA, PanCancer Atlas) - MSK Data Catalog. (n.d.). Retrieved from 
*   Liver Tumor Segmentation (LiTS) Dataset. (n.d.). Retrieved from 
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis. (n.d.). PubMed Central. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10587725/
*   NCI Imaging Data Commons (IDC). (n.d.). Retrieved from https://imaging.datacommons.cancer.gov/
*   Open Kidney Dataset. (n.d.). Retrieved from 
*   PLCO Datasets - Renal. (n.d.). The Cancer Data Access System. Retrieved from https://cdas.cancer.gov/plco/datasets/renal/
*   PLCO Datasets - Liver. (n.d.). The Cancer Data Access System. Retrieved from https://cdas.cancer.gov/plco/datasets/liver/
*   Public Medical Image Datasets for Segmentation Foundation Models. (n.d.). Retrieved from 
*   Renal cell carcinoma Datasets. (n.d.). BioGPS. Retrieved from 
*   TCGA Kidney Cancers - UCI Machine Learning Repository. (n.d.). UCI Machine Learning Repository. Retrieved from https://doi.org/10.24432/C5702T
*   TRUSTED: The Paired 3D Ultrasound and CT Human Data for Kidney Segmentation and Registration Research. (n.d.). Springer Nature. Retrieved from https://link.springer.com/article/10.1007/s10462-025-11310-x
*   CT KIDNEY DATASET: Normal-Cyst-Tumor and Stone. (n.d.). Kaggle. Retrieved from 
*   Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics. (n.d.). PubMed Central. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11396262/