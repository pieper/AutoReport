# Research Report: Liver-Kidney-Data
*Generated: 2026-09-28 UTC*

## Liver and Kidney Datasets Report

### Executive Summary

This report outlines key publicly available datasets for liver and kidney imaging, focusing on those with well-described diseases like cancers, non-restrictive licenses, and comprehensive annotations. Recent advancements include the introduction of multi-task datasets and more extensive annotation efforts. The identified datasets provide a strong foundation for AI research in medical imaging, enabling advancements in segmentation, detection, and classification tasks for these critical organs.

### Key Announcements and Datasets

**Kidney Datasets:**

*   **KiTS (Kidney Tumor Segmentation Challenge) Datasets:**
    *   **KiTS19:** A foundational dataset for kidney and kidney tumor segmentation, comprising 300 patients with CT scans and manual semantic segmentations. The training set of 210 patients is publicly available, with annotations including kidneys and tumors.
    *   **KiTS23-2D:** Derived from KiTS23, this dataset consists of 95,221 2D axial slices for kidney, tumor, and cyst segmentation from contrast-enhanced CT scans. It is particularly useful for 2D segmentation architectures.
    *   **RCC-AID (Renal Cell Carcinoma AI Dataset):** This dataset provides voxel-level segmentation annotations for CT imaging from three TCGA renal cell carcinoma cohorts (clear cell, papillary, and chromophobe). It includes 129 annotated CT scans from 91 patients and is licensed under CC BY 4.0 for annotations.

*   **Hyper and Multispectral Kidney Image Dataset:** This Kaggle dataset contains 20,000 hyperspectral and multispectral kidney images for classifying normal versus tumor tissue, divided into four categories. It is licensed under CC0 (Public Domain).

*   **Open Kidney Dataset:** Focused on ultrasound imaging, this dataset offers over 500 2D B-mode ultrasound images with fine-grained polygon annotations for kidney segmentation, intended for non-commercial use.

**Liver Datasets:**

*   **LiTS (Liver Tumor Segmentation Benchmark):**
    *   A widely used dataset for liver and tumor segmentation research, comprising 201 abdominal CT scans with primary and metastatic liver cancers. The training set has 131 cases with annotations, and 70 test cases have undisclosed labels.
    *   **LiTS Dataset (from PMC):** A specific mention of the LiTS dataset used in a study, detailing its composition of 131 CT scans for training and 70 for testing, with slices ranging from 42 to 1026 and varying resolutions.

*   **LiMT (Multi-task Liver Dataset):** This newly constructed dataset supports liver and tumor segmentation, multi-label lesion classification, and lesion detection using arterial phase-enhanced CT. It includes CT volumes from 150 cases with diverse liver diseases and normal cases, annotated by clinicians.

*   **ATLAS (Tumour and Liver Automatic Segmentation) Dataset:** This is a novel dataset providing systematic annotations of liver and liver tumors on contrast-enhanced MRI (CE-MRI) scans for 90 patients with unresectable HCC. It is noted as the first public dataset of its kind for CE-MRI of HCC.

*   **Duke Liver Dataset (MRI):** This dataset contains 2146 abdominal MRI series from 105 patients, with 310 image series including manually segmented liver masks. It is well-suited for training segmentation and series classification models for abdominal MRI.

*   **Primary Liver Cancer CECT Imaging Dataset:** This dataset includes 278 cases of liver cancer (HCC, ICC, cHCC-CCA) and 83 non-liver cancer subjects, with complete 3D contrast-enhanced CT data across Plain, Arterial, Venous, and Delayed phases. Annotations for liver and lesion regions are provided.

**Combined/Multi-Organ Datasets:**

*   **Blood–Liver–Kidney Tri-Organ Imaging Dataset:** A multi-modal dataset for object detection and tissue classification, including separate datasets for blood cell detection, liver tissue analysis, and kidney tissue analysis.

### Notable Papers

*   **"RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research"**: This paper introduces the RCC-AID dataset, which provides voxel-level segmentation annotations for CT imaging of renal cell carcinoma, aiming to foster accessible and reproducible AI research.
*   **"LiMT: a multi-task liver image benchmark dataset"**: This paper presents the LiMT dataset, designed for multi-task learning (segmentation, detection, and classification) of liver lesions from CT scans, addressing limitations of single-task datasets.
*   **"A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma"**: Introduces the ATLAS dataset, the first public dataset of CE-MRI for HCC with annotations for liver and liver tumors, crucial for automated treatment planning.
*   **"The state of the art in kidney and kidney tumor segmentation in contrast-enhanced CT imaging: Results of the KiTS19 challenge"**: Details the KiTS19 challenge and dataset, highlighting the progress in automatic 3D semantic segmentation of kidneys and kidney tumors.
*   **"Liver Tumor Segmentation with Deep Learning: A Comparative Analysis of CNN-, Transformer-, and YOLO-Based Models on the ATLAS MRI"**: Compares different deep learning architectures for liver and tumor segmentation on the ATLAS MRI dataset, finding volumetric CNNs to be superior.

### What to Watch

*   **Continued Expansion of Multi-Task Datasets:** Datasets like LiMT are emerging, which combine segmentation, detection, and classification tasks. This trend is likely to continue, offering more comprehensive resources for complex AI model development.
*   **Advancements in Annotation Quality and Quantity:** As seen with RCC-AID and ATLAS, there's a push towards more detailed and accurate annotations, including voxel-level segmentations and multi-rater agreement analysis, which are vital for robust model training.
*   **Broader Modality Inclusion:** While CT and MRI dominate, datasets like the Open Kidney Dataset highlight the growing importance of ultrasound data for kidney imaging research.

### Possible Clinical Relevance

The availability of these diverse and well-annotated datasets is crucial for developing and validating AI-powered tools that can significantly impact clinical practice:

*   **Early Cancer Detection and Diagnosis:** Improved segmentation and detection algorithms can lead to earlier and more accurate identification of liver and kidney tumors, potentially improving patient prognosis and treatment selection.
*   **Treatment Planning and Monitoring:** Precise segmentation of organs and tumors is essential for precise treatment planning (e.g., surgery, radiotherapy) and for monitoring treatment response over time.
*   **Quantitative Imaging Biomarkers:** Datasets with rich clinical metadata, such as KiTS19, can facilitate the discovery of imaging biomarkers that correlate with disease progression or treatment outcomes.
*   **Reducing Radiologist Workload:** Automated segmentation and analysis tools can help alleviate the burden on radiologists, allowing them to focus on more complex cases and diagnostic interpretation.

### Sources

*   KiTS23-2D Kidney Tumor Segmentation - Kaggle. (n.d.). Retrieved from 
*   The Cancer Imaging Archive: LIDC-IDRI - Kaggle. (n.d.). Retrieved from 
*   Liver Tumor Segmentation - Kaggle. (n.d.). Retrieved from 
*   LiMT: a multi-task liver image benchmark dataset. (2025, November 25). arXiv. Retrieved from https://arxiv.org/abs/2301.07430
*   A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma. (2023, April 27). MDPI. Retrieved from 
*   Challenge Data - KiTS19. (n.d.). Retrieved from 
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels. (n.d.). PubMed Central. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9065543/
*   Data from the training set of the 2019 Kidney and Kidney Tumor Segmentation Challenge (C4KC-KiTS) - Cancer Imaging Archive. (n.d.). Retrieved from 
*   The state of the art in kidney and kidney tumor segmentation in contrast-enhanced CT imaging: Results of the KiTS19 challenge. (n.d.). PubMed Central. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6943474/
*   Hyper and Multispectral Kidney Image dataset. (n.d.). Kaggle. Retrieved from 
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset. (n.d.). Kaggle. Retrieved from 
*   RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research. (2026, April 22). Zenodo. Retrieved from https://zenodo.org/records/20719257
*   Primary Liver Cancer CECT Imaging Dataset. (2025, May 15). Kaggle. Retrieved from 
*   The Liver Tumor Segmentation Benchmark (LiTS). (n.d.). Retrieved from https://competitions.codalab.org/competitions/17094
*   The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A Completed Reference Database of Lung Nodules on CT Scans. (2011, January 28). NIST. Retrieved from 
*   Lung Nodule Segmentation (LIDC-IDRI). (2025, September 15). Medium. Retrieved from 
*   Deep Learning-Based Liver Tumor Segmentation from Computed Tomography Scans with a Gradient-Enhanced Network. (2026, February 1). PubMed Central. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10921143/
*   3D Kidneys and Kidney Tumor Semantic Segmentation using Boundary-Aware Networks. (2019, September 14). arXiv. Retrieved from https://arxiv.org/abs/1909.06642
*   Liver Tumor Segmentation with Deep Learning: A Comparative Analysis of CNN-, Transformer-, and YOLO-Based Models on the ATLAS MRI. (n.d.). PubMed Central. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10865394/
*   The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A Completed Reference Database of Lung Nodules on CT Scans. (n.d.). PubMed Central. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3074157/
*   Enhanced Pulmonary Nodule Detection and Classification Using Artificial Intelligence on LIDC-IDRI Data. (2026, January 15). Xia & He Publishing Inc. Retrieved from 
*   The KiTS19 Challenge Data: 300 Kidney Tumor Cases with Clinical Context, CT Semantic Segmentations, and Surgical Outcomes. (2019, March 31). arXiv. Retrieved from https://arxiv.org/abs/1904.00445
*   RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research. (2026, August 5). medRxiv. Retrieved from https://www.medrxiv.org/content/10.1101/2026.08.05.26144902v1
*   Liver Cancer Multiclass Dataset. (n.d.). Kaggle. Retrieved from 
*   RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research. (2026, September 24). ResearchGate. Retrieved from 
*   Primary Liver Cancer CECT Imaging Dataset. (2024, August 22). Kaggle. Retrieved from -aug-2024
*   Open Kidney Dataset. (2022, June 14). GitHub. Retrieved from 
*   LiTS – Liver Tumor Segmentation Challenge (LiTS17). (2017, June 29). CodaLab. Retrieved from https://competitions.codalab.org/competitions/17094
*   MMIST ccRCC Dataset. (n.d.). Retrieved from 
*   LiTS – Liver Tumor Segmentation Challenge (LiTS17) - Academic Torrents. (n.d.). Retrieved from https://academictorrents.com/details/27772adef6f563a1ecc0ae19a528b956e6c803ce
*   Best Medical Image Segmentation Datasets for Training Clinical AI Models. (2026, August 3). DataVLab. Retrieved from 
*   Duke Liver Dataset (MRI). (2022, March 4). Zenodo. Retrieved from https://zenodo.org/records/6328447
*   Medical Imaging Datasets - Intelligent Clinical Care Center (IC3) » » University of Florida. (n.d.). Retrieved from 
*   Automatic Segmentation of Kidneys and Kidney Tumors: The KiTS19 International Challenge. (n.d.). Frontiers. Retrieved from https://www.frontiersin.org/articles/10.3389/fmed.2020.00056/full
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis. (n.d.). PubMed Central. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10534689/
*   Kidney Tumor Segmentation Challenge(KITS 19) - Kaggle. (n.d.). Retrieved from 
*   Artificial Intelligence in Renal Imaging: A Multi-Dataset Study for Kidney Disease Classification. (2026, May 14). MDPI. Retrieved from 
*   Public Medical Image Datasets for Segmentation Foundation Models. (n.d.). Retrieved from 
*   KiTS-19 Kidney Tumor Segmentation Dataset - Kaggle. (n.d.). Retrieved from 
*   A preclinical CT and MRI Liver Imaging Dataset with Anatomical, Functional and Segmentation Data. (2026, March 23). Read by QxMD. Retrieved from 