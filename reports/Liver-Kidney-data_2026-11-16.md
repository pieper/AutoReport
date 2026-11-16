# Research Report: Liver-Kidney-Data
*Generated: 2026-11-16 UTC*

## Executive Summary

This report details publicly available datasets for liver and kidney research, with a focus on cancer. Key findings indicate a growing number of datasets, many leveraging The Cancer Imaging Archive (TCIA) and the NCI Imaging Data Commons (IDC) as foundational sources. Datasets vary in size, annotation quality, and the inclusion of clinical data. Newer datasets like RCC-AID and PLC-CECT offer enhanced annotations and multi-phase imaging, addressing previous limitations. While many datasets provide valuable resources, licensing terms (e.g., CC-BY) are crucial for broad usability. The trend towards open-access data and detailed annotations is a positive development for AI-driven medical research.

## Key Announcements and Dataset Highlights

### The Cancer Imaging Archive (TCIA) and NCI Imaging Data Commons (IDC)

TCIA and the NCI IDC serve as central repositories for a vast amount of medical imaging data, including liver and kidney datasets. They host collections from various projects, including TCGA, and often provide DICOM-formatted data with associated metadata. Many newer datasets leverage these platforms.

*   **NCI Imaging Data Commons (IDC):** A cloud-based environment offering access to over 60 TB of publicly available cancer imaging data, including radiology, digital pathology, and fluorescence imaging. Data is often available under CC-BY licenses. The IDC is continuously enriched with annotations and analysis tools.
*   **The Cancer Imaging Archive (TCIA):** A key resource for radiological imaging data, often linked with genomic and clinical data from TCGA. TCIA hosts numerous collections relevant to liver and kidney research.

### Renal Cell Carcinoma (RCC) Datasets

Recent efforts have focused on improving annotations for kidney cancer datasets derived from TCGA.

*   **RCC-AID (Renal Cell Carcinoma AI Dataset):** This dataset provides voxel-level segmentation annotations for CT scans of 91 patients with clear cell, papillary, and chromophobe RCC. It addresses the common issue of TCGA imaging data lacking easily accessible public annotations. The dataset is derived from TCGA-KIRC, TCGA-KIRP, and TCGA-KICH cohorts and is available at Zenodo. It includes case-level metadata and is released under a CC BY 3.0 license.
*   **UCSF Renal Mass CT Dataset (UCSF RMaC):** This dataset contains 831 3D multiphase CT exams of renal masses (≤7cm) from UCSF. It includes annotations in the form of bounding boxes or polygon masks, along with pathology results from surgical specimens as ground truth. The dataset aims to support the development of algorithms to distinguish aggressive from indolent kidney disease.
*   **C4KC-KITS (Kidney and Kidney Tumor Segmentation Challenge):** This collection includes CT scans and segmentations from the training set of the 2019 KiTS19 challenge, featuring 210 patients with manual semantic segmentations of kidneys and tumors. The data is available under a CC BY 3.0 license.

### Liver Cancer Datasets

Several datasets focus on liver cancer, with a particular emphasis on Hepatocellular Carcinoma (HCC).

*   **PLC-CECT (Primary Liver Cancer CECT Imaging Dataset):** This dataset comprises 3D contrast-enhanced CT (CECT) images from 275 patients with HCC, Intrahepatic Cholangiocarcinoma (ICC), and Combined Hepatocellular-Cholangiocarcinoma (CHCC). It includes multi-phase scans and control scans. Over 50,000 annotated slices are available, making it a valuable resource for liver cancer classification and segmentation. This dataset is publicly available on PhysioNet.
*   **LiverHccSeg:** This dataset provides a curated resource for liver and HCC tumor segmentation tasks, featuring multiphasic contrast-enhanced MRI scans with manual segmentations by two radiologists. It includes 17 cases for liver segmentation and 14 for HCC tumor segmentation, with an analysis of inter-rater agreement. The dataset is derived from the TCGA-LIHC database.
*   **OpenSwissHCC:** This dataset contains 132 multiparametric DCE-MRI scans from adult patients with chronic liver disease, including both HCC-positive (n=63) and HCC-negative (n=69) cases. It features segmentations of up to 5 lesions per patient across different sequences, totaling 140 annotated lesions. Clinical information such as LI-RADS scores and lesion characteristics are included.
*   **HCC-TACE-Seg:** This dataset from TCIA includes pre- and post-treatment CT data from 105 patients with HCC. It contains multi-phase enhanced CT images with semi-automatically performed segmentations of the liver, tumors, and vessels. This dataset is valuable for predicting tumor response to TACE.

### Multi-Organ Datasets

Some datasets encompass multiple organs, including liver and kidneys.

*   **CT-ORG:** This dataset consists of 140 CT scans with 3D labels for organs such as lung, bones, liver, kidneys, and bladder. Many scans exhibit liver lesions. This dataset is suitable for training and evaluating organ segmentation algorithms.
*   **AbdomenCT-1K:** This dataset includes 1,112 abdominal CT scans with annotations for liver, kidney, spleen, and pancreas.

## Notable Papers and Datasets

*   **RCC-AID:** Provides voxel-level segmentation annotations for CT scans of renal cell carcinoma, addressing a gap in TCGA data accessibility.
*   **PLC-CECT:** A comprehensive collection of multi-phase CECT images for primary liver cancer, offering over 50,000 annotated slices.
*   **LiverHccSeg:** Offers multiphasic MRI scans with dual-radiologist segmentations for liver and HCC tumors, including inter-rater agreement analysis.
*   **UCSF RMaC:** Contains multiphase CT exams of renal masses with ground-truth pathology results, aimed at distinguishing aggressive from indolent disease.
*   **OpenSwissHCC:** Features multiparametric DCE-MRI scans for liver disease, with detailed annotations for lesions and clinical data.
*   **CT-ORG:** A multi-organ CT dataset with segmentations for liver, kidneys, and other organs, beneficial for organ segmentation algorithm development.
*   **LiMT (Multi-task Liver Image Benchmark Dataset):** Includes CT volumes for liver and tumor segmentation, multi-label lesion classification, and lesion detection, designed for multi-task learning.
*   **Duke Liver Dataset (DLDS):** Contains abdominal MRI series from patients with liver cirrhosis, with whole-organ liver segmentations available for a subset of series.

## What to Watch

*   **Continued Growth of Annotated Datasets:** Expect more datasets to emerge with high-quality, detailed annotations, particularly leveraging AI for the annotation process itself (e.g., RCC-AID).
*   **Integration with Multi-Omics Data:** Datasets that combine imaging with genomic, clinical, and other molecular data will become increasingly valuable for comprehensive research. Initiatives like TCGA and NCI IDC are central to this trend.
*   **Standardization and Harmonization:** Efforts by organizations like the NCI IDC to harmonize data formats (e.g., DICOM) and provide standardized access will continue to improve data usability and reproducibility.
*   **Focus on Diverse Patient Populations:** As AI models are deployed in clinical settings, there will be a growing demand for datasets representing diverse patient demographics and disease stages.

## Possible Clinical Relevance

The availability of high-quality, well-annotated, and freely accessible datasets is critical for the advancement of AI in medical imaging. These datasets enable the development and validation of robust algorithms for:

*   **Early Detection and Diagnosis:** Improved identification of cancerous lesions in liver and kidneys at earlier stages, potentially leading to better treatment outcomes.
*   **Disease Characterization and Subtyping:** More accurate classification of tumor subtypes and aggressiveness (e.g., differentiating aggressive from indolent RCC), guiding personalized treatment strategies.
*   **Treatment Planning and Monitoring:** Precise segmentation of organs and tumors for surgical planning, radiation therapy, and assessment of treatment response (e.g., predicting response to TACE for HCC).
*   **Prognosis Prediction:** Development of models that can predict patient outcomes based on imaging features, aiding in clinical decision-making.
*   **Reducing Radiologist Workload:** Automating repetitive tasks like segmentation and initial screening can help alleviate the burden on radiologists and improve efficiency.

## Sources

RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research - Zenodo. (n.d.). Retrieved from https://zenodo.org/records/20719257
 ljwa2323/PLC_CECT - GitHub. (n.d.). Retrieved from https://github.com/ljwa2323/PLC_CECT
 RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research. (2026, August 5). medRxiv. 
 Primary Liver Cancer CECT Imaging Dataset. (n.d.). ScienceDB. 
 LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis. (2023, October 10). PubMed Central. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10567218/
 C4KC-KITS - The Cancer Imaging Archive (TCIA). (n.d.). The Cancer Imaging Archive. https://www.cancerimagingarchive.net/collection/c4kc-kits/
 LiMT: a multi-task liver image benchmark dataset. (2025, November 25). arXiv. https://arxiv.org/abs/2311.15778
 OpenSwissHCC: a multiparametric liver MRI dataset with multiple tumor and liver segmentations of pre-treatment hepatocellular carcinomas. (2026, August 21). Zenodo. https://zenodo.org/records/12729296
 Open-Access Medical Image Repositories. (n.d.). aylward.org. 
 RCC-AID: Renal Cell Carcinoma AI Dataset for Medical Imaging Research. (2026, September 21). Melba Journal. 
 Project Imaging-X: A Survey of 1000+ Open-Access Medical Imaging Datasets for Foundation Model Development. (n.d.). GitHub. 
 An Open-Source Clinical Case Dataset for Medical Image Classification and Multimodal AI Applications. (2025, July 31). MDPI. 
 NIHR | NHS Open Source Imaging Datasets. (n.d.). NIHR. 
 UCSF RMaC: UCSF Renal Mass CT Dataset. (2025, January 9). UCSF RMaC. https://github.com/LarsonLab/UCSF-RMaC
 cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification. (n.d.). GitHub. https://github.com/cradleai/LKS-Dataset
 Publicly available medical imaging datasets for research and analysis. (n.d.). GitHub. 
 AIMI Shared Datasets | Center for Artificial Intelligence in Medicine & Imaging. (n.d.). Stanford AIMI. 
 Public Medical Imaging Datasets in MedSeg | CT and MRI. (n.d.). MedSeg. 
 CT-ORG - The Cancer Imaging Archive (TCIA). (2020, January 9). The Cancer Imaging Archive. https://www.cancerimagingarchive.net/collection/ct-org/
 Blood–Liver–Kidney Tri-Organ Imaging Dataset - Mendeley Data. (2026, September 15). Mendeley Data. https://data.mendeley.com/datasets/8m4z2yh9yv/1
 Collections | IDC - Imaging Data Commons - National Cancer Institute. (n.d.). National Cancer Institute. https://imaging.datacommons.cancer.gov/collections/
 Open Kidney Dataset | kidneyUS. (n.d.). kidneyUS. 
 Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels. (n.d.). PubMed. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10140244/
 Advances in Artificial Intelligence‐Based Liver‐Related Semantic Segmentation Techniques and Applications Using CT Imaging. (n.d.). PubMed. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10879219/
 Medical Imaging Datasets — PYCAD. (n.d.). PYCAD. 
 The Liver Kidney Stomach Dataset - COVE - Computer Vision Exchange. (2020, August 24). COVE. 
 MMIST ccRCC Dataset. (n.d.). MMIST ccRCC Dataset. 
 Dataset Roundup - Noteworthy Datasets on Liver Diseases - Elucidata. (2022, May 25). Elucidata. https://www.elucidata.io/blog/dataset-roundup-noteworthy-datasets-on-liver-diseases
 Liver - Datasets - PLCO - The Cancer Data Access System. (n.d.). The Cancer Data Access System. https://cdas.cancer.gov/plco/datasets/
 Top Liver Datasets and Models - Roboflow Universe. (n.d.). Roboflow Universe. 
 Imaging Data Commons | IDC - Imaging Data Commons - National Cancer Institute. (n.d.). National Cancer Institute. https://imaging.datacommons.cancer.gov/
 National Cancer Institute Imaging Data Commons (IDC) Collections. (n.d.). AWS Open Data Registry. https://registry.opendata.aws/nci-imaging-data-commons/
 NCI Imaging Data Commons. (n.d.). National Cancer Institute. https://imaging.datacommons.cancer.gov/
 Kidney Datasets - BioGPS. (n.d.). The Scripps Research Institute. 
 Artificial Intelligence in Renal Imaging: A Multi-Dataset Study for Kidney Disease Classification. (2026, May 14). MDPI. 
 NCI Imaging Data Commons. (2021, August 15). PubMed. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8373794/
 Awesome-Medical-Dataset/resources/HCC-TACE-Seg.md at main - GitHub. (n.d.). GitHub. 
 TCIA/TGCA-LIHC portal venous phase CT-scans for cirrhosis classification. (2023, July 31). Zenodo. https://zenodo.org/records/10071105
 TCGA-KIRC | The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma Collection. (n.d.). The Cancer Imaging Archive. https://www.cancerimagingarchive.net/collection/tcga-kirc/