# Research Report: Liver-Kidney-Data
*Generated: 2026-11-09 UTC*

## Executive Summary

This report details the best currently available freely accessible datasets for liver and kidney research, with a focus on conditions like cancer. Key datasets include those from The Cancer Imaging Archive (TCIA), Kaggle, and Grand Challenges, offering varying numbers of patient scans and levels of annotation. While many datasets provide high-quality imaging data, the availability of comprehensive clinical data and non-restrictive licenses can vary. Recent additions and ongoing efforts are expanding the availability of multimodal data and patient cohorts, particularly for liver cancer.

## Key Announcements, Grouped by Organization

### The Cancer Imaging Archive (TCIA)

*   **CT-ORG Dataset:** This dataset, updated as of January 9, 2020, contains 140 CT scans with segmentations for multiple organs, including the liver and kidneys. It specifically includes patients with liver lesions (benign and malignant) and metastatic disease, making it highly relevant for cancer research. The dataset is split into training and testing sets and offers a variety of imaging conditions.
*   **TCGA-KIRC (Kidney Renal Clear Cell Carcinoma Collection):** This collection links clinical and genomic data from The Cancer Genome Atlas (TCGA) with radiological data stored on TCIA, focusing on kidney cancer. It provides matched TCGA patient identifiers for researchers to explore correlations between genotype, radiological phenotype, and patient outcomes.
*   **HCC-TACE-Seg Dataset:** Part of the TCIA database, this dataset focuses on hepatocellular carcinoma (HCC) and includes pre- and post-treatment CT data from 105 patients. It features semi-automatically performed segmentations of the liver, tumors, and vessels, with manual clinical corrections, enabling prediction of treatment response.

### Kaggle

*   **Blood–Liver–Kidney Tri-Organ Imaging Dataset:** This dataset provides comprehensive histopathological and hematological image data. It includes separate datasets for blood cell detection, liver tissue analysis (classification of hepatocytes, sinusoids, portal triads), and kidney tissue analysis.
*   **Liver Cancer Multiclass Dataset:** This dataset comprises 11,002 MRI images for multi-class liver cancer classification, covering categories such as Angiosarcoma, Cholangiocarcinoma, and healthy liver.
*   **Liver Disease Patient Dataset 30K train data:** This dataset contains clinical and laboratory data for liver disease prediction, including variables like age, gender, bilirubin levels, and liver enzyme levels.

### Grand Challenges

*   **CHAOS (Combined Healthy Abdominal Organs Segmentation):** While primarily focused on healthy organs, this dataset includes abdominal CT images of potential liver donors. It notes that participants can include other liver datasets like SLIVER for training. The dataset contains challenges such as partial volume effects and atypical liver shapes.
*   **FLARE21 (Fully-supervised Localization And Reconstruction Ensemble):** This dataset includes annotations for four organs: liver, kidney, spleen, and pancreas. It is partly adapted from other datasets like MSD (Liver, Spleen, Pancreas) and KiTS under their respective license permissions. The license for FLARE21 is CC-BY-NC-SA.

### Other Notable Sources

*   **Blood–Liver–Kidney Tri-Organ Imaging Dataset (Mendeley Data):** Similar to the Kaggle version, this dataset is described as a multi-modal medical imaging dataset for object detection and tissue classification, focusing on blood cell detection, liver tissue analysis, and kidney tissue analysis.
*   **Liver Kidney Stomach (LKS) Dataset (GitHub/COVE):** This dataset, introduced in a CVPR2020 paper, consists of immunofluorescence whole slide images (WSI) used in the clinical investigation of autoimmune liver disease. It contains raw TIF images for researchers to explore alternative preprocessing methods.
*   **Duke Liver Dataset (DLDS):** This dataset provides a large collection of anonymized MRI image series (over 2000) from 105 subjects, primarily acquired for identifying hepatic cirrhosis. It includes manually segmented liver masks and is suitable for training algorithms for series identification and liver segmentation.
*   **CirrMRI600+:** A comprehensive dataset of 628 high-resolution abdominal MRI scans with expert-validated segmentation labels specifically for cirrhotic livers. It includes demographic information, clinical parameters, and histopathological validation.
*   **Open Kidney Dataset:** This dataset offers over 500 2D B-mode abdominal ultrasound images with fine-grained polygon annotations for four classes, intended for non-commercial use. It aims to address the lack of open ultrasound data for kidney research.
*   **Curvas Dataset:** This dataset includes 90 CT images with annotations for pancreas, kidney, and liver, featuring annotations from three different experts. The data usage agreement is CC BY-NC.

## Notable Papers

*   **"CT-ORG | CT volumes with multiple organ segmentations"** describes a dataset of 140 CT scans with segmentations for lungs, bones, liver, kidneys, and bladder, including patients with liver lesions.
*   **"Blood–Liver–Kidney Tri-Organ Imaging Dataset"** on Kaggle offers comprehensive histopathological and hematological image data, including separate datasets for blood cell detection, liver tissue analysis, and kidney tissue analysis.
*   **"LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis"** presents a dataset with manual whole liver and tumor segmentations for patients with hepatocellular carcinoma (HCC), with segmentations performed by two radiologists.
*   **"SOS: Selective Objective Switch for Rapid Immunofluorescence Whole Slide Image Classification"** introduced the Liver Kidney Stomach (LKS) dataset, which comprises immunofluorescence whole slide images for investigating autoimmune liver disease.
*   **"AbdomenCT-1K: Is Abdominal Organ Segmentation A Solved Problem?"** describes a dataset with annotations for liver, kidney, spleen, and pancreas, partly adapted from existing datasets.

## What to Watch

*   **Continued Growth of Multimodal Datasets:** There is a clear trend towards combining imaging data with genomic and clinical information, as seen in TCGA-KIRC and efforts to integrate data from multiple sources.
*   **Focus on Specific Diseases:** Datasets like LiverHccSeg and HCC-TACE-Seg highlight a growing need for specialized datasets focusing on specific liver pathologies, such as HCC.
*   **Advancements in Annotation Quality:** Datasets with annotations from multiple expert raters, like Curvas, are becoming more common, providing better insights into inter-rater variability.
*   **Expansion of Ultrasound Data:** The Open Kidney Dataset is a significant step towards addressing the scarcity of open ultrasound data for kidney research, an area that may see more development.
*   **Licensing Clarity:** While many datasets offer free access for research, the specificity of licenses (e.g., CC-BY-NC vs. CC-BY) remains an important factor for usability. Non-commercial licenses like CC-BY-NC-SA (used in FLARE21) limit commercial applications.

## Possible Clinical Relevance

The datasets described offer significant potential for clinical relevance across several areas:

*   **Improved Cancer Diagnosis and Treatment:** Datasets like CT-ORG and HCC-TACE-Seg, which include liver cancer and associated imaging, can be instrumental in developing AI models for earlier cancer detection, more accurate tumor segmentation, and prediction of treatment response.
*   **Enhanced Organ Segmentation:** Datasets with detailed organ annotations (liver, kidney) from various imaging modalities (CT, MRI) are crucial for developing robust segmentation algorithms. These algorithms can assist in surgical planning, radiation therapy, and automated quantification of organ volumes or disease burden.
*   **Understanding and Predicting Liver and Kidney Diseases:** Datasets containing clinical and laboratory data, such as the Liver Disease Patient Dataset or the Kidney Disease Dataset, can be used to build predictive models for disease progression, patient stratification, and personalized treatment strategies.
*   **Cirrhosis and Fibrosis Research:** Specialized datasets like CirrMRI600+ focusing on cirrhotic livers are vital for advancing research into the diagnosis, staging, and management of liver fibrosis and cirrhosis.
*   **Rare Disease Characterization:** While not as prevalent, datasets focusing on specific subtypes of cancer or rare liver/kidney conditions can contribute to a better understanding and development of targeted therapies for these less common diseases.

## Sources

 Blood–Liver–Kidney Tri-Organ Imaging Dataset. (n.d.). Kaggle. Retrieved from 
 CHAOS. (n.d.). Grand Challenge. Retrieved from 
 CT-ORG. (2020, January 9). The Cancer Imaging Archive (TCIA). Retrieved from https://www.cancerimagingarchive.net/ct-org/
 Blood–Liver–Kidney Tri-Organ Imaging Dataset. (2026, September 15). Mendeley Data. Retrieved from https://data.mendeley.com/datasets/j74z83h9xv/1
 cradleai/LKS-Dataset: Liver Kidney Stomach Dataset. (n.d.). GitHub. Retrieved from https://github.com/cradleai/LKS-Dataset
 Liver Datasets. (n.d.). PLCO - The Cancer Data Access System. Retrieved from https://cdas.cancer.gov/plco/datasets/
 FLARE21. (n.d.). Grand Challenge. Retrieved from 
 Liver cancer Datasets. (n.d.). BioGPS. Retrieved from https://biogps.org/dataset/tag/liver-cancer
 Dataset from proteomic analysis of human liver, lung, kidney and intestine microsomes. (n.d.). ScienceDirect. Retrieved from 
 Liver Hepatocellular Carcinoma (TCGA, PanCancer Atlas). (n.d.). MSK Data Catalog. Retrieved from 
 Liver Cancer Multiclass Dataset. (n.d.). Kaggle. Retrieved from 
 Top Liver Datasets and Models. (n.d.). Roboflow Universe. Retrieved from 
 CancerLivER: a database of liver cancer gene expression resources and biomarkers. (2020, March 7). PMC. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7056067/
 Liver Disease Patient Dataset 30K train data. (n.d.). Kaggle. Retrieved from 
 LiverHccSeg: A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis. (2023, October 10). PMC. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10569565/
 Kidney Disease Dataset. (n.d.). Kaggle. Retrieved from 
 Liver Disease Prediction Dataset. (n.d.). Kaggle. Retrieved from 
 Obstacles from the CT dataset and deficiencies from the current ... (n.d.). Retrieved from 
 Open Kidney Dataset. (n.d.). kidneyUS. Retrieved from 
 Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels. (2026, August 5). ResearchGate. Retrieved from 
 TCIA Dataset: Medical imaging for cancer research. (n.d.). Innovatiana. Retrieved from 
 HCC-TACE-Seg.md. (n.d.). GitHub. Retrieved from 
 The Liver Kidney Stomach Dataset. (2020, August 24). COVE - Computer Vision Exchange. Retrieved from 
 Kaggle dataset C.T. scan liver images. (n.d.). ResearchGate. Retrieved from 
 Curvas Dataset. (n.d.). Retrieved from https://zenodo.org/records/12687192
 TCGA-KIRC. (n.d.). The Cancer Genome Atlas. Retrieved from  কো/kidney-renal-clear-cell-carcinoma
 NIAID Data Discovery Portal | Duke Liver Dataset (MRI) v2. (2020, October 28). NIAID. Retrieved from 
 A preclinical CT and MRI Liver Imaging Dataset with Anatomical, Functional and Segmentation Data. (n.d.). PMC. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10765650/