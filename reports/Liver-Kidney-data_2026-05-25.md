# Research Report: Liver-Kidney-Data
*Generated: 2026-05-25 UTC*

## Executive Summary

This report details the best available free datasets for liver and kidney imaging, focusing on those with a large number of patients and scans, high scan quality, available annotations, and supplementary clinical data. Datasets associated with well-described diseases, particularly cancers, and those with non-restrictive licenses (e.g., CC-BY) are prioritized. The Cancer Imaging Archive (TCIA) and The Cancer Genome Atlas (TCGA) collections are prominent sources, offering a wealth of data for both liver and kidney research. Newer developments include increased efforts to link imaging data with genomic and clinical information, enhancing the potential for precision medicine.

## Key Announcements and Notable Datasets

### The Cancer Imaging Archive (TCIA)

TCIA is a crucial repository for cancer imaging data, providing access to a vast collection of medical images.

*   **C4KC-KiTS (Kidney and Kidney Tumor Segmentation Challenge):** This dataset includes CT scans and manual semantic segmentations of kidneys and tumors for 210 patients. It offers clinical data and is licensed under CC BY 3.0.
*   **TCGA-LIHC (Liver Hepatocellular Carcinoma Collection):** This collection links clinical, genetic, and pathological data from The Cancer Genome Atlas (TCGA) with radiological data stored in TCIA for liver cancer research. It comprises approximately 500 specimens per cancer type.
*   **TCGA-KIRC (Kidney Renal Clear Cell Carcinoma Collection):** Similar to TCGA-LIHC, this dataset provides CT imaging data for kidney renal clear cell carcinoma patients, linked with clinical, genetic, and pathological information. It includes 398 CT volumes.
*   **HCC-TACE-Seg:** This dataset contains pre- and post-procedure CT imaging studies of 105 confirmed Hepatocellular Carcinoma (HCC) patients who underwent Transarterial Chemoembolization (TACE). It includes semi-automatic segmentations of the liver, tumor, and blood vessels.
*   **COLORECTAL-LIVER-METASTASES:** This collection offers DICOM images and DICOM Segmentation Objects (DSOs) for 197 patients with Colorectal Liver Metastases (CRLM), including preoperative CT scans and corresponding clinical data.
*   **B-MODE-AND-CEUS-LIVER:** This dataset comprises contrast-enhanced ultrasound data for characterizing liver lesions and monitoring treatment response. It is expected to be expanded with volumetric data and cine loops.

### The Cancer Genome Atlas (TCGA)

TCGA, in conjunction with TCIA and the Genomic Data Commons (GDC), provides integrated datasets linking imaging with genomic and clinical information.

*   **TCGA Kidney Cancers:** This is a bulk RNA-seq dataset with transcriptome profiles for patients diagnosed with three different subtypes of kidney cancers, containing 1024 instances and 60660 features.
*   **Liver Hepatocellular Carcinoma (TCGA, PanCancer Atlas):** This dataset includes summary data visualizations and clinical data from 372 liver hepatocellular carcinomas, with clinical data encompassing mutation counts, mutated genes, demographics, disease status, and more.

### University of California San Francisco (UCSF) Datasets

UCSF offers several valuable datasets for medical imaging research.

*   **UCSF Renal Mass Dataset:** This dataset includes 831 3D Multiphase CT exams of renal masses with annotations and pathology results, aiming to differentiate aggressive from indolent disease.

### Other Notable Datasets

*   **The Liver Tumor Segmentation Benchmark (LiTS):** This dataset, created in collaboration with seven hospitals, contains 131 CT volumes for training and 70 unseen test images for liver and liver tumor segmentation. It has been used as an active benchmark.
*   **Duke Liver Dataset (DLDS):** This dataset includes 2146 abdominal MRI series from 105 patients with liver cirrhosis, with segmentation masks for the liver in 310 series. It is suitable for training segmentation and classification models.
*   **LiverHccSeg:** This dataset provides multiphasic MRI scans with liver and HCC tumor segmentations from two radiologists, including an analysis of inter-rater agreement.
*   **United States Renal Data System (USRDS):** While not primarily imaging-focused, USRDS is a comprehensive source for data on chronic kidney disease (CKD) and end-stage renal disease (ESRD) in the US, with various reports and analysis files available.
*   **Chronic Kidney Disease in Children Cohort Study (CKiD):** This cohort study provides data on children with mild to moderately impaired kidney function, including kidney history, clinical endpoints, and associated risk factors.
*   **MMIST ccRCC Dataset:** This dataset for clear cell renal cell carcinoma (ccRCC) was curated from CPTAC-CCRCC and TCGA-KIRC, aiming to improve prognosis estimation.
*   **Primary Liver Cancer CECT Imaging Dataset:** This dataset contains 278 liver cancer cases (HCC, ICC, cHCC-CCA) and 83 non-liver cancer subjects, with complete CT phasing (Plain, Arterial, Venous, Delayed) and annotated liver and lesion regions.
*   **LIDC-IDRI (Lung Image Database Consortium):** Although focused on lung nodules, this dataset is a significant resource for medical imaging with detailed annotations from four radiologists and is available under a CC BY 4.0 license.

## Notable Papers

*   **Heller et al. (arXiv:1904.00445):** Describes the data collection and annotation process for the KiTS19 dataset, which is now part of TCIA's C4KC-KiTS collection.
*   **Akin et al. (doi:10.7937/K9/TCIA.2016.V6PBVTDR):** The citation for the TCGA-KIRC dataset available on TCIA.
*   **Mota et al. (CVPR 2024):** Introduces the MMIST-ccRCC dataset for multi-modal systems development in medical imaging.
*   **Gross et al. (Zenodo):** Describes the LiverHccSeg dataset, a publicly available multiphasic MRI dataset with liver and HCC tumor segmentations.
*   **Sarfati et al. (MICCAI 2023):** Presents the TCIA/TGCA-LIHC portal venous phase CT-scans for cirrhosis classification.
*   **Khademi et al. (March 2025):** Introduces AutoRad-Lung, a radiomic-guided vision-language model for lung nodule malignancy prediction using the LIDC-IDRI dataset.
*   **Maksoud et al. (CVPR 2020):** Introduces the Liver Kidney Stomach (LKS) dataset for immunofluorescence whole slide image classification.

## What to Watch

*   **TCIA Updates:** TCIA is continuously updated with new cancer imaging datasets. Researchers should monitor their collections for new releases relevant to liver and kidney research.
*   **USRDS Announcements:** The United States Renal Data System provides regular updates on ESRD and CKD data, including quarterly updates and annual reports. Their website lists upcoming data availability and report releases.
*   **Ongoing Clinical Trials:** Many imaging datasets originate from ongoing clinical trials. Following publications from institutions like UCSF or those involved in TCGA research can highlight new data becoming available.
*   **LiverHccSeg Version 1.1:** A newer version of the LiverHccSeg dataset is available on Zenodo, suggesting ongoing refinement and potential for improved data.

## Possible Clinical Relevance

The datasets described offer significant potential for advancing clinical practice in liver and kidney disease management.

*   **Improved Diagnosis and Classification:** Datasets with detailed annotations and multiple imaging phases (e.g., TCIA-KIRC, Primary Liver Cancer CECT Imaging Dataset) can train AI models for more accurate and earlier diagnosis of cancers and other pathologies.
*   **Enhanced Treatment Planning:** The availability of precise segmentation masks for organs and tumors (e.g., C4KC-KiTS, LiTS, LiverHccSeg, ATLAS) is critical for pre-operative planning, particularly for surgeries like partial nephrectomies or resections of liver metastases.
*   **Precision Medicine:** Datasets integrating imaging with genomic and clinical data (e.g., TCGA collections) are invaluable for developing personalized treatment strategies, predicting treatment response, and identifying novel biomarkers.
*   **Prognosis Prediction:** Datasets like MMIST ccRCC can help develop models to estimate prognosis for kidney cancer patients, aiding in clinical decision-making.
*   **Understanding Disease Progression:** Longitudinal datasets (e.g., CKiD, USRDS) are crucial for understanding disease progression in conditions like chronic kidney disease, identifying risk factors, and evaluating interventions.
*   **Radiomics and Quantitative Imaging:** Datasets with detailed imaging information and associated outcomes (e.g., COLORECTAL-LIVER-METASTASES, HCC-TACE-Seg) enable the development of radiomic models for predicting treatment response and survival.

## Sources

*   C4KC-KITS - The Cancer Imaging Archive (TCIA). Retrieved from <a href="https://www.cancerimagingarchive.net/collection/c4kc-kits/" target="_blank">https://www.cancerimagingarchive.net/collection/c4kc-kits/</a>
*   2025 Guide to Medical Imaging Dataset Resources - Collective Minds. Retrieved from 
*   Real-World Imaging Datasets to Enhance Precision Medicine. Retrieved from 
*   UCSF Datasets for Medical Imaging. Retrieved from 
*   Liver Cancer Multiclass Dataset - Kaggle. Retrieved from 
*   Liver - Datasets - PLCO - The Cancer Data Access System. Retrieved from <a href="https://cdas.cancer.gov/plco/datasets/" target="_blank">https://cdas.cancer.gov/plco/datasets/</a>
*   Renal - Datasets - PLCO - The Cancer Data Access System. Retrieved from <a href="https://cdas.cancer.gov/plco/datasets/" target="_blank">https://cdas.cancer.gov/plco/datasets/</a>
*   TCGA Kidney Cancers - UCI Machine Learning Repository. Retrieved from <a href="https://archive.ics.uci.edu/dataset/505/tcga-kidney-cancers" target="_blank">https://archive.ics.uci.edu/dataset/505/tcga-kidney-cancers</a>
*   CancerLivER: a database of liver cancer gene expression resources and biomarkers - PMC. Retrieved from <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7061417/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7061417/</a>
*   Liver Hepatocellular Carcinoma (TCGA, PanCancer Atlas) - MSK Data Catalog. Retrieved from 
*   United States Renal Data System - USRDS - NIDDK. Retrieved from 
*   Liver cancer Datasets - BioGPS. Retrieved from 
*   TCGA-LIHC | The Cancer Genome Atlas Liver Hepatocellular Carcinoma Collection. Retrieved from <a href="https://www.cancerimagingarchive.net/collection/tcga-lihc/" target="_blank">https://www.cancerimagingarchive.net/collection/tcga-lihc/</a>
*   MMIST ccRCC Dataset. Retrieved from 
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC. Retrieved from <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9064857/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9064857/</a>
*   TCGA-KIRC | The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma Collection. Retrieved from <a href="https://www.cancerimagingarchive.net/collection/tcga-kirc/" target="_blank">https://www.cancerimagingarchive.net/collection/tcga-kirc/</a>
*   Shared Datasets | Center for Artificial Intelligence in Medicine & Imaging. Retrieved from 
*   The Chronic Kidney Disease in Children Cohort Study (CKiD) - NIDDK Central Repository. Retrieved from <a href="https://repository.niddk.nih.gov/studies/ckid/" target="_blank">https://repository.niddk.nih.gov/studies/ckid/</a>
*   Top 10 Free Healthcare Datasets for Computer Vision - Encord. Retrieved from 
*   Deep learning for end-to-end kidney cancer diagnosis on multi-phase abdominal computed tomography - PMC. Retrieved from <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8194019/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8194019/</a>
*   B-MODE-AND-CEUS-LIVER - The Cancer Imaging Archive (TCIA). Retrieved from <a href="https://www.cancerimagingarchive.net/collection/b-mode-and-ceus-liver/" target="_blank">https://www.cancerimagingarchive.net/collection/b-mode-and-ceus-liver/</a>
*   TCIA/TGCA-LIHC portal venous phase CT-scans for cirrhosis classification - Zenodo. Retrieved from 
*   HCC-TACE-SEG - The Cancer Imaging Archive (TCIA). Retrieved from <a href="https://www.cancerimagingarchive.net/collection/hcc-tace-seg/" target="_blank">https://www.cancerimagingarchive.net/collection/hcc-tace-seg/</a>
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC. Retrieved from <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10338228/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10338228/</a>
*   Primary Liver Cancer CECT Imaging Dataset. Retrieved from <a href="https://github.com/ljwa2323/PLC_CECT" target="_blank">https://github.com/ljwa2323/PLC_CECT</a>
*   TCGA-KIRP (Kidney Renal Clear Cell Carcinoma) - Kaggle. Retrieved from 
*   Kidney | HuBMAP Organ & Tissue Data. Retrieved from 
*   LIDC-IDRI - The Cancer Imaging Archive (TCIA). Retrieved from <a href="https://www.cancerimagingarchive.net/collection/lidc-idri/" target="_blank">https://www.cancerimagingarchive.net/collection/lidc-idri/</a>
*   Classification results on LIDC-IDRI dataset. - ResearchGate. Retrieved from 
*   LIDC-IDRI - Kaggle. Retrieved from 
*   The Liver Kidney Stomach Dataset - COVE - Computer Vision Exchange. Retrieved from 
*   Standardized representation of the TCIA LIDC-IDRI annotations using DICOM (DICOM-LIDC-IDRI-Nodules) - Cancer Imaging Archive Wiki. Retrieved from 
*   Liver Disease Patient Dataset 30K train data - Kaggle. Retrieved from 
*   A DEEP LEARNING-BASED HEPATOCELLULAR CARCINOMA STAGING SYSTEM BY MULTI-PHASE COMPUTED TOMOGRAPHY | AASLD. Retrieved from 
*   [1901.04056] The Liver Tumor Segmentation Benchmark (LiTS) - arXiv. Retrieved from <a href="https://arxiv.org/abs/1901.04056" target="_blank">https://arxiv.org/abs/1901.04056</a>
*   COLORECTAL-LIVER-METASTASES - The Cancer Imaging Archive (TCIA). Retrieved from <a href="https://www.cancerimagingarchive.net/collection/colorectal-liver-metastases/" target="_blank">https://www.cancerimagingarchive.net/collection/colorectal-liver-metastases/</a>
*   LiverHccSeg: A Publicly Available Multiphasic MRI Dataset with Liver and HCC Tumor Segmentations and Inter-Rater Agreement Analysis - Zenodo. Retrieved from <a href="https://zenodo.org/records/7040325" target="_blank">https://zenodo.org/records/7040325</a>
*   ILPD (Indian Liver Patient Dataset) - UCI Machine Learning Repository. Retrieved from <a href="https://archive.ics.uci.edu/dataset/373/ilpd-indian-liver-patient-dataset" target="_blank">https://archive.ics.uci.edu/dataset/373/ilpd-indian-liver-patient-dataset</a>
*   TCGA-KIRC (Kidney Renal Clear Cell Carcinoma) - Hugging Face. Retrieved from 
*   NIDDK Data or Sample Repositories - dkNET. Retrieved from 