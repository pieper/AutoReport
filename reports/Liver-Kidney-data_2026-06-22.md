# Research Report: Liver-Kidney-Data
*Generated: 2026-06-22 UTC*

## Executive Summary

This report outlines freely available datasets for liver and kidney imaging, focusing on those with annotations, clinical data, and non-restrictive licenses suitable for research. The **Liver Tumor Segmentation Benchmark (LiTS)** and the **Kidney and Kidney Tumor Segmentation Challenge (KiTS19)** datasets are prominent for their extensive annotations and relevance to cancer research. Emerging efforts like the **Medical Imaging and Data Resource Center (MIDRC)** aim to consolidate and expand access to diverse medical imaging data, including for chronic diseases like liver conditions. While most datasets are CT-based, some MRI and ultrasound datasets are also available, offering multi-modal research opportunities.

## Key Announcements and Datasets

### Kidney Datasets

*   **KiTS19 (Kidney and Kidney Tumor Segmentation Challenge):**
    *   **Description:** This dataset includes CT scans and corresponding semantic segmentations of kidneys and kidney tumors for 300 patients who underwent nephrectomy. It also provides comprehensive clinical outcomes.
    *   **Patient/Scan Count:** 300 patients with CT scans.
    *   **Annotations:** Manual semantic segmentations of kidneys and tumors are available.
    *   **Clinical Data:** Comprehensive clinical outcomes and demographic data are included.
    *   **License:** CC BY-NC-SA (non-commercial use, share-alike).
    *   **Associated Papers:** "The KiTS19 Challenge Data: 300 Kidney Tumor Cases with Clinical Context, CT Semantic Segmentations, and Surgical Outcomes"

*   **CT-ORG (The Cancer Imaging Archive):**
    *   **Description:** This dataset contains 140 CT scans with 3D segmentations of multiple organs, including liver and kidneys. It features patients with lesions in these organs, including benign and malignant liver lesions.
    *   **Patient/Scan Count:** 140 CT scans.
    *   **Annotations:** 3D organ segmentations for lung, bones, liver, kidneys, and bladder.
    *   **License:** Publicly available for download via TCIA.
    *   **Associated Papers:** Accessible via The Cancer Imaging Archive (TCIA).

*   **Open Kidney Dataset:**
    *   **Description:** This dataset comprises over 500 two-dimensional B-mode abdominal ultrasound images with fine-grained polygon annotations for four classes. It is intended for non-commercial use.
    *   **Patient/Scan Count:** Over 500 ultrasound images.
    *   **Annotations:** Fine-grained polygon annotations for kidney structures.
    *   **License:** CC BY-NC-SA (non-commercial use, share-alike).
    *   **New Since Last Review:** This dataset is relatively new and focuses on ultrasound imaging, which is less common in large public repositories.

### Liver Datasets

*   **LiTS (Liver Tumor Segmentation Benchmark):**
    *   **Description:** This benchmark dataset provides CT scans and segmentation masks for liver and liver tumors. It includes primary and secondary tumors of various sizes and appearances.
    *   **Patient/Scan Count:** 201 abdominal CT scans (131 training, 70 test).
    *   **Annotations:** Pixel-wise segmentation masks for liver and tumors.
    *   **License:** The Kaggle version of LiTS is CC BY NC ND 4.0. The original challenge data details are available through MICCAI and ISBI.
    *   **Associated Papers:** LiTS dataset has been used in numerous studies, including publications associated with MICCAI and ISBI challenges.

*   **TCGA-LIHC (The Cancer Genome Atlas Liver Hepatocellular Carcinoma):**
    *   **Description:** This collection includes clinical images matched with genomic and pathological data for liver hepatocellular carcinoma from The Cancer Genome Atlas (TCGA).
    *   **Patient/Scan Count:** Large numbers of specimens per cancer type, with specific details on image counts available via TCIA.
    *   **Annotations:** Radiological data stored on TCIA, with matched clinical and genomic data in the GDC Data Portal.
    *   **License:** Data is generally accessible for research purposes via TCIA and GDC.
    *   **Associated Papers:** Linked to TCGA research efforts.

*   **LiverHccSeg:**
    *   **Description:** A curated dataset of multiphasic MRI scans for liver and HCC tumor segmentation, with manual segmentations by two radiologists.
    *   **Patient/Scan Count:** 17 patients for whole liver segmentation, 14 for tumor segmentation.
    *   **Annotations:** Manual segmentations by two radiologists.
    *   **Clinical Data:** Relevant metadata and patient characteristics are included.
    *   **License:** Data is publicly available for research.
    *   **Associated Papers:** Described in "LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis."

*   **CARE-Liver:**
    *   **Description:** A dataset of 610 patients with liver fibrosis, including multi-phase MRI scans (T2-weighted, diffusion-weighted, and Gd-EOB-DTPA-enhanced dynamic MRIs).
    *   **Patient/Scan Count:** 610 patients.
    *   **Annotations:** Data is prepared for liver fibrosis staging tasks.
    *   **License:** Data access details should be verified on the respective platform (e.g., challenge website).
    *   **Associated Papers:** Related to the CARE challenges.

### Multi-Organ / General Datasets

*   **MIDRC (Medical Imaging and Data Resource Center):**
    *   **Description:** MIDRC aims to curate a comprehensive repository of medical imaging data for research, including data for chronic diseases like chronic liver disease. It acts as a federated data search and discovery platform.
    *   **Patient/Scan Count:** Large and growing repository with millions of imaging studies.
    *   **Annotations:** Varies by dataset, but MIDRC supports annotation and labeling.
    *   **License:** Open access for registered users under a data use agreement.
    *   **New Since Last Review:** MIDRC is an ongoing initiative aiming to expand its scope and features, including a federated data search platform.

*   **The Cancer Imaging Archive (TCIA):**
    *   **Description:** TCIA hosts a large archive of de-identified medical images of cancer, organized into collections. It is a primary source for many imaging datasets, including liver and kidney-related ones.
    *   **Patient/Scan Count:** Varies greatly by collection, with many datasets containing hundreds or thousands of scans.
    *   **Annotations:** Varies by dataset; some collections have extensive annotations (e.g., CT-ORG).
    *   **License:** Generally public download for research.
    *   **Associated Papers:** Datasets are typically linked to publications.

*   **AbdomenAtlas:**
    *   **Description:** A collection of abdominal CT datasets, including "AbdomenAtlas Full" and "AbdomenAtlas 1.1," which contain segmentations for multiple abdominal structures like the liver and kidneys.
    *   **Patient/Scan Count:** AbdomenAtlas Full has 20,460 CT scans; AbdomenAtlas 1.1 has 8,448 CT scans.
    *   **Annotations:** 25 abdominal structures are segmented.
    *   **License:** CC BY-NC-SA (non-commercial use, share-alike).

## Notable Papers

*   **"The KiTS19 Challenge Data: 300 Kidney Tumor Cases with Clinical Context, CT Semantic Segmentations, and Surgical Outcomes"**: This paper introduces the KiTS19 dataset, highlighting its comprehensive nature for kidney tumor segmentation research.
*   **"LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis"**: This publication describes the LiverHccSeg dataset, a valuable resource for liver and HCC tumor segmentation using MRI.
*   **"Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics"**: This paper introduces a substantial dataset of multiphase CECT scans for liver cancer, addressing a gap in existing resources for AI development in this area.
*   **"Deep Learning-Based Liver Tumor Segmentation from Computed Tomography Scans with a Gradient-Enhanced Network"**: This study demonstrates a deep learning approach using the LiTS dataset, showcasing its utility for liver tumor segmentation.

## What to Watch

*   **MIDRC Expansion:** The Medical Imaging and Data Resource Center is continuously expanding its repository and capabilities, aiming to become a more comprehensive resource for various diseases, including chronic liver disease. Researchers should monitor MIDRC for new dataset releases and platform updates.
*   **New Challenge Datasets:** Keep an eye on major medical imaging conferences (e.g., MICCAI, ISBI) for announcements of new challenges and associated datasets, which often lead to valuable public resources. The existence of KiTS23 and earlier KiTS19/21 versions indicates ongoing efforts in kidney tumor segmentation.
*   **Continued TCIA Data Curation:** The Cancer Imaging Archive (TCIA) is a dynamic resource, with new collections and updates being added regularly. Checking TCIA for newly curated datasets relevant to liver and kidney research is recommended.

## Possible Clinical Relevance

The availability of large, well-annotated datasets like KiTS19 and LiTS is crucial for developing and validating AI algorithms for early detection, diagnosis, and treatment planning for kidney and liver cancers. Datasets with associated clinical data, such as KiTS19 and TCGA-LIHC, enable research into imaging biomarkers that correlate with patient outcomes, potentially leading to more personalized treatment strategies. The development of multiphase imaging datasets, like the one described in, is vital for improving the accuracy of cancer subtype classification and treatment response assessment. Furthermore, datasets focusing on specific modalities like ultrasound (Open Kidney Dataset) or MRI (LiverHccSeg, CARE-Liver) can drive advancements in non-invasive diagnostic tools and monitoring techniques. The expansion of resources like MIDRC promises to provide a broader foundation for research into various kidney and liver diseases, fostering more generalized and robust AI solutions for clinical application.

## Sources

1.  Challenge Data - KiTS19. (n.d.). Retrieved from 
2.  [1904.00445] The KiTS19 Challenge Data: 300 Kidney Tumor Cases with Clinical Context, CT Semantic Segmentations, and Surgical Outcomes - arXiv. (n.d.). Retrieved from https://arxiv.org/abs/1904.00445
3.  The Liver Tumor Segmentation Benchmark (LiTS) - PMC - NIH. (n.d.). Retrieved from https://www.ncbi.nlm.nih.gov/pmc/
4.  CT-ORG - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from 
5.  C4KC-KITS - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from 
6.  Liver and Liver Tumor Segmentation - Kaggle. (n.d.). Retrieved from https://www.kaggle.com/datasets/andrewmvd/liver-tumor-segmentation
7.  LiTS - Liver Tumor Segmentation Challenge - CodaLab - Competition. (n.d.). Retrieved from 
8.  Subset of LiTS Dataset for Liver and Tumor Segmentation - Zenodo. (n.d.). Retrieved from https://zenodo.org/record/5141075
9.  Deep Learning-Based Liver Tumor Segmentation from Computed Tomography Scans with a Gradient-Enhanced Network - PMC. (n.d.). Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8881650/
10. Automatic Segmentation of Kidneys and Kidney Tumors: The KiTS19 International Challenge - PMC. (n.d.). Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7140248/
11. KITS 19 - Kidney Tumor Segmentation - Kaggle. (n.d.). Retrieved from 
12. Liver - Datasets - PLCO - The Cancer Data Access System. (n.d.). Retrieved from https://cdas.cancer.gov/plco/datasets/
13. Blood–Liver–Kidney Tri-Organ Imaging Dataset - Kaggle. (n.d.). Retrieved from 
14. Liver cancer Datasets - BioGPS. (n.d.). Retrieved from http://biogps.org/dataset/
15. Medical Image Datasets and Annotations. (n.d.). Retrieved from https://grand-challenge.org/
16. TCGA-LIHC - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from 
17. Liver Cancer Multiclass Dataset - Kaggle. (n.d.). Retrieved from 
18. LiMT: a multi-task liver image benchmark dataset - arXiv. (n.d.). Retrieved from https://arxiv.org/abs/2203.07601
19. Open Kidney Dataset | kidneyUS. (n.d.). Retrieved from 
20. m-aryayi/Medical-Imaging-Datasets: Publicly available medical imaging datasets for research and analysis. - GitHub. (n.d.). Retrieved from https://github.com/m-aryayi/Medical-Imaging-Datasets
21. Medical Imaging Datasets - Intelligent Clinical Care Center (IC3) » » University of Florida. (n.d.). Retrieved from 
22. CARE-Liver. (n.d.). Retrieved from 
23. Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels | Radiology: Artificial Intelligence - RSNA Journals. (n.d.). Retrieved from 
24. CancerLivER: a database of liver cancer gene expression resources and biomarkers - PMC. (n.d.). Retrieved from https://www.ncbi.nlm.nih.gov/pmc/
25. TCGA Kidney Cancers - UCI Machine Learning Repository. (n.d.). Retrieved from 
26. MIDRC. (n.d.). Retrieved from https://www.midrc.org/
27. Dataset Directory - American College of Radiology. (n.d.). Retrieved from 
28. General Dataset (TCIA) - Kaggle. (n.d.). Retrieved from 
29. LiverHccSeg: a multi-task liver image benchmark dataset - arXiv. (n.d.). Retrieved from https://arxiv.org/abs/2306.11468
30. Shared Datasets | Center for Artificial Intelligence in Medicine & Imaging. (n.d.). Retrieved from 
31. Imaging-based deep learning in kidney diseases: recent progress and future prospects. (n.d.). Retrieved from 
32. Comprehensive Medical Imaging Datasets Repository - GitHub. (n.d.). Retrieved from 
33. Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics - PMC. (n.d.). Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8954001/
34. Artificial Intelligence in Renal Imaging: A Multi-Dataset Study for Kidney Disease Classification - MDPI. (n.d.). Retrieved from 
35. Medical Imaging Data Resource Center (MIDRC) - RSNA. (n.d.). Retrieved from 
36. TCGA-KIRC | The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma Collection. (n.d.). Retrieved from 
37. B-MODE-AND-CEUS-LIVER - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from 
38. The Cancer Imaging Archive. (n.d.). Retrieved from https://www.cancerimagingarchive.net/
39. The Medical Imaging and Data Resource Center Commons - MIDRC. (n.d.). Retrieved from 
40. MIDRC Data. (n.d.). Retrieved from https://data.midrc.org/