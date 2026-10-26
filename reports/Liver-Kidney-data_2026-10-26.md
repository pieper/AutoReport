# Research Report: Liver-Kidney-Data
*Generated: 2026-10-26 UTC*

"The LIDC-IDRI dataset, while focused on lung nodules, is a foundational dataset in medical imaging due to its rigorous two-phase annotation process by four radiologists, ensuring high-quality lesion identification and characterization. It contains 1,018 cases with associated XML files detailing lesion annotations.

**2. Liver Tumor Segmentation Benchmark (LiTS)**
*   **Description:** This benchmark dataset focuses on liver and liver tumors from contrast-enhanced CT scans. It was organized in conjunction with ISBI 2017 and MICCAI 2017/2018, featuring diverse cases from seven institutions.
*   **Patient/Scan Count:** Trained on 131 CT volumes and tested on 70 unseen cases. Some sources mention 201 CT volumes in total. The CT-ORG dataset also incorporates images from LiTS.
*   **Annotations:** Includes annotations for the liver and lesions.
*   **Clinical Data:** Not explicitly detailed in the search results.
*   **License:** CC BY-NC-SA 4.0.

**3. Kidney and Kidney Tumor Segmentation Challenge (KiTS19)**
*   **Description:** This dataset was created for a segmentation challenge and contains CT scans with kidney and kidney tumor segmentations. It was released in 2019 and includes clinical context and surgical outcomes for patients who underwent nephrectomy.
*   **Patient/Scan Count:** Consists of 300 kidney tumor cases, with 210 CT scans with segmentation masks for training and 90 without for testing.
*   **Annotations:** High-quality kidney and kidney tumor segmentations.
*   **Clinical Data:** Includes clinical context and surgical outcomes.
*   **License:** CC-BY-NC-SA-4.0.

**4. RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research**
*   **Description:** A newer dataset providing voxel-level segmentation annotations for CT imaging from three TCGA renal cell carcinoma (RCC) cohorts: clear cell (TCGA-KIRC), papillary (TCGA-KIRP), and chromophobe (TCGA-KICH). It aims to support accessible and reproducible AI research.
*   **Patient/Scan Count:** 129 annotated CT scans from 91 patients.
*   **Annotations:** Voxel-level annotations for kidneys, primary solid tumors, and cysts.
*   **Clinical Data:** Includes patient demographics, RCC subtype, and TCIA series identifiers.
*   **License:** Segmentation annotations: CC BY 4.0. NIfTI images and metadata.csv are derived from TCIA source collections, published under CC BY 3.0.

**5. Primary Liver Cancer CECT Imaging Dataset (PLC-CECT)**
*   **Description:** A comprehensive collection of 3D contrast-enhanced CT (CECT) images for primary liver cancer, including HCC, ICC, and cHCC-CCA. It features complete four-phase imaging and expert lesion annotations.
*   **Patient/Scan Count:** 278 patients with primary liver cancer and 83 non-liver cancer control cases.
*   **Annotations:** Over 50,000 manually annotated lesion sections, with a median interobserver Dice coefficient of 0.76.
*   **Clinical Data:** Not explicitly detailed in the search results.
*   **License:** Publicly available on Physionet.

**6. UCSF Renal Mass CT Dataset (RMaC)**
*   **Description:** This dataset contains 831 3D multiphase CT exams of renal masses, with annotations in the form of bounding boxes or polygon masks, and associated pathology results. It's designed to help distinguish aggressive from indolent disease.
*   **Patient/Scan Count:** 831 exams.
*   **Annotations:** Renal mass annotations (bounding boxes or polygon masks) and pathology results.
*   **Clinical Data:** Pathology results serve as ground-truth outcomes.
*   **License:** Not explicitly stated in search results, but generally available for research.

**7. CT-ORG (CT volumes with multiple organ segmentations)**
*   **Description:** This dataset includes 140 CT scans with manual segmentations for five organs: lung, bones, liver, kidneys, and bladder. It's ideal for training organ segmentation algorithms.
*   **Patient/Scan Count:** 140 CT scans.
*   **Annotations:** 3D manual segmentations of organs.
*   **Clinical Data:** Patients were included based on the presence of lesions in labeled organs; many images exhibit liver lesions.
*   **License:** Not explicitly stated as CC-BY in the search results, but generally considered open for research.

### Notable Papers

*   **"The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A Completed Reference Database of Lung Nodules on CT Scans"**: This paper details the creation and characteristics of the LIDC-IDRI dataset, highlighting its value for computer-aided diagnosis research.
*   **"The Liver Tumor Segmentation Benchmark (LiTS)"**: This publication describes the setup and results of the LiTS benchmark, emphasizing the dataset's diversity and its use in evaluating segmentation algorithms.
*   **"The KiTS19 Challenge Data: 300 Kidney Tumor Cases with Clinical Context, CT Semantic Segmentations, and Surgical Outcomes"**: This paper introduces the KiTS19 dataset, detailing its content and its role in advancing kidney tumor segmentation.
*   **"RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research"**: This preprint introduces the RCC-AID dataset, focusing on its contribution to reproducible AI research in renal cell carcinoma with voxel-level annotations.
*   **"Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics"**: This article describes the PLC-CECT dataset, emphasizing its multiphase imaging and expert annotations for liver cancer AI diagnostics.
*   **"UCSF RMaC: UCSF Renal Mass CT Dataset"**: This resource page details the UCSF Renal Mass CT Dataset, highlighting its annotations and pathology results for renal masses.

### What to Watch For

*   **Human Cell Atlas (HCA):** The HCA is making significant progress in releasing comprehensive atlases, including planned Liver, Gut, and Kidney atlases, available through the AWS Open Data Program. While this is single-cell data, it represents a major expansion of publicly available biological data.
*   **LiMT (Multi-task Liver Image Benchmark Dataset):** This dataset is under development with plans to expand its scope to include finer CT slices and multi-phase scan data, as well as integrating multi-center data and a wider range of liver diseases.
*   **Continued growth in specialized datasets:** Expect to see more datasets like RCC-AID that provide detailed, voxel-level annotations for specific cancer types, addressing the need for highly curated data for advanced AI model development.

### Possible Clinical Relevance

The datasets described are crucial for developing and validating AI-driven tools that can aid in the early detection, diagnosis, segmentation, and treatment planning of liver and kidney cancers.

*   **Early Detection and Diagnosis:** Improved AI models trained on these datasets can help radiologists identify subtle lesions that might be missed by the human eye, leading to earlier diagnoses and better patient outcomes.
*   **Treatment Planning and Monitoring:** Accurate segmentation of tumors and organs is essential for precise treatment planning, such as in radiation therapy or surgical intervention. These datasets enable the development of automated segmentation tools that can save time and improve accuracy.
*   **Disease Subtyping and Prognosis:** Datasets with detailed clinical and pathological information, like KiTS19 and RCC-AID, are vital for developing models that can predict disease aggressiveness and patient prognosis, guiding treatment decisions.
*   **Drug Development and Research:** These datasets serve as a foundation for research into new diagnostic markers and therapeutic strategies for liver and kidney diseases.

### Sources

The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A Completed Reference Database of Lung Nodules on CT Scans - NIST: https://www.cancerimagingarchive.net/lidc-idri/
The Cancer Imaging Archive: LIDC-IDRI - Kaggle: 
The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A Completed Reference Database of Lung Nodules on CT Scans - PMC - NIH: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2704242/
The Liver Tumor Segmentation Benchmark (LiTS): 
FLamby/flamby/datasets/fed_kits19/README.md at main - GitHub: 
0004_lits/README_0004_lits.md · huggingface/CADS-dataset at main: 
Lung Nodule Segmentation (LIDC-IDRI) — Preparing Data for Inference | by Hannah Do: 
The state of the art in kidney and kidney tumor segmentation in contrast-enhanced CT imaging: Results of the KiTS19 challenge - PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6986769/
Enhanced Pulmonary Nodule Detection and Classification Using Artificial Intelligence on LIDC-IDRI Data - Xia & He Publishing Inc.: 
[1904.00445] The KiTS19 Challenge Data: 300 Kidney Tumor Cases with Clinical Context, CT Semantic Segmentations, and Surgical Outcomes - arXiv: https://arxiv.org/abs/1904.00445
Challenge Data - KiTS19: 
C4KC-KITS - The Cancer Imaging Archive (TCIA): https://www.cancerimagingarchive.net/c4kc-kits/
RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research | medRxiv: 
Primary Liver Cancer CECT Imaging Dataset: 
RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research - Zenodo: https://zenodo.org/record/8128462
The Liver Tumor Segmentation Benchmark (LiTS) - PubMed - NIH: 
The Liver Tumor Segmentation Benchmark (LiTS) - FAU CRIS: 
CT-ORG - The Cancer Imaging Archive (TCIA): https://www.cancerimagingarchive.net/ct-org/
Medical Imaging Datasets — PYCAD: https://pycad.github.io/
Publicly available medical imaging datasets for research and analysis. · GitHub: 