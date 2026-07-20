# Research Report: Liver-Kidney-Data
*Generated: 2026-07-20 UTC*

## Executive Summary

This report details currently available, freely accessible datasets for liver and kidney imaging research, with a focus on cancer and well-annotated pathologies. Key datasets include the Liver Tumor Segmentation Benchmark (LiTS) and the Kidney and Kidney Tumor Segmentation Challenge (KiTS) series, which offer a substantial number of scans with detailed annotations. The TCGA (The Cancer Genome Atlas) project provides extensive clinical and genomic data alongside imaging for both liver (TCGA-LIHC) and kidney (TCGA-KIRC, TCGA-KIRP, TCGA-KICH) cancers. Recent advancements include the KiTS23 dataset, which expands the number of cases and includes nephrogenic contrast phases. Several datasets offer comprehensive clinical data, crucial for developing predictive models. The majority of these datasets are under permissive licenses like CC BY, though some specific use cases may have non-commercial restrictions.

## Key Announcements by Organization

### The Cancer Genome Atlas (TCGA) Program

TCGA continues to be a primary source for comprehensive cancer datasets, integrating genomic, clinical, and imaging data.

*   **TCGA-LIHC (Liver Hepatocellular Carcinoma):** This collection offers clinical, genetic, pathological, and radiological data for liver cancer patients. Images are available through The Cancer Imaging Archive (TCIA), while clinical and genomic data are in the Genomic Data Commons (GDC) Data Portal. Recent updates may include expanded clinical data or improved access mechanisms.
*   **TCGA-KIRC, TCGA-KIRP, TCGA-KICH (Kidney Renal Cell Carcinoma sub-types):** Similar to the liver collection, these provide integrated data for different kidney cancer subtypes. Imaging is on TCIA, with clinical and genomic data on the GDC Data Portal. The RCC-AID dataset specifically provides voxel-level segmentation annotations for these cohorts.

### Kidney and Kidney Tumor Segmentation Challenge (KiTS)

The KiTS series has been instrumental in advancing kidney tumor segmentation research.

*   **KiTS23:** This latest iteration significantly expands the dataset with 599 cases (489 for training, 110 for testing). A key update is the inclusion of scans in the nephrogenic contrast phase, alongside the previous late arterial phase, offering richer imaging data. The training set includes cases from previous KiTS challenges (KiTS19, KiTS21).
*   **KiTS19:** A foundational dataset with 300 contrast-enhanced CT scans and manual segmentations of kidneys and tumors.

### Liver Tumor Segmentation Benchmark (LiTS)

LiTS is a well-established benchmark for liver and liver tumor segmentation.

*   **LiTS:** This dataset comprises 201 CT volumes with annotations for liver and lesions, collected from multiple institutions worldwide. It has been used in several challenges (ISBI 2017, MICCAI 2017/2018) and remains a critical resource. The dataset includes primary and secondary liver tumors with varied characteristics.

## Notable Papers

*   **"The KiTS23 Challenge Data: 300 Kidney Tumor Cases with Clinical Context, CT Semantic Segmentations, and Surgical Outcomes"** (arXiv:1904.00445) describes the KiTS19 dataset, providing a valuable resource with imaging, segmentation masks, and clinical outcomes for kidney tumor research.
*   **"The Liver Tumor Segmentation Benchmark (LiTS)"** reports on the setup and results of the LiTS challenge, detailing the diverse image dataset and performance benchmarks for liver and tumor segmentation algorithms.
*   **"Deep Learning-Based Liver Tumor Segmentation from Computed Tomography Scans with a Gradient-Enhanced Network"** (PMC, February 01, 2026) utilizes the LiTS dataset to present a novel segmentation method, demonstrating state-of-the-art performance.
*   **"RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research"** (Zenodo, April 22, 2026) introduces a dataset with voxel-level segmentation annotations for CT imaging from three TCGA renal cell carcinoma cohorts, aiming to improve accessibility and reproducibility.
*   **"MRSegMentator: An nnU-Net-based, cross-modality image segmentation model that segments 40 anatomic structures in both MRI and CT images"** (Radiology: Artificial Intelligence, RSNA Journals) describes a model trained on datasets including UK Biobank, an in-house dataset, and TotalSegmentator CT, demonstrating high segmentation accuracy for organs like the liver and kidneys across modalities.

## What to Watch

*   **Continued expansion of KiTS:** Future iterations of the KiTS challenge are likely to further increase the dataset size and potentially incorporate new imaging phases or modalities.
*   **TCGA data integration:** Ongoing efforts to integrate and make accessible the vast clinical and genomic data from TCGA with imaging will continue to be a major trend, enabling more holistic research.
*   **Multi-organ segmentation datasets:** Datasets like CT-ORG and AbdomenCT-1K, which include segmentations for multiple abdominal organs (liver, kidneys, spleen, pancreas), are becoming more prevalent and will be crucial for developing robust, generalizable models. The MORE dataset aims for even greater scale and diversity in CT reconstruction.
*   **New modalities:** While CT and MRI dominate, emerging datasets focusing on other modalities like ultrasound (Open Kidney Dataset) or spectral imaging for kidney analysis may offer new avenues for research.

## Possible Clinical Relevance

These datasets are crucial for developing and validating AI models that can assist clinicians in:

*   **Early Disease Detection:** Identifying subtle signs of liver and kidney tumors or other pathologies in imaging scans.
*   **Accurate Segmentation:** Precisely delineating tumor boundaries and organ structures, essential for surgical planning (e.g., nephron-sparing surgery) and radiation therapy.
*   **Risk Stratification and Prognosis:** Using imaging features alongside clinical and genomic data to predict disease progression, treatment response, and patient outcomes.
*   **Monitoring Treatment Efficacy:** Quantifying changes in tumor size or characteristics over time to assess the effectiveness of therapies.
*   **Reducing Workload:** Automating time-consuming tasks like image segmentation and analysis, allowing clinicians to focus on more complex aspects of patient care.

## Sources

*   
*   https://imaging.cancer.gov/programs/radiology-da
*   https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga
*   
*   https://arxiv.org/abs/1904.00445
*   https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10830865/
*   https://www.cancerimagingarchive.net/collection/tcga-lihc/
*   
*   
*   
*   https://huggingface.co/datasets/WSKINGDOM/MORE
*   https://www.cancerimagingarchive.net/collection/c4kc-kits/
*   
*   https://academictorrents.com/details/27772adef6f563a1ecc0ae19a528b956e6c803ce
*   https://zenodo.org/records/11489615
*   
*   
*   
*   
*   https://www.cancerimagingarchive.net/collection/ct-org/
*   
*   https://zenodo.org/records/1184069
*   
*   https://github.com/cradleai/LKS-Dataset
*   https://www.youtube.com/watch?v=XJ4bJ4Nq8a4
*   https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9634209/
*   https://arxiv.org/abs/2401.16783
*   https://github.com/adalca/medical-datasets
*   https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6524157/
*   
*   https://livercellatlas.org/