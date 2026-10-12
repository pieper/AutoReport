# Research Report: Liver-Kidney-Data
*Generated: 2026-10-12 UTC*

## Executive Summary

This report details freely available datasets for liver and kidney research, focusing on imaging data with annotations and clinical information. Key datasets include the Liver Tumor Segmentation Benchmark (LiTS) for liver scans and the Kidney and Kidney Tumor Segmentation (KiTS) series for kidney data. Recent developments include the KiTS23 dataset with expanded cases and the MICCAI FLARE challenges, which have progressively increased in scale and complexity, incorporating more organs and semi-supervised learning. These datasets offer varying numbers of patients and scans, with quality generally good and annotations detailed, particularly for segmentation tasks. Clinical data availability differs across datasets, with some offering comprehensive information while others are limited. Licenses are predominantly open for research use, often with attribution requirements.

## Key Announcements and Datasets

### Liver Datasets

*   **Liver Tumor Segmentation Benchmark (LiTS):** This established dataset, a collaboration with seven hospitals, provides 131 CT volumes for training and 70 for testing, featuring primary and secondary liver tumors of various sizes and appearances. It has been used in conjunction with ISBI and MICCAI challenges.
*   **Duke Liver Dataset (DLDS):** This MRI dataset includes 2146 abdominal MRI series (113,280 images) from 105 patients, with liver segmentations for 310 series. It is particularly useful for training liver segmentation and series classification models.
*   **LiverHccSeg:** This dataset offers multiphasic MRI scans with liver and Hepatocellular Carcinoma (HCC) tumor segmentations. It includes 17 cases for liver segmentation and 14 for HCC tumor segmentation, with inter-rater agreement analysis.
*   **Primary Liver Cancer CECT Imaging Dataset:** This dataset contains 3D contrast-enhanced CT (CECT) data from 278 liver cancer cases (Hepatocellular Carcinoma, Intrahepatic Cholangiocarcinoma, and Combined Hepatocellular-Cholangiocarcinoma) and 83 non-liver cancer subjects. It includes annotations for liver and lesion regions across multiple phases.
*   **CARE-Liver:** This dataset focuses on liver fibrosis and includes multi-phase MRI scans from 610 patients. It supports research in automated liver segmentation and fibrosis staging.

### Kidney Datasets

*   **Kidney and Kidney Tumor Segmentation (KiTS) Series:**
    *   **KiTS19:** Provided 210 CT scans with manual segmentations of kidneys and tumors.
    *   **KiTS23:** The most recent iteration, featuring an expanded training set of 489 cases and a new test set of 110 cases. It includes cases from the "nephrogenic contrast phase" in addition to the "late arterial" phase.
*   **Open Kidney Dataset:** This dataset comprises over 500 2D B-mode abdominal ultrasound images with expert polygon annotations. It is available for non-commercial use.
*   **MICCAI FLARE Challenges:** These challenges have progressively released datasets for abdominal organ segmentation.
    *   **FLARE 2021:** Focused on segmenting liver, kidney, spleen, and pancreas in 511 CT scans.
    *   **FLARE 2022:** Expanded to 2,300 CT scans, including more organs (e.g., right and left kidneys) and using a semi-supervised setting.
    *   **FLARE 2023:** Further increased to 4,500 CT scans, incorporating pan-cancer segmentation alongside 13 abdominal organs.

### Multi-Organ Datasets (Including Liver and Kidney)

*   **CT-ORG:** This dataset contains 140 CT scans with labels for liver, kidneys, and other organs. It's suitable for training organ segmentation algorithms across diverse imaging conditions.
*   **AbdomenCT-1K:** This dataset includes CT scans with annotations for liver, kidneys, pancreas, and spleen.
*   **MMIST ccRCC Dataset:** While primarily focused on kidney cancer (ccRCC), this dataset includes CT and MRI modalities for a large number of patients, with potential for studying kidney-related imaging.
*   **Liver Kidney Stomach (LKS) Dataset:** This dataset consists of Immunofluorescence Whole Slide Images (WSIs) for research into autoimmune liver disease, containing sections of rodent kidney and liver tissue.

## Notable Papers

*   **The Liver Tumor Segmentation Benchmark (LiTS):** This work describes the setup and results of the LiTS benchmark, highlighting the performance of submitted segmentation algorithms on a diverse dataset of liver CT scans.
*   **KiTS23 | The 2023 Kidney and Kidney Tumor Segmentation Challenge:** This paper details the KiTS23 challenge, emphasizing its expanded dataset, inclusion of nephrogenic contrast phase imaging, and its role as a benchmark for kidney tumor segmentation.
*   **Automatic Segmentation of Kidneys and Kidney Tumors: The KiTS19 International Challenge:** This paper reports on the KiTS19 challenge, demonstrating how publicly available segmented data and an incentivized competition can drive advancements in automated kidney and kidney tumor segmentation.
*   **LiverHccSeg: A Publicly Available Multiphasic MRI Dataset with Liver and HCC Tumor Segmentations and Inter-Rater Agreement Analysis:** This publication introduces the LiverHccSeg dataset, providing multiphasic MRI data with manual liver and HCC tumor segmentations, and an analysis of inter-rater agreement to ensure data reliability.
*   **CT-ORG:** This dataset paper describes a collection of 140 CT scans with labels for multiple abdominal organs, designed to train and evaluate organ segmentation algorithms under various imaging conditions.

## What to Watch

*   **FLARE 2025:** The FLARE challenge continues to evolve, with FLARE 2025 focusing on critical clinical needs, including pan-cancer segmentation, unsupervised domain adaptation for MRI and PET scans, and foundational models for 3D CT and MRI. This indicates a trend towards more complex tasks and multi-modal data.
*   **Human Cell Atlas (HCA):** While not strictly imaging datasets for segmentation in the same vein as LiTS or KiTS, the HCA is making vast amounts of single-cell data available, including new Liver, Gut, and Kidney atlases, which may offer complementary multi-omic data for research.

## Possible Clinical Relevance

These datasets are crucial for developing and validating AI-driven tools that can assist in the diagnosis, treatment planning, and monitoring of liver and kidney diseases.

*   **Early Detection and Diagnosis:** Datasets like LiTS and KiTS enable the training of algorithms to automatically detect and segment tumors in CT and MRI scans, potentially leading to earlier and more accurate diagnoses of liver and kidney cancers.
*   **Treatment Planning:** Precise segmentation of organs and lesions is vital for surgical planning, radiation therapy targeting, and assessing treatment response. Datasets with detailed annotations support the development of more accurate segmentation models.
*   **Prognosis and Risk Stratification:** By correlating imaging features with clinical outcomes, these datasets can help develop models that predict disease progression or patient prognosis, aiding in personalized treatment strategies. The MMIST ccRCC dataset, for instance, aims to improve prognosis estimation for kidney cancer.
*   **Reducing Radiologist Workload:** Automated segmentation and detection tools developed from these datasets can help reduce the time and effort required for manual image analysis, allowing radiologists to focus on more complex cases.
*   **Understanding Disease Mechanisms:** Datasets with detailed annotations and clinical data, such as LiverHccSeg and CARE-Liver, can facilitate research into the underlying mechanisms of liver fibrosis and HCC, potentially leading to new therapeutic targets.

## Sources

*   The Liver Tumor Segmentation Benchmark (LiTS) - PMC - NIH: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10643389/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10643389/</a>
*   The Liver Tumor Segmentation Benchmark (LiTS): <a href="https://arxiv.org/abs/2102.09948" target="_blank">https://arxiv.org/abs/2102.09948</a>
*   Awesome-Medical-Dataset/resources/KiTS23.md at main - GitHub: 
*   KiTS23 | The 2023 Kidney and Kidney Tumor Segmentation Challenge: 
*   Data from the training set of the 2019 Kidney and Kidney Tumor Segmentation Challenge (C4KC-KiTS) - Cancer Imaging Archive Wiki: ))
*   Subset of LiTS Dataset for Liver and Tumor Segmentation | Zenodo: <a href="https://zenodo.org/records/19161543" target="_blank">https://zenodo.org/records/19161543</a>
*   Liver Tumor Segmentation - Kaggle: 
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset - Mendeley Data: 
*   The liver tumor segmentation benchmark (lits) - Gabriel Chartrand: 
*   MICCAI FLARE22 Challenge Dataset - Kaggle: 
*   Challenge Data - KiTS19: 
*   Automatic Segmentation of Kidneys and Kidney Tumors: The KiTS19 International Challenge - PMC: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7479901/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7479901/</a>
*   Dataset - MICCAI FLARE 2022 - Grand Challenge: 
*   Public Medical Image Datasets for Segmentation Foundation Models: 
*   Open Kidney Dataset | kidneyUS: 
*   cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification. · GitHub: <a href="https://github.com/cradleai/LKS-Dataset" target="_blank">https://github.com/cradleai/LKS-Dataset</a>
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10387228/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10387228/</a>
*   Liver - Datasets - PLCO - The Cancer Data Access System: 
*   Datasets - UCI Machine Learning Repository: <a href="https://archive.ics.uci.edu/" target="_blank">https://archive.ics.uci.edu/</a>
*   FLARE 2025 Challenge: 
*   JUNMA11/FLARE: Official Repository of MICCAI FLARE Challenges - GitHub: <a href="https://github.com/JunMa11/FLARE" target="_blank">https://github.com/JunMa11/FLARE</a>
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels | Radiology: Artificial Intelligence - RSNA Journals: 
*   A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels: 
*   Primary Liver Cancer CECT Imaging Dataset: <a href="https://github.com/ljwa2323/PLC_CECT" target="_blank">https://github.com/ljwa2323/PLC_CECT</a>
*   CFDE Liver Resource: 
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10204949/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10204949/</a>
*   MMIST ccRCC Dataset: 
*   CT-ORG - The Cancer Imaging Archive (TCIA): <a href="https://www.cancerimagingarchive.net/ct-org/" target="_blank">https://www.cancerimagingarchive.net/ct-org/</a>
*   LIDC-IDRI - The Cancer Imaging Archive (TCIA): <a href="https://www.cancerimagingarchive.net/lidc-idri/" target="_blank">https://www.cancerimagingarchive.net/lidc-idri/</a>
*   Computer-aided detection of pulmonary nodules: a comparative study using the public LIDC/IDRI database - PMC: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5749172/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5749172/</a>
*   siddharthdhara17/lidc-idri-text-annotations · Datasets at Hugging Face: <a href="https://huggingface.co/datasets/siddharthdhara17/lidc-idri-text-annotations" target="_blank">https://huggingface.co/datasets/siddharthdhara17/lidc-idri-text-annotations</a>
*   LiverHccSeg: A Publicly Available Multiphasic MRI Dataset with Liver and HCC Tumor Segmentations and Inter-Rater Agreement Analysis - NIAID Data Ecosystem: <a href="https://data.niaid.nih.gov/data/query/7957515" target="_blank">https://data.niaid.nih.gov/data/query/7957515</a>
*   TCGA-LIHC - The Cancer Imaging Archive (TCIA): <a href="https://www.cancerimagingarchive.net/tcga-lihc/" target="_blank">https://www.cancerimagingarchive.net/tcga-lihc/</a>
*   NCI's Collection of Datasets for Health, Medical, and Biomedical Research Purposes - NCBI: 
*   LiMT: a multi-task liver image benchmark dataset - arXiv: <a href="https://arxiv.org/abs/2311.14548" target="_blank">https://arxiv.org/abs/2311.14548</a>
*   CARE-Liver: 
*   DICOM-LIDC-IDRI-NODULES - The Cancer Imaging Archive (TCIA): <a href="https://www.cancerimagingarchive.net/dicom-lidc-idri-nodules/" target="_blank">https://www.cancerimagingarchive.net/dicom-lidc-idri-nodules/</a>