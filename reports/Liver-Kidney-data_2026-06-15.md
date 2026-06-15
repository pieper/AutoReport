# Research Report: Liver-Kidney-Data
*Generated: 2026-06-15 UTC*

## Executive Summary

This report details freely available datasets for liver and kidney research, focusing on quality, patient numbers, scan diversity, annotation availability, and clinical data. Key datasets include the TCGA Liver Hepatocellular Carcinoma collection, the Liver Tumor Segmentation Benchmark (LiTS), and the Kidney and Kidney Tumor Segmentation Challenge (KiTS19). Recent developments highlight comprehensive multiphase CT datasets for liver cancer and advancements in kidney tumor segmentation with integrated clinical data. The datasets generally permit non-commercial use, with some offering CC-BY licenses.

## Key Announcements and Datasets

### Liver Datasets

*   **The Cancer Genome Atlas (TCGA) Liver Hepatocellular Carcinoma (LIHC) Collection:**
    *   Provides extensive clinical and genomic data for a large number of liver hepatocellular carcinomas.
    *   Includes imaging data (radiological) stored separately on The Cancer Imaging Archive (TCIA).
    *   Offers data visualizations, mutation counts, gene information, demographics, and more.
    *   License: Publicly available, with some features requiring login.

*   **Liver Tumor Segmentation Benchmark (LiTS):**
    *   A diverse CT dataset with primary and secondary liver tumors, varying in size and appearance.
    *   Collaborated with seven hospitals and research institutions.
    *   Comprises 131 CT volumes for training and 70 for testing.
    *   Includes manual segmentations for livers and tumors.
    *   License: Data and online evaluation are accessible via CodaLab.

*   **Primary Liver Cancer CECT Imaging Dataset:**
    *   Features 278 cases of primary liver cancer (HCC, ICC, cHCC-CCA) with complete 3D contrast-enhanced CT (CECT) data across four phases (Plain, Arterial, Venous, Delayed).
    *   Includes annotations for liver and lesion regions.
    *   Contains 50,560 slices with lesions.
    *   License: Not explicitly stated as free for all uses, but presented as a resource for development and validation.

*   **LiverHccSeg Dataset:**
    *   Provides liver and tumor segmentations on multiphasic contrast-enhanced MRI for hepatocellular carcinoma (HCC).
    *   Includes manual segmentations by two radiologists, allowing for inter-rater agreement analysis.
    *   Derived from the TCGA-LIHC database.
    *   License: Publicly available.

*   **Duke Liver Dataset (DLDS):**
    *   Contains 2146 abdominal MRI series from 105 patients, with a focus on liver cirrhosis.
    *   Includes binary masks of hand-drawn, whole-organ liver segmentations for 310 image series.
    *   Well-suited for liver segmentation models.
    *   License: Data release approved by licensing committee, requirement for consent waived due to retrospective nature and de-identification.

### Kidney Datasets

*   **Kidney and Kidney Tumor Segmentation Challenge (KiTS19):**
    *   A dataset of CT scans for 210 patients with manual semantic segmentations of kidneys and tumors.
    *   Imaging collected during routine care, leading to heterogeneity in scanner manufacturers and protocols.
    *   Segmentations are for the corticomedullary phase.
    *   License: CC BY 3.0.

*   **KiTS19 Challenge Data (Expanded):**
    *   A collection of multi-phase CT imaging, segmentation masks, and clinical outcomes for 300 patients.
    *   210 cases are publicly released as the training set for the 2019 MICCAI KiTS Kidney Tumor Segmentation Challenge.
    *   License: CC BY-NC-SA.

*   **MMIST ccRCC Dataset:**
    *   Curated from CPTAC-CCRCC and TCGA-KIRC datasets, focusing on clear cell renal cell carcinoma (ccRCC).
    *   Includes multi-modal data: CT, MRI, Whole Slide Images (WSI), Genomics, and Clinical data.
    *   License: Access to original data from TCGA and CPTAC repositories.

*   **Mendeley Data - Renal Malignancy Dataset:**
    *   A dataset for classifying renal malignancy, part of a larger collection of medical imaging.
    *   License: CC BY 4.0.

*   **Open Kidney Dataset:**
    *   Over 500 2D B-mode abdominal ultrasound images with two sets of polygon annotations by an expert sonographer.
    *   Four classes are available for non-commercial use.
    *   License: For non-commercial use.

*   **Hyper and Multispectral Kidney Image dataset:**
    *   A balanced collection of 20,000 hyperspectral and multispectral kidney images for classifying normal vs. tumor tissue.
    *   License: CC0: Public Domain.

### Combined Liver and Kidney Datasets

*   **Blood–Liver–Kidney Tri-Organ Imaging Dataset:**
    *   A multi-modal dataset for object detection and tissue classification.
    *   Includes separate datasets for blood cell detection, liver tissue analysis, and kidney tissue analysis.
    *   License: Not explicitly stated, but Kaggle datasets often have open usage policies.

## Notable Papers and Descriptions

*   **The Liver Tumor Segmentation Benchmark (LiTS):** This work details the setup and results of the LiTS benchmark, highlighting the diversity of the image dataset and the performance of segmentation algorithms.
*   **The KiTS19 Challenge Data:** This paper introduces the KiTS19 challenge dataset, featuring CT imaging, segmentation masks, and clinical outcomes for kidney tumor patients, serving as a resource for segmentation models and biomarker studies.
*   **Primary Liver Cancer CECT Imaging Dataset:** This dataset, rich in liver cancer types and complete in CT phasing, facilitates the development and validation of diagnostic classification and lesion segmentation models.
*   **LiverHccSeg:** This paper describes LiverHccSeg, a public dataset with liver and HCC tumor segmentations on multiphasic contrast-enhanced MRI, valuable for evaluating segmentation algorithms.
*   **MMIST ccRCC Dataset:** This resource provides multi-modal data (CT, MRI, WSI, Genomics, Clinical) for clear cell renal cell carcinoma (ccRCC), aiming to aid prognosis estimation and patient management.
*   **Open Kidney Dataset:** This work presents a dataset of annotated ultrasound images for kidney analysis, addressing the lack of open ultrasound data for AI research.
*   **Imaging-based deep learning in kidney diseases:** This review discusses the application of imaging-based deep learning in kidney diseases, covering organ segmentation, lesion detection, and diagnosis, while also outlining current challenges and future prospects.

## What to Watch

*   **Continued expansion of TCGA data:** The Cancer Genome Atlas project is ongoing, with potential for further data releases related to liver and kidney cancers.
*   **New challenges and datasets:** Keep an eye on upcoming challenges organized by institutions like MICCAI, ISBI, and Kaggle, which often release new, valuable datasets.
*   **Advancements in multi-modal data integration:** Datasets like MMIST ccRCC, which combine imaging with genomic and clinical data, are becoming increasingly important and may see more examples emerge.

## Possible Clinical Relevance

These datasets are crucial for advancing AI in medical imaging, with direct clinical relevance for:

*   **Improved Cancer Diagnosis and Detection:** More accurate and earlier detection of liver and kidney tumors through enhanced imaging analysis.
*   **Personalized Treatment Planning:** AI models trained on these datasets can assist in surgical planning (e.g., precise tumor delineation for nephron-sparing surgery) and treatment selection.
*   **Prognosis Prediction:** Datasets with rich clinical data can enable the development of models to predict patient outcomes and inform treatment strategies.
*   **Reduced Healthcare Costs:** Automation of segmentation and analysis tasks can streamline workflows, potentially reducing the time and cost of diagnosis and follow-up.
*   **Development of Novel Biomarkers:** Integration of imaging, genomic, and clinical data may lead to the discovery of new imaging biomarkers for disease diagnosis and prognosis.

## Sources

*   Liver Hepatocellular Carcinoma (TCGA, PanCancer Atlas) - MSK Data Catalog.
*   The Liver Tumor Segmentation Benchmark (LiTS).
*   Primary Liver Cancer CECT Imaging Dataset.
*   Data from the training set of the 2019 Kidney and Kidney Tumor Segmentation Challenge (C4KC-KITS) - Cancer Imaging Archive Wiki.
*   Liver Hepatocellular Carcinoma - MSK Data Catalog.
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC.
*   TCGA-LIHC - The Cancer Imaging Archive (TCIA).
*   Challenge Data - KiTS19.
*   The Liver Tumor Segmentation Benchmark (LiTS) - PubMed - NIH.
*   The Cancer Genome Atlas Liver Hepatocellular Carcinoma Collection (TCGA-LIHC).
*   [1904.00445] The KiTS19 Challenge Data: 300 Kidney Tumor Cases with Clinical Context, CT Semantic Segmentations, and Surgical Outcomes - arXiv.
*   Liver and Liver Tumor Segmentation - Kaggle.
*   A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma - MDPI.
*   Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics | Radiology - RSNA Journals.
*   Liver Cancer Multiclass Dataset - Kaggle.
*   C4KC-KITS - The Cancer Imaging Archive (TCIA).
*   LiTS – Liver Tumor Segmentation Challenge (LiTS17) - Academic Torrents.
*   Hyper and Multispectral Kidney Image dataset - Kaggle.
*   Subset of LiTS Dataset for Liver and Tumor Segmentation - Zenodo.
*   AI in Medical Imaging: The Kidney Tumor Segmentation Challenge | Banook.
*   KITS 19 - Kidney Tumor Segmentation - Kaggle.
*   m-aryayi/Medical-Imaging-Datasets: Publicly available medical imaging datasets for research and analysis. - GitHub.
*   MMIST ccRCC Dataset.
*   Kidney Cancer Diagnosis and Surgery Selection by Machine Learning from CT Scans Combined with Clinical Metadata - PMC.
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC.
*   Advances in Artificial Intelligence‐Based Liver‐Related Semantic Segmentation Techniques and Applications Using CT Imaging - PMC.
*   GitHub - cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification.
*   Liver - Datasets - PLCO - The Cancer Data Access System.
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset - Kaggle.
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series LabelsRadiology: Artificial Intelligence - RSNA Journals.
*   Data - LUNA16 - Grand Challenge.
*   Liver Cell Atlas.
*   Open Kidney Dataset | kidneyUS.
*   Enhanced Ultrasound Superior to MRI for Diagnosing Certain Liver and Kidney Tumors, According to New Studies | Imaging Technology News.
*   Imaging-based deep learning in kidney diseases: recent progress and future prospects.
*   Medical Imagining (CT scan, MRI, X-ray, and Microscopic Imagery) Data - Mendeley Data.
*   LIDC-IDRI - The Cancer Imaging Archive (TCIA).
*   LIDC-IDRI-DRR.
*   LiMT: a multi-task liver image benchmark dataset - arXiv.
*   LIDC-IDRI-DRR.
*   GitHub - jaeho3690/LIDC-IDRI-Segmentation: This is the segmentation process of the LIDC-IDRI dataset. Checkout my preprocessing repository to use this repository.