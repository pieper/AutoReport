# Research Report: Liver-Kidney-Data
*Generated: 2026-05-11 UTC*

## Executive Summary

This report details the current landscape of freely available liver and kidney imaging datasets, with a focus on those suitable for research into well-described diseases like cancer. Several promising datasets have been identified, offering varying degrees of patient numbers, scan quality, annotation availability, and accompanying clinical data. The Duke Liver Dataset stands out for its extensive MRI series and segmentation masks. The NCI Imaging Data Commons (IDC) provides a vast repository of cancer imaging data with a strong emphasis on CC-BY licensing. Emerging datasets like the Blood–Liver–Kidney Tri-Organ Imaging Dataset offer multi-modal capabilities. While many datasets focus on segmentation, there is a continuous need for datasets with comprehensive clinical data and annotations for complex disease patterns.

## Key Announcements and Dataset Highlights

### NCI Imaging Data Commons (IDC)

*   **Vast Data Repository:** As of Spring 2025, IDC houses over 85 TB of cancer imaging data, including radiology (CT, MRI, PET), digital pathology, and multispectral microscopy images.
*   **Commercial-Friendly Licensing:** Over 95% of the data is under the permissive CC-BY license, facilitating commercial reuse. A small subset uses CC-NC.
*   **Harmonized Data:** All images and derived data are harmonized into the standard DICOM format.
*   **Comprehensive Sources:** IDC ingests data from numerous sources, including TCGA, TCIA, CPTAC, and others, providing a rich and diverse collection.

### Duke Liver Dataset (DLDS)

*   **Extensive MRI Data:** Contains 2,146 abdominal MRI series from 105 patients, many with cirrhotic features.
*   **Segmentation Masks:** Includes hand-drawn, whole-organ liver segmentations for 310 image series.
*   **Potential for Transfer Learning:** The dataset is well-suited for training segmentation models for other abdominal organs like the spleen and kidneys.
*   **Availability:** Downloadable from Zenodo.

### Blood–Liver–Kidney Tri-Organ Imaging Dataset

*   **Multi-Modal Approach:** Consists of three datasets: blood cell detection (object detection), liver tissue analysis (classification), and kidney tissue analysis (classification).
*   **Designed for Correlation:** Intended for multi-sample correlation analysis across different tissue types and blood cell analysis.
*   **Total Images:** Includes a total of 2,874 images with annotations for object detection and tissue classification tasks.

### Hyper and Multispectral Kidney Image Dataset

*   **Novel Imaging Modalities:** A balanced collection of 20,000 hyperspectral and multispectral kidney images for classifying normal versus tumor tissues.
*   **High Spectral Resolution:** Hyperspectral images offer fine-grained tissue characterization, while multispectral images capture broader spectral information.
*   **License:** Released under CC0: Public Domain.

### MMIST ccRCC Dataset

*   **Kidney Cancer Focus:** Curated from CPTAC-CCRCC and TCGA-KIRC studies, focusing on clear cell renal cell carcinoma (ccRCC).
*   **Multi-Modal Data:** Includes CT and MRI images, with options to access data from TCGA and CPTAC repositories.
*   **Reduced Volumes:** Data was curated to reduce redundancy, with 736 CT and 552 MRI volumes used.

### Other Notable Datasets

*   **Medical-Imaging-Datasets (GitHub):** A collection of publicly available medical imaging datasets, including some with CC BY 4.0 licenses for liver metastases, and others with CC BY-NC-ND 4.0 for liver MRI.
*   **LiMT (Liver Multi-Task Dataset):** A multi-task liver dataset designed for liver and tumor segmentation, and multi-task learning.
*   **Open Kidney Dataset:** Provides over 500 annotated ultrasound images of kidneys for non-commercial use, addressing the lack of open ultrasound data.

## Notable Papers and Datasets Described

*   **"Blood–Liver–Kidney Tri-Organ Imaging Dataset"**: This dataset offers a multi-modal approach for object detection and tissue classification, designed for multi-sample correlation analysis across blood, liver, and kidney tissues.
*   **"Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels"**: This paper introduces a comprehensive liver MRI dataset with over 2000 series and segmentation masks, valuable for developing and evaluating automated segmentation models.
*   **"MMIST ccRCC Dataset"**: This dataset focuses on clear cell renal cell carcinoma (ccRCC) and is curated from established studies, providing multi-modal CT and MRI data for research.
*   **"Hyper and Multispectral Kidney Image dataset"**: This dataset provides a large collection of hyperspectral and multispectral kidney images to advance research in spectral imaging for kidney abnormality detection.
*   **"Advances in Artificial Intelligence‐Based Liver‐Related Semantic Segmentation Techniques and Applications Using CT Imaging"**: This review highlights advancements in AI-based semantic segmentation for liver CT imaging and mentions datasets containing CT and MRI images with 3D segmentations of liver, spleen, and kidneys.

## What to Watch

*   **NCI Imaging Data Commons (IDC) Growth:** Continued expansion of data, especially with its CC-BY licensing, makes it a key resource to monitor for new liver and kidney cancer datasets.
*   **Advancements in Multi-Organ Datasets:** Datasets like the Blood–Liver–Kidney Tri-Organ Imaging Dataset signal a trend towards more integrated, multi-organ research, which is likely to grow.
*   **Open Ultrasound Data:** The Open Kidney Dataset is a significant step, and further development in open ultrasound data for kidneys could be crucial for accessible diagnostics.
*   **Proteomic Data Integration:** The Dataset from proteomic analysis of human liver, lung, kidney and intestine microsomes hints at increasing integration of multi-omics data with imaging.

## Possible Clinical Relevance

The identified datasets have significant potential for clinical applications, particularly in the advancement of diagnostic and prognostic tools for liver and kidney diseases, including cancers.

*   **Improved Diagnostic Accuracy:** Datasets with high-quality scans and annotations, such as the Duke Liver Dataset and those within the IDC, can train AI models to detect and classify lesions with greater accuracy and efficiency, potentially surpassing human capabilities in certain tasks.
*   **Enhanced Surgical Planning:** Accurate segmentation of organs and tumors, facilitated by datasets like LiMT and those used in reviews of AI-based segmentation, is critical for precise surgical planning in liver cancer and other hepatic interventions.
*   **Non-Invasive Disease Monitoring:** The development of AI tools trained on datasets like the Hyper and Multispectral Kidney Image Dataset could lead to more reliable non-invasive methods for monitoring kidney abnormalities and tumors.
*   **Personalized Medicine:** Integrating imaging data with clinical and multi-omics data, as seen in efforts like the MMIST ccRCC dataset, can pave the way for more personalized treatment strategies for kidney cancers.
*   **Streamlined Early Detection:** Datasets focusing on specific diseases like ccRCC (MMIST ccRCC) or liver nodules (as discussed in the CEUS study context) can accelerate the development of AI tools for earlier detection, which is crucial for improving patient outcomes.

## Sources

1.  Blood–Liver–Kidney Tri-Organ Imaging Dataset. Kaggle. (n.d.). Retrieved from 
2.  m-aryayi/Medical-Imaging-Datasets: Publicly available medical imaging datasets for research and analysis. GitHub. (n.d.). Retrieved from <a href="https://github.com/m-aryayi/Medical-Imaging-Datasets" target="_blank">https://github.com/m-aryayi/Medical-Imaging-Datasets</a>
3.  Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels. *PMC*. (n.d.). Retrieved from <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10418183/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10418183/</a>
4.  Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels. *Radiology: Artificial Intelligence*. (n.d.). Retrieved from 
5.  Dataset from proteomic analysis of human liver, lung, kidney and intestine microsomes. *Data in Brief*. (n.d.). Retrieved from 
6.  Hyper and Multispectral Kidney Image dataset. Kaggle. (n.d.). Retrieved from 
7.  MMIST ccRCC Dataset. (n.d.). Retrieved from 
8.  Top Liver Datasets and Models | Roboflow Universe. Roboflow. (n.d.). Retrieved from 
9.  Public Medical Image Datasets for Segmentation Foundation Models. (n.d.). Retrieved from 
10. GitHub - cradleai/LKS-Dataset: This is the official repo for the Liver Kidney Stomach dataset introduced in the paper: SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification. GitHub. (n.d.). Retrieved from <a href="https://github.com/cradleai/LKS-Dataset" target="_blank">https://github.com/cradleai/LKS-Dataset</a>
11. Imaging Data Commons | CRDC. NCI Imaging Data Commons. (n.d.). Retrieved from <a href="https://imaging.datacommons.cancer.gov/" target="_blank">https://imaging.datacommons.cancer.gov/</a>
12. Advances in Artificial Intelligence‐Based Liver‐Related Semantic Segmentation Techniques and Applications Using CT Imaging. *PMC*. (n.d.). Retrieved from <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10898680/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10898680/</a>
13. Liver - Datasets - PLCO - The Cancer Data Access System. National Cancer Institute. (n.d.). Retrieved from <a href="https://cdas.cancer.gov/plco/datasets/" target="_blank">https://cdas.cancer.gov/plco/datasets/</a>
14. Dataset Roundup - Noteworthy Datasets on Liver Diseases. Elucidata. (n.d.). Retrieved from <a href="https://elucidata.io/blog/dataset-roundup-noteworthy-datasets-on-liver-diseases" target="_blank">https://elucidata.io/blog/dataset-roundup-noteworthy-datasets-on-liver-diseases</a>
15. Enhanced Ultrasound Superior to MRI for Diagnosing Certain Liver and Kidney Tumors, According to New Studies | Imaging Technology News. Imaging Technology News. (n.d.). Retrieved from 
16. LiMT: a multi-task liver image benchmark dataset. *arXiv*. (n.d.). Retrieved from <a href="https://arxiv.org/abs/2311.13864" target="_blank">https://arxiv.org/abs/2311.13864</a>
17. Blood–Liver–Kidney Tri-Organ Imaging Dataset. PYCAD. (n.d.). Retrieved from 
18. Imaging-based deep learning in kidney diseases: recent progress and future prospects. *PMC*. (n.d.). Retrieved from <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10878803/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10878803/</a>
19. Open Kidney Dataset | kidneyUS. (n.d.). Retrieved from 