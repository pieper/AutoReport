# Research Report: Liver-Kidney-Data
*Generated: 2026-05-18 UTC*

## Executive Summary

This report details the current landscape of freely available liver and kidney datasets for research. Several key initiatives, notably the Kidney Precision Medicine Project (KPMP) and the National Cancer Institute's Imaging Data Commons (IDC), offer substantial resources. While KPMP focuses on detailed molecular and spatial data for kidney research, IDC provides a broad range of cancer imaging data, including liver and kidney. The Cancer Imaging Archive (TCIA) remains a crucial repository for cancer-related imaging, with growing collections that often include liver and kidney scans. Emerging trends include the integration of multi-modal data (imaging, genomics, clinical) and the increasing availability of data with permissive licenses.

## Key Announcements by Organization

### Kidney Precision Medicine Project (KPMP)

*   **Expanding Data Repository:** KPMP continues to build a comprehensive atlas of human kidney tissue in health and disease. Their repository includes data from single-cell/nucleus transcriptomics, spatial transcriptomics, proteomics, and various imaging modalities.
*   **Focus on AKI and CKD:** The project is specifically collecting baseline and longitudinal data from participants with Acute Kidney Injury (AKI) and Chronic Kidney Disease (CKD), alongside data from living kidney donors.
*   **Data Accessibility:** While some clinical data is openly available, more detailed datasets often require a Data Use Agreement and approval for access, utilizing controlled access mechanisms.

### National Cancer Institute (NCI) - Imaging Data Commons (IDC)

*   **Massive Data Growth:** As of Spring 2025, IDC hosts over 85 TB of data, encompassing radiology (CT, MRI, PET), digital pathology, and microscopy images, along with associated annotations, segmentations, and clinical data.
*   **Commercial-Friendly Licensing:** The majority (over 95%) of data in IDC is available under the permissive CC-BY license, facilitating commercial reuse.
*   **Integrated Data Sources:** IDC harmonizes data from various NCI initiatives, including The Cancer Genome Atlas (TCGA), The Cancer Imaging Archive (TCIA), and others, providing a unified access point.
*   **Anatomical Sites Covered:** IDC includes imaging data for kidney and liver cancers, among many other anatomical sites.

### The Cancer Imaging Archive (TCIA)

*   **Growing Collections:** TCIA continues to expand its archive of de-identified medical images for cancer research. It serves as a primary source for radiological images (DICOM format) and increasingly includes pathology images.
*   **Pan-Cancer Data:** TCIA data is organized into collections, often by cancer type, modality, or research focus. It provides radiological images matched with clinical, genomic, and pathological data from sources like TCGA and CPTAC.
*   **Licensing Evolution:** While historically most data was CC-BY, recent NIH Controlled Data Access Policy changes mean datasets requiring data use agreements are now managed via dbGaP within the NCI Cancer Research Data Commons.
*   **CT-ORG Dataset:** A notable dataset includes 140 CT scans with five organs (lung, bones, liver, kidneys, bladder) labeled in 3D, useful for organ segmentation tasks, particularly for images exhibiting liver lesions.

## Notable Papers and Associated Datasets

*   **"An atlas of healthy and injured cell states and niches in the human kidney"**: Associated with the Kidney Precision Medicine Project (KPMP), this work provides detailed molecular and spatial data for kidney research.
*   **"CT-ORG | CT volumes with multiple organ segmentations"**: This dataset, available through TCIA, contains CT scans with labeled organs including liver and kidneys, suitable for segmentation model training.
*   **"Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels"**: This dataset offers a substantial collection of abdominal MRI series with liver segmentation masks, valuable for liver segmentation and potentially transferable to kidney segmentation tasks.
*   **"LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis"**: Derived from TCIA-LIHC data, this dataset provides manual segmentations for liver and HCC tumors, offering a resource for evaluating AI algorithms for liver segmentation.
*   **"A Reference Tissue Atlas for the Human Kidney"**: This publication from KPMP describes the construction of an integrated reference map of kidney cells, pathways, and genes using various high-resolution molecular and imaging techniques.

## What to Watch

*   **NCI Cancer Research Data Commons (CRDC):** Continued expansion and integration of data within the CRDC, including IDC and TCIA, is expected to provide even more comprehensive and accessible datasets.
*   **Human Tumor Atlas Network (HTAN):** HTAN is focused on constructing dynamic 3D atlases of human cancers, integrating molecular, cellular, and tissue composition analyses. Datasets generated by HTAN are becoming available through NCI's CRDC.
*   **Advancements in Licensing Transparency:** While many datasets are increasingly under permissive licenses like CC-BY, researchers should remain vigilant about specific license terms for each dataset, especially for commercial use.
*   **Multi-modal Data Integration:** Expect a continued trend towards datasets that combine imaging with multi-omics (genomics, proteomics, transcriptomics) and rich clinical data, offering deeper insights into diseases like liver and kidney cancers.

## Possible Clinical Relevance

The availability of high-quality, diverse datasets with detailed annotations and clinical data is crucial for advancing research in liver and kidney diseases, particularly cancers.

*   **Improved Diagnostic Accuracy:** Large datasets with well-annotated scans allow for the training and validation of AI models that can assist in the early and accurate detection of liver and kidney tumors, as well as other pathologies.
*   **Development of Novel Treatments:** Datasets rich in molecular and clinical information, such as those from KPMP, can help researchers understand disease mechanisms at a deeper level, leading to the identification of new therapeutic targets and personalized treatment strategies.
*   **Enhanced Radiomics and Quantitative Imaging:** Datasets like those in IDC and TCIA, often with accompanying clinical and genomic data, are essential for developing and validating radiomic biomarkers that can predict treatment response or patient outcomes.
*   **Benchmarking and Standardization:** Publicly available datasets with clear segmentation targets, like CT-ORG, are vital for benchmarking segmentation algorithms and promoting standardization in medical image analysis tools, ultimately leading to more reliable clinical applications.

## Sources

*   KPMP Datasets for "An atlas of healthy and injured cell states and niches in the human kidney".
*   Available Data - the Kidney Precision Medicine Project.
*   KPMP Datasets for a Reference Tissue Atlas for the Human Kidney - Zenodo.
*   Kidney Precision Medicine Project (KPMP) - NIDDK Central Repository - NIH.
*   Kidney Tissue Atlas - the Kidney Precision Medicine Project.
*   Imaging Data Commons | CRDC.
*   CT-ORG - The Cancer Imaging Archive (TCIA).
*   Public Medical Image Datasets for Segmentation Foundation Models.
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC.
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC.
*   NCI Data Catalog - National Cancer Institute.
*   TCIA data - The CGC Knowledge Center.
*   The NCI's Human Tumor Atlas Network (HTAN): Generating Spatial Atlases of Cancer Transitions - YouTube.
*   Data Usage Policies and Restrictions - The Cancer Imaging Archive (TCIA).