# Research Report: Liver-Kidney-Data
*Generated: 2026-06-01 UTC*

## Executive Summary

This report details freely available datasets for liver and kidney research, focusing on imaging data for disease characterization, particularly cancers. Key datasets offer substantial patient numbers, high-quality scans, and varying degrees of annotation and clinical data. Licenses are generally permissive, favoring CC-BY. Recent advancements include more comprehensive multi-phase CT datasets for liver cancer and improved annotations for kidney tumor segmentation. These resources are critical for developing AI-driven diagnostic and treatment planning tools, with ongoing efforts to expand data availability and quality.

## Key Announcements, Grouped by Organization

### NCI Imaging Data Commons (IDC)
*   The IDC, as of Spring 2025, houses over 85 TB of cancer imaging data, including radiology and microscopy images, with associated annotations, segmentations, and clinical data.
*   Over 95% of the data in IDC is licensed under CC-BY, promoting commercial reuse.
*   IDC aggregates data from various sources, including TCGA and TCIA, harmonizing it into DICOM format for accessibility.

### The Cancer Imaging Archive (TCIA)
*   TCIA provides access to a large archive of de-identified cancer images, including radiology and digital histopathology, often linked to clinical, genomic, and outcome data.
*   Most TCIA data is available under permissive CC-BY licenses (3.0 or 4.0), though a small subset has commercial use restrictions.
*   Newer TCIA datasets requiring data use agreements are now managed by the NCI Cancer Research Data Commons and accessed via dbGaP.
*   The **C4KC-KiTS** collection contains CT scans and segmentations from the 2019 Kidney and Kidney Tumor Segmentation Challenge (KiTS19), with 210 patients and manual segmentations of kidneys and tumors.
*   The **TCGA-KIRC** collection focuses on Kidney Renal Clear Cell Carcinoma, linking radiological data from TCIA with clinical and genomic data from the Genomic Data Commons (GDC).

### Kaggle
*   The **Liver Cancer Multiclass Dataset** categorizes liver MRI images into five classes: malignant tumors, benign tumors, and non-cancerous scans.
*   The **Blood–Liver–Kidney Tri-Organ Imaging Dataset** includes separate datasets for blood cell detection, liver tissue classification, and kidney tissue classification.
*   The **Kidney Function Health Dataset** is a synthetic but medically realistic collection of kidney-related health indicators for regression and classification tasks.

### Mendeley Data
*   The **Kidney stone detection** dataset features CT scan images for kidney stone detection, including original and augmented images with annotations.
*   The **Benchmark Diagnostic MRI and Medical Imaging Dataset** (updated September 16, 2024) contains over 34,000 MRI scans across 40 disease classes, focusing on brain, neuro, and spine.

### GitHub Repositories
*   The **m-aryayi/Medical-Imaging-Datasets** repository is a collection of publicly available medical imaging datasets, aiming to be a comprehensive resource.
*   The **cradleai/LKS-Dataset** is a novel Liver, Kidney, and Stomach (LKS) dataset constructed from routine clinical samples, comprising sections of rodent kidney, stomach, and liver tissue.

### Other Notable Repositories and Datasets
*   **Primary Liver Cancer CECT Imaging Dataset** (May 15, 2025) offers a large dataset of 278 primary liver cancer cases with full four-phase CECT scans and annotations, including HCC, ICC, and cHCC-CCA.
*   **ATLAS Dataset** (Tumour and Liver Automatic Segmentation) consists of 90 liver-focused CE-MRI acquisitions with liver and tumor segmentation masks for HCC.
*   **LiverHccSeg** provides liver and HCC tumor segmentations on multiphasic contrast-enhanced MRI scans, with annotations from two radiologists.
*   **LiTS (Liver Tumor Segmentation)** dataset comprises 201 abdominal CT scans with liver and liver tumor annotations.
*   **CHAOS (Combined Healthy Abdominal Organ Segmentation)** dataset includes abdominal CT and MR scans from healthy subjects, with segmentations for liver, kidneys, and spleen.
*   **Duke Liver Dataset (DLDS)** contains 2,146 abdominal MRI series from 105 patients with liver cirrhosis, including 310 series with manually segmented liver masks.
*   **KiTS (Kidney Tumor Segmentation)** dataset provides annotated CT scans of kidneys and kidney tumors, utilized in segmentation challenges.
*   **Open Kidney Dataset** offers over 500 annotated ultrasound images for kidney analysis, available for non-commercial use.
*   **CKD Dynamic Dataset** by Briya contains over 31,000 patient records with comprehensive data on Chronic Kidney Disease, including imaging data.
*   **ILPD (Indian Liver Patient Dataset)** from UCI Machine Learning Repository includes 583 patient records with biochemical markers for liver disease prediction.

## Notable Papers Describing Datasets

*   **Primary Liver Cancer CECT Imaging Dataset:** This dataset facilitates the development and validation of diagnostic and segmentation models for liver cancer using full-phase 3D CECT images.
*   **ATLAS Dataset:** The first public dataset providing CE-MRI of HCC with systematic annotations of liver and liver tumors, aiding automated segmentation tools for treatment planning.
*   **LiverHccSeg:** This dataset provides manual whole-liver and tumor segmentations from two radiologists on multiphasic CE-MRI, enabling robust validation of segmentation algorithms.
*   **LiMT:** Introduces a 3D CT multi-task dataset for liver and tumor segmentation, multi-label lesion classification, and detection, addressing the limitation of single-task datasets.
*   **KidneyNeXt:** Proposes a lightweight CNN architecture for multi-class renal tumor classification using CT imaging, evaluated on multiple datasets including the Kaggle CT KIDNEY dataset.
*   **Kidney stone detection:** This dataset provides CT scan images for kidney stone detection with annotations at a detailed level, supporting AI and deep learning applications.
*   **Open Kidney Dataset:** This dataset aims to standardize ultrasound segmentation benchmarking and reduce interpretation efforts in AI-enhanced ultrasound.

## What to Watch

*   **NCI Imaging Data Commons (IDC):** As of Spring 2025, IDC is continuously expanding its 85 TB of cancer imaging data, with a strong emphasis on CC-BY licensing for broad accessibility.
*   **TCIA:** Continues to be a primary repository for cancer imaging data, with ongoing additions and updates to collections like C4KC-KiTS and TCGA-KIRC.
*   **Newer Datasets:** Keep an eye on recent publications announcing new datasets, such as the "Primary Liver Cancer CECT Imaging Dataset" (May 2025) and "Kidney stone detection" (March 2025), which offer valuable, up-to-date resources.
*   **AI Challenges:** Events like the ATLAS challenge (MICCAI 2023) and the KiTS challenge highlight the development and evaluation of AI models using specific datasets, often leading to further dataset refinement or new benchmark releases.

## Possible Clinical Relevance

These datasets are crucial for advancing AI in medical diagnostics and treatment planning for liver and kidney diseases.

*   **Early Detection and Diagnosis:** High-quality, annotated imaging datasets enable the training of AI models for more accurate and timely detection of liver and kidney cancers and other pathologies. For instance, datasets like the "Primary Liver Cancer CECT Imaging Dataset" and the "KiTS" dataset are vital for developing automated systems that can identify and segment tumors.
*   **Treatment Planning:** Detailed segmentations of organs and tumors, as provided in datasets like ATLAS and LiverHccSeg, are essential for precise surgical planning, radiation therapy, and interventional procedures like transarterial radioembolisation (TARE).
*   **Prognosis and Risk Stratification:** Datasets with associated clinical and outcome data, such as TCGA-KIRC or the CKD Dynamic Dataset, can help develop models that predict disease progression and patient outcomes, aiding in personalized treatment strategies.
*   **Drug Discovery and Development:** Multi-omics data linked with imaging, as explored in research on liver diseases and CKD/NAFLD, can accelerate the identification of biomarkers and therapeutic targets.
*   **Improving Workflow Efficiency:** Automated segmentation and classification tools trained on these datasets can reduce the workload for radiologists and clinicians, allowing them to focus on more complex cases and patient interaction.

## Sources

 Luo, X., et al. (2025, May 15). Primary Liver Cancer CECT Imaging Dataset. *arXiv*. Retrieved from https://arxiv.org/abs/2405.07493
 Rusu, A., et al. (2023, April 27). A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma. *Hepatoma Research*. Retrieved from 
 Liver Cancer Multiclass Dataset. (n.d.). *Kaggle*. Retrieved from 
 Liu, Z., et al. (2025, November 25). LiMT: a multi-task liver image benchmark dataset. *arXiv*. Retrieved from https://arxiv.org/abs/2405.18681
 Blood–Liver–Kidney Tri-Organ Imaging Dataset. (n.d.). *Kaggle*. Retrieved from 
 Ghaffari, M., et al. (2023). LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis. *Scientific Reports*, *13*(1). 
 NCI Imaging Data Commons (IDC). (n.d.). *National Cancer Institute*. Retrieved from https://imaging.datacommons.cancer.gov/
 Kidney Tumor Segmentation Challenge (KiTS). (n.d.). *Keosys*. Retrieved from 
 C4KC-KITS. (n.d.). *The Cancer Imaging Archive*. Retrieved from https://www.cancerimagingarchive.net/collection/c4kc-kits/
 TCGA-KIRC. (n.d.). *The Cancer Imaging Archive*. Retrieved from https://www.cancerimagingarchive.net/collection/tcga-kirc/
 MMIST ccRCC Dataset. (n.d.). *Mendeley Data*. Retrieved from https://data.mendeley.com/datasets/fk8k6fct7p/1
 Duke Liver Dataset (DLDS). (2023, April 20). *Zenodo*. Retrieved from https://zenodo.org/record/7774566
 KidneyNeXt: A Lightweight Convolutional Neural Network for Multi-Class Renal Tumor Classification in Computed Tomography Imaging. (2025, July 11). *PubMed Central*. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11251895/
 m-aryayi/Medical-Imaging-Datasets. (2025, January 23). *GitHub*. Retrieved from https://github.com/m-aryayi/Medical-Imaging-Datasets
 Open Kidney Dataset. (2022, June 14). *GitHub*. Retrieved from 
 Medical Imaging Datasets. (n.d.). *University of Florida IC3*. Retrieved from 
 Benchmark Diagnostic MRI and Medical Imaging Dataset. (2024, September 16). *Mendeley Data*. Retrieved from https://data.mendeley.com/datasets/d73rs38yk6
 Data Usage Policies and Restrictions. (n.d.). *The Cancer Imaging Archive*. Retrieved from 
 CKD Dynamic Dataset. (n.d.). *Briya*. Retrieved from https://briya.ai/datasets/ckd-dynamic-dataset/
 Luo, X., et al. (2025, September 19). Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics. *PubMed Central*. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11426320/
 List of Open Access Medical Imaging Datasets. (2023, March 9). *radRounds Radiology Network*. Retrieved from 
 cradleai/LKS-Dataset. (2023, January 23). *GitHub*. Retrieved from https://github.com/cradleai/LKS-Dataset
 Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels. (2023, April 20). *Radiology: Artificial Intelligence*. Retrieved from 
 Liver - Datasets - PLCO. (n.d.). *The Cancer Data Access System*. Retrieved from 
 ILPD (Indian Liver Patient Dataset). (2012, May 20). *UCI Machine Learning Repository*. Retrieved from https://archive.ics.uci.edu/dataset/354/indian-liver-patient-dataset
 Kidney stone detection via axial CT imaging: A dataset for AI and deep learning applications. (2025, March 5). *Mendeley Data*. Retrieved from https://data.mendeley.com/datasets/b39j3zdxkb
 Liver Patient Dataset. (2019, May 19). *Kaggle*. Retrieved from 
 Kidney Function Health Dataset. (n.d.). *Kaggle*. Retrieved from 
 Datasets. (n.d.). *UCI Machine Learning Repository*. Retrieved from https://archive.ics.uci.edu/datasets?p=2&ps=50
 Identification of biomarkers for the diagnosis of chronic kidney disease (CKD) with non-alcoholic fatty liver disease (NAFLD) by bioinformatics analysis and machine learning. (2023, February 26). *Frontiers*. Retrieved from 
 Dataset Roundup - Noteworthy Datasets on Liver Diseases. (2022, May 25). *Elucidata*. Retrieved from https://www.elucidata.io/blog/dataset-roundup-noteworthy-datasets-on-liver-diseases
 Collection of awesome medical dataset resources. (2025, January 23). *GitHub*. Retrieved from 
 Shared Datasets. (n.d.). *Center for Artificial Intelligence in Medicine & Imaging*. Retrieved from https://aimi.stanford.edu/shared-datasets