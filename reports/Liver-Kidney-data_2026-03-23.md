# Research Report: Liver-Kidney-Data
*Generated: 2026-03-23 UTC*

# Executive Summary

This report outlines the best freely available liver and kidney datasets for research, focusing on those with a significant number of patients and high-quality scans, comprehensive annotations, and accessible clinical data. Datasets from The Cancer Imaging Archive (TCIA) and the NCI Imaging Data Commons (IDC) are highlighted as primary resources, offering extensive collections of cancer imaging data, including liver and kidney conditions. Recent updates include the expansion of IDC with over 85 TB of data as of Spring 2025, and ongoing curation of specialized datasets like the LiverHccSeg. These resources predominantly utilize non-restrictive licenses, such as CC BY, facilitating broad research use.

## Key Announcements and Resources

### NCI Imaging Data Commons (IDC) and The Cancer Imaging Archive (TCIA)

*   **NCI Imaging Data Commons (IDC):** This cloud-based repository is a significant node within the NCI Cancer Research Data Commons (CRDC). As of Spring 2025, it contains over 85 TB of data, including radiology, digital pathology, and slide microscopy images, along with annotations, segmentations, and clinical data. IDC harmonizes data from various sources like TCGA and TCIA, offering free and open access with a predominantly CC BY license, suitable for commercial use.
*   **The Cancer Imaging Archive (TCIA):** TCIA is a large, de-identified archive of medical images specifically for cancer research. It hosts numerous collections, including those focused on liver and kidney cancers, often providing segmentations and associated clinical data. TCIA partners with the NCI's CRDC for enhanced data access.

### Specialized Liver Datasets

*   **Duke Liver Dataset (DLDS):** This dataset comprises over 2000 anonymized MRI series from 105 patients with cirrhotic features, including 310 series with manual liver segmentation masks. It is suitable for training models for liver segmentation and series classification and can be combined with other datasets like CHAOS or LiTS.
*   **LiverHccSeg:** This dataset focuses on hepatocellular carcinoma (HCC) and provides multiphasic MRI scans with manual segmentations of the liver and tumors by two radiologists. It includes an analysis of inter-rater agreement, offering valuable data for validating segmentation algorithms.
*   **LiMT (Liver Multi-task):** A recently introduced dataset featuring 3D CT liver images from 150 cases annotated for anatomy and lesion types. It aims to support multiple tasks, including segmentation, classification, and detection, addressing a gap in existing liver-related datasets.
*   **CancerLivER:** While not an imaging dataset, CancerLivER is a valuable resource for liver cancer research, integrating 115 datasets with gene expression profiles for 9611 samples and 594 biomarkers. It is available with a CC-BY 4.0 license.
*   **Liver Tumor Segmentation:** This Kaggle dataset, derived from the LiTS17 challenge, offers 130 CT scans for liver and tumor lesion segmentation.
*   **Annotated Ultrasound Liver Images:** A Kaggle dataset containing annotated ultrasound images of the liver with outlines of the liver and masses, classified into benign, malignant, and normal cases, useful for computer vision models.
*   **Large-Scale CT Dataset for Liver Cancer:** A new dataset (as of September 2025) of 278 patients with primary liver cancer, featuring four-phase contrast-enhanced CT scans and expert lesion annotations, designed to support AI diagnostics.

### Specialized Kidney Datasets

*   **CT-ORG:** This dataset includes 140 CT scans with 3D segmentations of organs like the lungs, bones, liver, and kidneys. It is beneficial for training organ segmentation algorithms across varied imaging conditions.
*   **C4KC-KiTS (Kidney and Kidney Tumor Segmentation Challenge):** This dataset contains CT scans and manual segmentations of kidneys and kidney tumors from 210 patients, collected during routine care. It has been updated to ensure better compatibility with DICOM tools.
*   **Open Kidney Dataset:** This dataset provides over 500 2D B-mode abdominal ultrasound images with fine-grained polygon annotations for four kidney-related classes. It is available for non-commercial use under a CC BY-NC-SA license.
*   **TotalSegmentator MRI:** This dataset, while not exclusively for kidneys, includes segmentations of 80 anatomical structures, relevant for organ volumetry and disease characterization, and has demonstrated strong performance in segmenting kidneys in MRI scans.

## Notable Papers

*   **NCI Imaging Data Commons (IDC):** IDC ingests and harmonizes data from numerous sources, including TCGA, TCIA, CPTAC, CCDI, HTAN, LIDC, QIN, VHP, and NLST, making it a comprehensive resource for cancer research.
*   **CT-ORG:** This dataset provides CT volumes with multiple organ segmentations, including liver and kidneys, and is ideal for training and evaluating organ segmentation algorithms under diverse imaging conditions.
*   **C4KC-KiTS:** The Kidney and Kidney Tumor Segmentation Challenge dataset offers CT scans and manual segmentations of kidneys and tumors, aiding in the development of 3D semantic segmentation techniques for kidney cancer.
*   **Duke Liver Dataset (DLDS):** This dataset is well-suited for training series classification models or liver segmentation models for abdominal MRI and can be used with transfer learning for segmenting other abdominal organs like the spleen and kidneys.
*   **TCGA-KIRC:** The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma collection provides clinical images matched with TCGA clinical, genetic, and pathological data for correlations between genotype, phenotype, and patient outcomes.
*   **LiMT:** This paper introduces a multi-task liver CT dataset with annotations for anatomy and lesion types, addressing the lack of publicly available datasets supporting segmentation, classification, and detection tasks for liver abnormalities.
*   **Large-Scale CT Dataset for Liver Cancer:** This recent dataset offers multiphase, expert-annotated CECT images for primary liver cancer, supporting the development of AI models for classification and segmentation of liver cancer subtypes.
*   **LiverHccSeg:** This dataset provides liver and HCC tumor segmentations on multiphasic contrast-enhanced MRI, along with inter-rater agreement analysis, crucial for rigorous validation of automated segmentation algorithms.
*   **TotalSegmentator MRI:** This work presents a robust MRI segmentation model for multiple anatomical structures, including kidneys, demonstrating high performance and outperforming other publicly available models on external datasets.

## What to Watch

*   **NCI Imaging Data Commons (IDC):** Continues to expand its data repository, with over 85 TB of data as of Spring 2025, indicating ongoing additions and improvements. Its cloud-based nature and harmonized data formats are key for future large-scale AI development.
*   **Updates to TCIA Collections:** TCIA regularly updates existing collections and adds new ones. Researchers should monitor TCIA for new liver and kidney-specific datasets that may emerge, especially those related to emerging cancer research areas or specific imaging modalities.
*   **Emerging Datasets:** Keep an eye on newly published datasets or challenges in medical imaging, such as those frequently appearing on platforms like Kaggle or through research initiatives like the ones described in recent publications. The continuous development of AI in medicine suggests a trend towards more specialized and annotated datasets.

## Possible Clinical Relevance

The datasets described offer significant potential for clinical relevance by enabling the development and validation of advanced AI tools for medical diagnosis and treatment planning.

*   **Improved Diagnostic Accuracy:** High-quality annotated datasets, such as those from TCIA and IDC, are crucial for training AI models that can detect and classify liver and kidney diseases, including cancers, with greater accuracy and speed than manual methods alone. This can lead to earlier diagnosis and intervention.
*   **Enhanced Treatment Planning:** Datasets with detailed segmentations of organs and tumors (e.g., C4KC-KiTS, LiverHccSeg, LiTS) are vital for developing AI systems that can precisely delineate treatment areas for surgery, radiation therapy, or chemotherapy, potentially personalizing treatment strategies.
*   **Quantitative Imaging Biomarkers:** The availability of diverse imaging data with associated clinical and genomic information (e.g., TCGA-KIRC) can facilitate the discovery of novel imaging biomarkers for disease prognosis, treatment response prediction, and patient stratification.
*   **Automation of Repetitive Tasks:** Datasets with extensive annotations enable the development of AI tools to automate tedious tasks like organ segmentation (e.g., CT-ORG, TotalSegmentator MRI) or lesion identification, freeing up clinician time for more complex patient care.
*   **Advancements in Surgical Planning:** Datasets featuring detailed anatomical and pathological information, such as those from the Duke Liver Dataset or LiverHccSeg, can support the creation of AI-powered tools for pre-operative planning, simulation, and even intra-operative guidance.

## Sources

*   NCI Imaging Data Commons (IDC). https://imaging.datacommons.cancer.gov/
*   CT-ORG. https://www.cancerimagingarchive.net/collections/ct-org/
*   C4KC-KITS. https://www.cancerimagingarchive.net/collections/c4kc-kits/
*   m-aryayi/Medical-Imaging-Datasets: Publicly available medical imaging datasets for research and analysis. https://github.com/m-aryayi/Medical-Imaging-Datasets
*   TCGA-KIRC. https://www.cancerimagingarchive.net/collections/tcga-kirc/
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels. 
*   Browse Collections - The Cancer Imaging Archive (TCIA). https://www.cancerimagingarchive.net/collections/
*   LiMT: a multi-task liver image benchmark dataset. https://arxiv.org/abs/2401.07546
*   TCIA Dataset: Medical imaging for cancer research. 
*   General Dataset (TCIA) - Kaggle. 
*   Public Medical Image Datasets for Segmentation Foundation Models. 
*   LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis. 
*   CancerLivER: a database of liver cancer gene expression resources and biomarkers. 
*   Large-Scale CT Dataset with Complete Phase Coverage Advances Primary Liver Cancer AI Diagnostics. 
*   Open Kidney Dataset. 
*   22 Free and Open Healthcare Datasets for Machine Learning and AI Development in 2025. 
*   Annotated Ultrasound Liver images Dataset - Kaggle. 
*   18 Open Healthcare Datasets — 2025 Update. https://www.datasciencecentral.com/18-open-healthcare-datasets-2025-update/
*   Shared Datasets | Center for Artificial Intelligence in Medicine & Imaging. 
*   20 Best Free Healthcare Datasets for ML in 2026 - Unidata. 
*   20 Free Life Sciences, Healthcare, and Medical Datasets for Machine Learning - iMerit. https://imerit.net/blog/20-free-life-sciences-healthcare-and-medical-datasets-for-machine-learning/
*   Datasets | CRDC - Cancer Research Data Commons. 
*   Liver Tumor Segmentation - Kaggle. https://www.kaggle.com/datasets/andrewmvd/liver-tumor-segmentation
*   TotalSegmentator MRI: Robust Sequence-independent Segmentation of Multiple Anatomic Structures in MRI. 
*   Liver Disease - Research - NIDDK. 
*   NIH Strides - Registry of Open Data on AWS. 
*   Liver Cancer Multiclass Dataset - Kaggle. 