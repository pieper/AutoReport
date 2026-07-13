# Research Report: Liver-Kidney-Data
*Generated: 2026-07-13 UTC*

# Liver and Kidney Datasets: A Comprehensive Report

## Executive Summary

This report synthesizes the current landscape of freely available liver and kidney imaging datasets, with a focus on cancer-related data. Key findings indicate a growing availability of high-quality, annotated datasets, particularly for liver and kidney tumors. Datasets like the Liver Tumor Segmentation Benchmark (LiTS) and the Kidney and Kidney Tumor Segmentation (KiTS) challenges offer substantial patient numbers and scan quantities, often accompanied by detailed annotations and associated clinical data. Recent advancements include the introduction of multi-phase CT datasets for liver cancer and expanded cohorts for kidney tumor segmentation. While many datasets are open for research, licensing terms vary, with CC-BY-NC-SA licenses being prevalent, necessitating careful review for specific use cases.

## Key Announcements and Notable Datasets

### Liver Datasets

*   **The Liver Tumor Segmentation Benchmark (LiTS):** This benchmark dataset, organized in conjunction with ISBI and MICCAI, provides a diverse set of 131 CT volumes with primary and secondary liver tumors. It includes manual segmentations for the liver and tumors, facilitating research in segmentation and detection. Some processed versions are adapted for classification tasks.
*   **ATLAS Dataset (Tumour and Liver Automatic Segmentation):** A publicly available dataset focusing on contrast-enhanced MRI scans of Hepatocellular Carcinoma (HCC). It contains 90 liver-focused CE-MRI acquisitions with corresponding liver and tumor segmentation masks, making it a valuable resource for automated delineation tools.
*   **LiverHccSeg:** This dataset offers multiphasic MRI scans with manual segmentations for liver and HCC tumors, annotated by two radiologists. It includes metadata and an inter-rater agreement analysis, providing a solid foundation for algorithm validation.
*   **Primary Liver Cancer CECT Imaging Dataset (PLC-CECT):** A comprehensive collection of 3D contrast-enhanced CT (CECT) images from 275 liver cancer patients (HCC, ICC, cHCC-CCA) and 83 controls. It features complete multi-phase coverage (Plain, Arterial, Venous, Delayed) and over 50,000 annotated slices, useful for classification and segmentation models. Access requires a data access request.
*   **Duke Liver Dataset (DLDS):** Comprising 2146 abdominal MRI series from 105 patients with liver cirrhosis indications, DLDS includes 310 series with manually segmented liver masks. It's suitable for training series classification or liver segmentation models, and potentially for segmenting other abdominal organs.
*   **CARE-Liver:** This dataset includes multi-phase and multi-center MRI data from 610 patients with liver fibrosis, acquired across different scanner vendors. It features T2-weighted, diffusion-weighted, and Gd-EOB-DTPA-enhanced dynamic MRIs across various phases, suitable for liver fibrosis staging.
*   **CT-ORG Dataset:** While not exclusively liver-focused, this dataset of 140 CT scans includes segmentations for five organs, including the liver, with many exhibiting liver lesions (benign and malignant). It's useful for multi-class organ segmentation.

### Kidney Datasets

*   **Kidney and Kidney Tumor Segmentation (KiTS) Datasets:** The KiTS challenges have produced several valuable datasets. The KiTS19 dataset, available on TCIA, contains CT scans and segmentations for 210 patients with kidney and kidney tumors. KiTS23 expands on this with 489 training cases and 110 test cases, including nephrogenic contrast phase data. The data is available under a CC BY-NC-SA 4.0 license.
*   **CT-ORG Dataset:** As mentioned above, this dataset includes segmented kidneys alongside other organs, making it relevant for kidney-focused research.
*   **TCGA-KIRC (The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma):** This collection provides CT scans matched to clinical, genetic, and pathological data from the TCGA project, focusing on clear cell renal cell carcinoma. Imaging data is available via TCIA.
*   **CPTAC-CCRCC (Clinical Proteomic Tumor Analysis Consortium Clear Cell Renal Cell Carcinoma):** Similar to TCGA-KIRC, this collection links radiology and pathology images with proteomic, genomic, and clinical data for clear cell renal cell carcinoma patients.
*   **Open Kidney Dataset:** This dataset provides over 500 2D B-mode abdominal ultrasound images with expert annotations for four classes. It is available for non-commercial use under a CC BY-NC-SA license.
*   **Multi and Hyperspectral Kidney Image Dataset:** A collection of 20,000 images (hyperspectral and multispectral) for classifying normal vs. tumor kidney tissue. It is released under CC0 (Public Domain).
*   **Kidney Stone Detection Dataset:** Focused on kidney stone detection, this dataset contains CT images with annotations for stone and non-stone cases.

## Notable Papers

*   **The Liver Tumor Segmentation Benchmark (LiTS):** This work reports the setup and results of the LiTS benchmark, highlighting the performance of various segmentation algorithms on a diverse dataset of liver tumors.
*   **The state of the art in kidney and kidney tumor segmentation in contrast-enhanced CT imaging: Results of the KiTS19 challenge:** This paper details the KiTS19 challenge, including the dataset and the performance of participating teams in segmenting kidneys and kidney tumors.
*   **Primary Liver Cancer CECT Imaging Dataset (PLC-CECT):** This paper introduces the PLC-CECT dataset, emphasizing its comprehensive multi-phase CT scans and annotations for various liver cancer subtypes, facilitating diagnostic and segmentation model development.
*   **ATLAS: A Tumour and Liver Automatic Segmentation Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma:** This study presents the ATLAS dataset, the first public dataset with CE-MRI of HCC and annotations, aiming to advance automated segmentation tools.
*   **LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis:** This paper describes the LiverHccSeg dataset, emphasizing the value of dual-radiologist annotations for benchmarking segmentation algorithms.

## What to Watch

*   **Continued expansion of KiTS datasets:** The Kidney and Kidney Tumor Segmentation (KiTS) challenge continues to evolve, with KiTS23 offering an expanded training set and new data phases, indicating ongoing efforts to enhance kidney imaging datasets.
*   **Emergence of multi-phase and multi-modal datasets:** Datasets like PLC-CECT and CARE-Liver highlight a trend towards including multi-phase imaging and multiple modalities (e.g., CT, MRI) to capture a more comprehensive view of liver diseases.
*   **Integration with multi-omics data:** Datasets linked to TCGA and CPTAC (e.g., TCGA-KIRC, CPTAC-CCRCC) are increasingly integrating imaging data with genomic and proteomic information, enabling deeper correlative studies.
*   **Focus on specific cancer subtypes and clinical relevance:** New datasets are increasingly focusing on specific subtypes of liver and kidney cancer (e.g., HCC, ICC, ccRCC) and their associated clinical data, aiming for more targeted research and clinical translation.

## Possible Clinical Relevance

The availability of these diverse and well-annotated datasets is crucial for advancing medical imaging research. They serve as the backbone for developing and validating AI algorithms for:

*   **Early Detection and Diagnosis:** Improved segmentation and classification models can aid in the early and accurate detection of liver and kidney tumors, potentially leading to better patient outcomes.
*   **Treatment Planning:** Precise segmentation of tumors and organs is essential for radiotherapy planning and surgical guidance, minimizing damage to healthy tissue.
*   **Prognosis and Monitoring:** Radiomic features extracted from these datasets can contribute to predicting disease progression and monitoring treatment response.
*   **Personalized Medicine:** By correlating imaging data with genomic and clinical information, researchers can work towards personalized treatment strategies for liver and kidney cancers.
*   **Reducing Radiologist Workload:** Automated tools developed using these datasets can help alleviate the burden on radiologists by providing rapid and consistent image analysis.

## Sources

*   Liver Tumor Segmentation - Kaggle. `
*   A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma - MDPI. `
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC. `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10849353/`
*   Primary Liver Cancer CECT Imaging Dataset - ScienceDB. `
*   Primary Liver Cancer CECT Imaging Dataset (PLC-CECT) - GitHub. `
*   The Liver Tumor Segmentation Benchmark (LiTS). `
*   Primary Liver Cancer CECT Imaging Dataset. `
*   Kidney and Kidney Tumor Segmentation Data - Technology Commercialization. `
*   m-aryayi/Medical-Imaging-Datasets: Publicly available medical imaging datasets for research and analysis. - GitHub. `
*   KiTS23 | The 2023 Kidney Tumor Segmentation Challenge. `
*   C4KC-KITS - The Cancer Imaging Archive (TCIA). `
*   Hyper and Multispectral Kidney Image dataset - Kaggle. `
*   [1901.04056] The Liver Tumor Segmentation Benchmark (LiTS) - arXiv. `
*   CPTAC-CCRCC - The Cancer Imaging Archive (TCIA). `
*   seongun/liver-tumor-classification · Datasets at Hugging Face. `
*   The Liver Tumor Segmentation Benchmark (LiTS) - PMC. `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10633098/`
*   Open Kidney Dataset | kidneyUS. `
*   CT-ORG - The Cancer Imaging Archive (TCIA). `
*   The state of the art in kidney and kidney tumor segmentation in contrast-enhanced CT imaging: Results of the KiTS19 challenge - PMC. `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7276301/`
*   Kidney Tumor Segmentation Based on DWR-SegFormer - MDPI. `
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC. `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10137467/`
*   Public Medical Image Datasets for Segmentation Foundation Models. `
*   GitHub - cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification. `
*   LiMT: a multi-task liver image benchmark dataset - arXiv. `
*   Liver - Datasets - PLCO - The Cancer Data Access System. `https://cdas.cancer.gov/plco/datasets/`
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series LabelsRadiology: Artificial Intelligence - RSNA Journals. `
*   CARE-Liver. `
*   Datasets: Imaging, Labels - The PI-CAI Challenge. `https://picai.org/datasets/`
*   The PI-CAI Challenge: Public Training and Development Dataset - Zenodo. `
*   Medical Imaging Datasets — PYCAD. `
*   B-MODE-AND-CEUS-LIVER - The Cancer Imaging Archive (TCIA). `
*   General Dataset (TCIA) - Kaggle. `
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset | Kaggle. `
*   Liver Cancer Multiclass Dataset - Kaggle. `
*   Published Datasets - ICCR-cancer.org. `
*   Artificial Intelligence in Renal Imaging: A Multi-Dataset Study for Kidney Disease Classification - MDPI. `
*   Liver cancer Datasets - BioGPS. `
*   TCGA-KIRC | The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma Collection. `
*   AI: Tasks, Evaluation - The PI-CAI Challenge. `https://picai.org/ai-tasks-evaluation/`
*   DIAGNijmegen/picai_baseline: Baseline AI models for 3D csPCa detection/diagnosis in bpMRI - GitHub. `