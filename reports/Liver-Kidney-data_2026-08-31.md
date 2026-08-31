# Research Report: Liver-Kidney-Data
*Generated: 2026-08-31 UTC*

## Liver and Kidney Datasets Report

### Executive Summary

This report details freely available liver and kidney datasets for research, focusing on those with large patient numbers, high-quality scans, extensive annotations, and relevant clinical data. The Cancer Imaging Archive (TCIA) and The Cancer Genome Atlas (TCGA) initiatives are primary sources for cancer-related imaging data, offering significant collections for both liver (TCGA-LIHC) and kidney (TCGA-KIRC, TCGA-KICH, TCGA-KIRP) cancers. These datasets are valuable due to their linked genomic and clinical data, though image heterogeneity is a noted challenge. Newer datasets, such as the Kidney and Kidney Tumor Segmentation Challenge (KiTS19) and the Primary Liver Cancer CECT Imaging Dataset (PLC-CECT), offer more specific annotations and multi-phase imaging crucial for AI development. The UK Biobank is a significant source for general organ imaging, providing data on liver and kidney characteristics, while specialized datasets like the Blood–Liver–Kidney Tri-Organ Imaging Dataset and the UCSF Renal Mass CT Dataset cater to specific research needs.

### Key Announcements by Organization

*   **The Cancer Imaging Archive (TCIA) & The Cancer Genome Atlas (TCGA)**
    *   **TCGA-LIHC (Liver Hepatocellular Carcinoma Collection):** A major resource providing CT imaging data for liver cancer patients, linked to clinical and genomic data from TCGA. Images are heterogeneous due to multiple acquisition sites and protocols.
    *   **TCGA-KIRC, TCGA-KICH, TCGA-KIRP (Kidney Cancer Collections):** Similar to TCGA-LIHC, these collections offer imaging data for various kidney cancer subtypes (Clear Cell, Chromophobe, Papillary Renal Cell Carcinoma) linked to TCGA's clinical and genomic databases.
    *   **C4KC-KiTS (Kidney and Kidney Tumor Segmentation Challenge):** This dataset includes CT scans and manual semantic segmentations of kidneys and tumors from patients who underwent nephrectomy. It's a valuable resource for segmentation tasks.
    *   **RCC-AID (Renal Cell Carcinoma AI Dataset):** Provides voxel-level segmentation annotations for CT imaging from TCGA kidney cancer cohorts (KIRC, KIRP, KICH), addressing the lack of easily accessible annotations in TCGA data.

*   **UK Biobank**
    *   **Abdominal MRI Data:** Offers extensive MRI data, including scans of the liver and kidneys, providing quantitative data on organ volume, fat percentage, and iron content. This dataset is suitable for large-scale population studies and analysis of organ health.

*   **Medical Imaging and Data Resource Center (MIDRC)**
    *   **Expanding Data Commons:** MIDRC is an open-access platform aiming to provide standardized, aggregated, and curated imaging data for machine learning research. It includes data from various institutions and covers chronic diseases, including liver and kidney conditions.

*   **Kaggle**
    *   **Blood–Liver–Kidney Tri-Organ Imaging Dataset:** A multi-modal dataset containing blood cell detection, liver tissue analysis, and kidney tissue analysis datasets, suitable for object detection and tissue classification.
    *   **TCGA-KIRP:** A Kaggle version of the TCGA Kidney Renal Papillary Cell Carcinoma collection, providing access to this dataset.

### Notable Papers and Datasets

*   **The Cancer Genome Atlas (TCGA) Initiative:** Provides a foundational collection of linked imaging, clinical, and genomic data for various cancers, including liver (TCGA-LIHC) and kidney (TCGA-KIRC, TCGA-KICH, TCGA-KIRP).
*   **Kidney and Kidney Tumor Segmentation Challenge (KiTS19):** Released CT scans with manual segmentations of kidneys and tumors, crucial for developing automated segmentation models.
*   **Primary Liver Cancer CECT Imaging Dataset (PLC-CECT):** A comprehensive dataset of multi-phase CT scans for primary liver cancer, featuring expert annotations, addressing a gap in public data for AI development.
*   **UCSF Renal Mass CT Dataset:** Contains 831 multiphase CT exams of renal masses with annotations and pathology results, aimed at distinguishing aggressive from indolent kidney disease.
*   **UK Biobank:** Offers large-scale abdominal MRI data with quantitative measures of liver and kidney health, enabling population-level health studies.
*   **MMIST ccRCC Dataset:** Curated from CPTAC-CCRCC and TCGA-KIRC, this dataset focuses on clear cell renal cell carcinoma (ccRCC) and includes CT, MRI, WSI, genomics, and clinical data.
*   **LiverHccSeg:** Provides multiphasic MRI data with liver and HCC tumor segmentations from two radiologists, including inter-rater agreement analysis.
*   **ATLAS Dataset:** The first public dataset with CE-MRI of HCC, providing liver and liver tumor segmentation masks for 90 patients, facilitating automated delineation development.
*   **MCT-LTDiag:** A multi-phase CT dataset for liver tumor diagnosis, containing 517 cases with five tumor subtypes and expert-annotated tumor masks, designed for AI-based classification.
*   **RCC-AID:** Offers segmentation annotations for CT imaging from TCGA kidney cancer cohorts, improving accessibility of annotated TCGA imaging data.

### What to Watch

*   **MIDRC's Continued Expansion:** MIDRC is actively expanding its data commons to include more chronic disease data and is developing a federated data search and analysis platform, which will likely yield more comprehensive liver and kidney datasets in the future.
*   **UK Biobank Updates:** UK Biobank regularly releases new tranches of imaging data, which may include further detailed information on liver and kidney health parameters.
*   **New Publication-Driven Datasets:** Emerging research frequently leads to the release of new, specialized datasets. Researchers should monitor publications in major medical imaging and AI conferences and journals for novel collections. For instance, the "A multi-paradigm evaluation spanning pixels to voxels for deep learning-based kidney tumor segmentation" paper published in "Journal of medical engineering & technology" in 2026 might be associated with new datasets or dataset expansions.

### Possible Clinical Relevance

The datasets described have significant clinical relevance for:

*   **Early Disease Detection and Diagnosis:** Improved AI models trained on these datasets can aid in the earlier and more accurate detection of liver and kidney cancers, as well as other conditions like liver fibrosis and chronic kidney disease.
*   **Treatment Planning and Response Prediction:** Detailed annotations and multi-phase imaging can help in precisely planning treatments such as surgery or transarterial radioembolisation (TARE) and in predicting treatment efficacy.
*   **Prognosis Assessment:** Datasets linking imaging features with clinical outcomes and pathology reports can help develop models to predict patient prognosis, guiding clinical management.
*   **Understanding Disease Heterogeneity:** The inclusion of diverse patient populations, disease subtypes, and multi-modal data (imaging, genomics, clinical) allows for a deeper understanding of disease variability and the identification of novel biomarkers.
*   **Personalized Medicine:** By integrating imaging data with other omics data (genomics, proteomics), these datasets can contribute to the development of personalized treatment strategies.

---

### Sources

*   TCGA-LIHC | The Cancer Genome Atlas Liver Hepatocellular Carcinoma Collection. https://www.cancerimagingarchive.net/TCGA-LIHC/
*   The Cancer Genome Atlas Liver Hepatocellular Carcinoma Collection (TCGA-LIHC). 
*   TCGA-KIRC | The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma Collection. https://www.cancerimagingarchive.net/TCGA-KIRC/
*   Collection TCGA-KICH - Imaging Data Commons. 
*   TCGA-LIHC (Liver Hepatocellular Carcinoma) - Hugging Face. 
*   TCGA-KICH - The Cancer Imaging Archive (TCIA). https://www.cancerimagingarchive.net/TCGA-KICH/
*   C4KC-KiTS - The Cancer Imaging Archive (TCIA). https://www.cancerimagingarchive.net/C4KC-KiTS/
*   Blood–Liver–Kidney Tri-Organ Imaging Dataset - Kaggle. 
*   Imaging Data - UK Biobank Community. 
*   Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics - PMC. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10451930/
*   Primary Liver Cancer CECT Imaging Dataset (PLC-CECT) - GitHub. 
*   TCGA-KIRP - Kaggle. 
*   RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research - Zenodo. 
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9206067/
*   A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma - MDPI. 
*   MMIST ccRCC Dataset. 
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8143258/
*   Medical Imaging and Data Resource Center (MIDRC) - RSNA. 
*   10 research findings from our imaging project's first decade - UK Biobank. 
*   The KiTS19 Challenge Data: 300 Kidney Tumor Cases with Clinical Context, CT Semantic Segmentations, and Surgical Outcomes. https://arxiv.org/abs/2107.00044
*   Systematic quantification of health parameters from UK Biobank abdominal MRI - bioRxiv. 
*   UCSF RMaC: UCSF Renal Mass CT Dataset. 
*   RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research - Zenodo. 
*   Data from the training set of the 2019 Kidney and Kidney Tumor Segmentation Challenge (C4KC-KiTS) - Cancer Imaging Archive Wiki. https://wiki.cancerimagingarchive.net/display/Public/Data+from+the+training+set+of+the+2019+Kidney+and+Kidney+Tumor+Segmentation+Challenge+%28C4KC-KiTS%29
*   MIDRC Data Commons. 