# Research Report: Liver-Kidney-Data
*Generated: 2026-04-27 UTC*

## Executive Summary

This report synthesizes the current landscape of freely available liver and kidney imaging datasets, focusing on those suitable for research in cancer and other well-described diseases. Recent advancements have seen an increase in datasets with detailed annotations, multi-phase imaging, and associated clinical data, enhancing their utility for developing AI models. Notably, several new datasets have emerged with a focus on hepatocellular carcinoma (HCC) and clear cell renal cell carcinoma (ccRCC), offering rich annotation and multi-modal data. The availability of non-restrictive licenses, such as CC BY, is increasing, which is crucial for broad research adoption.

## Key Announcements, Grouped by Organization

### The Cancer Imaging Archive (TCIA)

TCIA continues to be a primary resource for medical imaging datasets, including those for liver and kidney diseases. Several collections have been updated or added, offering detailed annotations and associated clinical and genomic data for various cancers.

*   **CPTAC-CCRCC Annotations:** Provides image annotations for clear cell renal cell carcinoma (ccRCC) derived from the Clinical Proteomic Tumor Analysis Consortium (CPTAC) collection. These annotations include three-dimensional segmentations of lesions, reviewed by radiologists, aiming to improve their value for AI research.
*   **TCGA-KIRC:** This collection offers CT scans for kidney renal clear cell carcinoma, linked with clinical, genetic, and pathological information. While images are heterogeneous due to their multi-institutional origin, the matched data allows for correlations between genotype, radiological phenotype, and patient outcomes.
*   **CT-ORG:** This dataset contains 140 CT scans with segmentations for multiple organs, including the liver and kidneys. It is particularly useful for training organ segmentation algorithms, as it includes images with various lesions and from diverse imaging conditions.

### Grand Challenges & Academic Consortia

Several platforms and research groups are actively releasing comprehensive datasets.

*   **ATLAS Dataset (University of Burgundy):** Introduces the first public dataset of contrast-enhanced MRI (CE-MRI) for hepatocellular carcinoma (HCC), featuring 90 patient scans with liver and tumor segmentation masks. This is specifically designed to facilitate the development of automated segmentation tools for treatment planning.
*   **LiverHccSeg Dataset:** Offers a curated resource of contrast-enhanced multiphasic MRI scans for HCC, with manual segmentations by two radiologists. It includes an analysis of inter-rater agreement, providing a robust foundation for algorithm validation.
*   **Primary Liver Cancer CECT Imaging Dataset (Luo et al.):** This dataset comprises 278 cases of primary liver cancer (HCC, ICC, cHCC-CCA) using full-phase 3D CECT scans. It includes annotations for liver and lesion regions, aiming to improve diagnostic classification and lesion segmentation models.
*   **MMIST ccRCC Dataset:** Curated from CPTAC-CCRCC and TCGA-KIRC, this dataset focuses on clear cell renal cell carcinoma (ccRCC) and integrates CT, MRI, Whole Slide Images (WSI), genomics, and clinical data, offering a multi-modal approach for prognosis estimation.
*   **KITS19/KITS23 (Kidney and Kidney Tumor Segmentation Challenge):** These challenges have released datasets with CT scans and manual semantic segmentations of kidneys and tumors. KITS19 includes 210 patients, while KITS23 expands this with 599 cases, aiming to accelerate progress in automatic 3D semantic segmentation.
*   **CHAOS (Combined CT-MR Healthy Abdominal Organ Segmentation):** While primarily focused on healthy organs, the dataset includes segmentations for liver, spleen, and kidneys from both CT and MRI. This can be valuable for general abdominal organ segmentation tasks.
*   **FLARE21:** This challenge dataset focuses on abdominal organ segmentation (liver, kidney, spleen, pancreas) using CT data, with annotations for 100 test cases. It incorporates data adapted from other sources under license.

### Kaggle & Other Repositories

*   **Blood–Liver–Kidney Tri-Organ Imaging Dataset:** A multi-modal dataset designed for object detection and tissue classification, including separate datasets for blood cell detection, liver tissue analysis, and kidney tissue analysis.
*   **Duke Liver Dataset:** Contains a large collection of abdominal MRI series from patients with liver cirrhosis, including manually segmented liver masks. It can serve as a foundation for segmenting other abdominal organs.

## Notable Papers Describing Datasets

*   **ATLAS Dataset:** Introduces the first public dataset of CE-MRI for HCC with liver and tumor segmentation annotations, facilitating automated delineation for treatment planning.
*   **LiverHccSeg Dataset:** Presents a curated resource for HCC liver and tumor segmentation using multiphasic CE-MRI, with dual radiologist annotations and inter-rater agreement analysis.
*   **Primary Liver Cancer CECT Imaging Dataset:** Describes a large dataset of full-phase 3D CECT scans for various primary liver cancer types, including detailed annotations for improved diagnostic and segmentation models.
*   **MMIST ccRCC Dataset:** Details a multi-modal dataset for ccRCC integrating CT, MRI, WSI, genomics, and clinical data to aid in prognosis estimation.
*   **KITS19 Challenge Data:** Introduces a dataset of CT scans and manual semantic segmentations for kidneys and kidney tumors, aimed at advancing automatic 3D semantic segmentation.
*   **Duke Liver Dataset:** Describes a large collection of abdominal MRI series from liver cirrhosis patients with manual liver segmentations, useful for organ segmentation model development.

## What to Watch

*   **Ongoing Challenges and Updates:** Platforms like Grand Challenges and The Cancer Imaging Archive (TCIA) frequently host new challenges and update existing datasets. Researchers should monitor these platforms for emerging collections related to liver and kidney imaging.
*   **Multi-Modal Data Integration:** The trend towards multi-modal datasets (e.g., imaging, genomics, clinical data) is expected to continue, offering richer insights into disease mechanisms and patient outcomes. Datasets like MMIST ccRCC exemplify this trend.
*   **Advancements in Annotation Quality:** As seen with LiverHccSeg and CPTAC-CCRCC Annotations, there's a continuous effort to improve annotation quality through expert review and inter-rater agreement analysis, which is critical for robust AI model development.

## Possible Clinical Relevance

The datasets described herein hold significant potential for clinical relevance by enabling the development and validation of AI-powered tools for:

*   **Early Diagnosis and Detection:** Improved segmentation and classification models can lead to earlier and more accurate identification of liver and kidney cancers and other pathologies.
*   **Treatment Planning and Monitoring:** Precise segmentation of tumors and organs is crucial for radiation therapy planning, surgical guidance, and monitoring treatment response. Datasets like ATLAS and Primary Liver Cancer CECT Imaging Dataset are directly contributing to this.
*   **Prognostic Assessment:** Integrating imaging data with clinical and genomic information, as seen in datasets like MMIST ccRCC, can lead to more accurate prognostic models, aiding in personalized treatment strategies.
*   **Reducing Inter-Observer Variability:** Datasets with multiple annotations and inter-rater agreement analyses (e.g., LiverHccSeg) help in developing models that can achieve consistent and reliable segmentations, reducing human error.
*   **Surgical Planning:** Accurate delineation of organs and lesions is vital for minimally invasive procedures, such as partial nephrectomies or liver transplant evaluations. Datasets like KITS and CHAOS support this area.

## Sources

*   ATLAS Dataset. https://atlas-challenge.u-bourgogne.fr
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10535748/
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset. 
*   Primary Liver Cancer CECT Imaging Dataset. https://github.com/ljwa2323/PLC_CECT
*   Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics. 
*   CPTAC-CCRCC-TUMOR-ANNOTATIONS. 
*   CODEX imaging of HCC. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8036479/
*   MMIST ccRCC Dataset. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8861737/
*   TCGA-KIRC - The Cancer Imaging Archive (TCIA). https://www.cancerimagingarchive.net/collection/tcga-kirc/
*   CT-ORG - The Cancer Imaging Archive (TCIA). https://www.cancerimagingarchive.net/collection/ct-org/
*   CPTAC-CCRCC - The Cancer Imaging Archive (TCIA). https://www.cancerimagingarchive.net/collection/cptac-ccrcc/
*   Public Medical Image Datasets for Segmentation Foundation Models. 
*   LiMT: a multi-task liver image benchmark dataset. https://arxiv.org/abs/2107.12180
*   Awesome Public Medical Imaging Datasets. https://github.com/m-aryayi/Medical-Imaging-Datasets
*   Data Info - CHAOS - Grand Challenge. 
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset. 
*   C4KC-KITS - The Cancer Imaging Archive (TCIA). https://www.cancerimagingarchive.net/collection/c4kc-kits/
*   Public Medical Imaging Datasets For Artificial Intelligence Models. 
*   UCSF RMaC: University of California San Francisco 3D Multi-Phase Renal Mass CT Dataset with Tumor Segmentations. https://www.medrxiv.org/content/10.1101/2026.02.11.26346096v1
*   AI in Medical Imaging: The Kidney Tumor Segmentation Challenge. 
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels. 
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series LabelsRadiology: Artificial Intelligence - RSNA Journals. 
*   Dataset And Baseline - FLARE21 - Grand Challenge. 
*   TCGA-KIRP (Kidney Renal Papillary Cell Carcinoma) - Hugging Face. 
*   GitHub - cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification. https://github.com/cradleai/LKS-Dataset
*   The 2023 Kidney Tumor Segmentation Challenge - KiTS23. 
*   Description - CHAOS - Grand Challenge. 
*   Liver - Datasets - PLCO - The Cancer Data Access System. https://cdas.cancer.gov/plco/datasets/
*   Datasets - Learn2Reg - Grand Challenge. 
*   Browse Collections - The Cancer Imaging Archive (TCIA). https://www.cancerimagingarchive.net/collections/
*   General Dataset (TCIA) - Kaggle. 
*   Liver Patient Dataset | Kaggle. 
*   liver disorders - Kaggle. 
*   Predict Liver Disease: 1700 Records Dataset - Kaggle. 
*   Liver Disorders - Kaggle. 
*   Duke Liver Dataset (MRI) v2 - Zenodo. https://zenodo.org/records/3760611
*   B-MODE-AND-CEUS-LIVER - The Cancer Imaging Archive (TCIA). https://www.cancerimagingarchive.net/collection/b-mode-and-ceus-liver/
*   Liver segmentation – 3D-ircadb-01 - IRCAD. https://www.ircad.fr/database/liver-segmentation-3d-ircadb-01/