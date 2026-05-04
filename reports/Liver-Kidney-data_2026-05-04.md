# Research Report: Liver-Kidney-Data
*Generated: 2026-05-04 UTC*

## Executive Summary

This report details freely available liver and kidney datasets for medical imaging research. The NCI Imaging Data Commons (IDC) stands out as a comprehensive resource, offering over 85 TB of cancer imaging data, predominantly under a permissive CC-BY license, and harmonized into DICOM format. For specific liver conditions, the LiverHccSeg dataset provides high-quality MRI scans with expert segmentations of the liver and HCC tumors. In kidney research, the KiTS (Kidney and Kidney Tumor Segmentation) dataset is a key resource for CT scans with detailed annotations of kidneys and tumors. While many datasets focus on specific organs or diseases, the increasing trend is towards multimodal data integration and the development of foundation models for broader applicability.

## Key Announcements, Grouped by Organization

### National Cancer Institute (NCI) / Cancer Research Data Commons (CRDC)

*   **NCI Imaging Data Commons (IDC):** This cloud-based repository is a major hub for publicly available cancer imaging data, exceeding 85 TB as of Spring 2025. It includes radiology, microscopy, and image-derived data (annotations, segmentations, quantitative measurements) along with clinical data. The majority of data is under a CC-BY license, allowing commercial reuse. IDC aggregates data from various sources including TCGA and TCIA.
*   **The Cancer Imaging Archive (TCIA):** As a node within the CRDC, TCIA hosts de-identified cancer imaging data accessible for public download. It partners with NCI's CRDC for enhanced access to many datasets.

### The Cancer Genome Atlas (TCGA)

*   TCGA data collections, often accessible through TCIA and now integrated into IDC, provide clinical images matched with subjects, enabling research into connecting cancer phenotypes to genotypes. This includes specific collections for kidney renal papillary cell carcinoma and kidney chromophobe.

### Duke University

*   **Duke Liver Dataset (DLDS):** This dataset comprises 2146 abdominal MRI series from 105 patients, with a majority having cirrhotic features. It includes 310 image series with manually segmented liver masks. DLDS is noted for its extensive imaging data and potential for training models for other abdominal organs.

### University of Minnesota

*   **Kidney and Kidney Tumor Segmentation Challenge (KiTS):** This dataset, particularly the KiTS19 training set, contains CT scans and manual semantic segmentations of kidneys and tumors for 210 patients. It is a valuable resource for advancing automatic 3D semantic segmentation techniques in kidney cancer research.

### Other Notable Datasets and Initiatives

*   **LiverHccSeg:** This dataset provides multiphasic contrast-enhanced MRI scans with liver and HCC tumor segmentations performed by two radiologists. It aims to foster collaboration and improve diagnosis and treatment of HCC.
*   **Medical Imaging Datasets (UCSF):** UCSF offers several publicly available datasets, including multimodal brain MRI scans for gliomas and datasets for renal masses, often with expert voxelwise segmentations and clinical data.
*   **Open Kidney Dataset:** This dataset contains over 500 2D B-mode abdominal ultrasound images with fine-grained polygon annotations for four kidney-related classes, intended for non-commercial research.
*   **Human Organ Atlas (HOA):** A new initiative using hierarchical phase-contrast tomography (HiP-CT) to visualize organs like the liver and kidneys in unprecedented detail down to the cellular level. While not a traditional "dataset" for AI training in the same way as CT/MRI, it represents a significant advancement in imaging detail.

## Notable Papers and Datasets

*   **LiverHccSeg:** A dataset providing multiphasic MRI scans with expert segmentations of the liver and HCC tumors, useful for evaluating segmentation algorithms and fostering collaborations.
*   **KiTS Dataset (Kidney and Kidney Tumor Segmentation):** This dataset, comprising CT scans and manual segmentations of kidneys and tumors, is crucial for research in automatic 3D semantic segmentation for kidney cancer.
*   **Duke Liver Dataset (DLDS):** Contains extensive abdominal MRI series with segmented liver masks, serving as a foundation for training models for liver segmentation and potentially other abdominal organs.
*   **NCI Imaging Data Commons (IDC):** A large-scale repository of over 85 TB of cancer imaging data, harmonized in DICOM format and largely under a CC-BY license, enabling broad research applications.
*   **Large-Scale CT Dataset for Liver Cancer:** Luo et al. created a comprehensive 3D CECT dataset of 278 primary liver cancer cases with four-phase imaging and expert annotations, addressing gaps in publicly available liver cancer imaging data.

## What to Watch

*   **NCI Imaging Data Commons (IDC) Growth:** IDC is continuously expanding, with its 85 TB of data as of Spring 2025 likely to grow further, incorporating more diverse cancer imaging datasets.
*   **Advancements in Annotation Quality and Standardization:** As highlighted by multiple sources, the quality and consistency of annotations remain critical for robust AI model training. Initiatives focusing on standardized annotation protocols and inter-rater agreement analysis (like in LiverHccSeg) will be important.
*   **Multimodal Data Integration:** The trend towards integrating imaging data with clinical, genomic, and other omics data is expected to accelerate. Datasets that facilitate this integration will become increasingly valuable for precision medicine.
*   **Human Organ Atlas (HOA):** While still in its early stages as a broadly accessible dataset for AI training, the HOA's high-resolution imaging of organs like the liver and kidneys could pave the way for new types of analysis and model development in the future.

## Possible Clinical Relevance

The availability of high-quality, well-annotated datasets for liver and kidney diseases is paramount for advancing AI-driven clinical applications.

*   **Improved Diagnosis and Segmentation:** Datasets like KiTS and LiverHccSeg directly support the development of AI algorithms for accurate tumor and organ segmentation, which is crucial for surgical planning, treatment monitoring, and early detection of cancers.
*   **Enhanced Precision Medicine:** Integrating imaging data with clinical and genomic information, as facilitated by resources like IDC and TCGA, allows for more personalized treatment strategies. This can lead to better prediction of disease progression and response to therapy.
*   **Accelerated Drug Development:** Comprehensive imaging datasets can aid pharmaceutical companies in evaluating drug efficacy and optimizing clinical trials by providing objective, quantitative measures of disease response.
*   **Reduced Inter-Observer Variability:** Standardized datasets and robust annotation processes help in developing AI models that can offer consistent interpretations, reducing the variability often seen between human experts.
*   **Benchmarking and Validation:** Freely available datasets enable researchers and developers to rigorously benchmark and validate AI algorithms, ensuring their reliability and generalizability before clinical deployment.

## Sources

*  
*  
*  
*  
*  
*  
*  
*  
*  
*  
*  
*  