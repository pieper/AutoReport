# Research Report: Liver-Kidney-Data
*Generated: 2026-03-17 UTC*

## Executive Summary

This report details freely available datasets for liver and kidney research, focusing on those with large patient cohorts, high-quality scans, comprehensive annotations, and readily available clinical data. Particular attention has been given to datasets featuring well-described diseases like cancers and those with non-restrictive licenses (e.g., CC-BY). Recent advancements include the development of high-resolution 3D organ atlases and AI-generated annotations, significantly enhancing the utility of existing repositories like The Cancer Imaging Archive (TCIA).

## Key Announcements by Organization

### The Cancer Imaging Archive (TCIA) and NCI Imaging Data Commons (IDC)

*   **Expansion and Enhancement:** TCIA and IDC continue to be central hubs for cancer imaging data, boasting over 85 TB of data as of Spring 2025. They now include radiology, microscopy images, image-derived data (annotations, segmentations), and clinical data.
*   **AI-Assisted Annotations:** A significant advancement is the release of AI-generated annotations for various cancer types, including liver and kidney, which have been reviewed and corrected by radiologists. These enhanced datasets are integrated into the IDC, facilitating research and AI development.
*   **Diverse Cancer Datasets:** TCIA hosts numerous collections for various cancers, including kidney cancer (e.g., TCGA-KICH, TCGA-KIRC, TCGA-KIRP) and liver cancer (e.g., TCGA-LIHC), often with associated clinical and genomic data.

### Human Organ Atlas (HOA)

*   **High-Resolution 3D Organ Data:** The HOA, powered by Hierarchical Phase-Contrast Tomography (HiP-CT), now offers an expanded collection of high-quality 3D datasets for organs including the liver and kidneys. This resource provides near-cellular resolution and is accessible via a standard web browser, bridging the gap between radiology and histology.
*   **AI and Education Focus:** The HOA's large, high-quality 3D datasets are specifically highlighted as valuable for training advanced medical AI systems for disease detection and super-resolution analysis, as well as for medical education.

### Kaggle and UCI Machine Learning Repository

*   **Specialized Datasets:** Kaggle and the UCI Machine Learning Repository continue to host a variety of datasets, including the Kidney Disease Dataset with 43 diverse features, and specialized datasets like the TCGA Kidney Cancers Dataset (RNA-seq) from UCI.
*   **Segmentation Challenges:** Datasets like the Liver Tumor Segmentation Benchmark (LiTS) on Kaggle provide CT scans with masks for liver, tumors, and other abdominal organs, facilitating segmentation model development.

## Notable Papers and Datasets

*   **Open Kidney Dataset:** This dataset provides over 500 2D B-mode abdominal ultrasound images with fine-grained annotations for kidney segmentation, aimed at standardizing benchmarking and reducing interpretation efforts.
*   **Human Kidney Benchmark Dataset:** This dataset includes single-cell and single-nucleus RNA sequencing data from healthy kidneys and those with acute or chronic kidney disease, curated for model performance evaluation.
*   **LiMT (Liver Image Benchmark Dataset):** This dataset comprises 150 CT cases with annotations for four common liver lesion types, normal liver examples, and liver segmentation labels, serving as a valuable resource for liver research.
*   **Primary Liver Cancer CECT Imaging Dataset:** A large dataset with 278 liver cancer cases (HCC, ICC, cHCC-CCA) and 83 non-cancerous subjects, featuring full-phase 3D contrast-enhanced CT scans for diagnostic classification and lesion segmentation.
*   **LiverHccSeg:** This dataset offers multiphasic contrast-enhanced MRI scans with liver and HCC tumor segmentations from two radiologists, including an analysis of inter-rater agreement, valuable for validating segmentation algorithms.
*   **CT-ORG:** This dataset from TCIA contains 140 CT scans with 3D segmentations for multiple organs including the liver and kidneys, useful for multi-class organ segmentation algorithm development.

## What to Watch

*   **Imaging Data Commons (IDC) Expansion:** The IDC is continuously expanding its data holdings, with over 85 TB expected by Spring 2025. Researchers should monitor IDC for new collections and updates, particularly those with enhanced AI-generated annotations.
*   **Human Organ Atlas (HOA) Growth:** The HOA is a rapidly developing resource. Its focus on high-resolution 3D imaging suggests future releases will offer even more detailed anatomical data, crucial for AI training and novel research applications.
*   **AI Annotation Integration:** The trend of AI-assisted annotations being integrated into major repositories like TCIA/IDC is likely to continue, making datasets more robust and easier to utilize for complex AI tasks.
*   **Specialized Kidney Ultrasound Data:** The Open Kidney Dataset is a recent addition focusing on ultrasound, addressing a gap in this imaging modality for kidney research. Future updates or similar datasets could emerge.

## Possible Clinical Relevance

The datasets discussed hold significant potential for clinical translation across various areas:

*   **Early Disease Detection and Diagnosis:** Datasets with detailed annotations and clinical data, especially for cancers (liver and kidney), can accelerate the development of AI models for earlier and more accurate diagnoses.
*   **Treatment Planning and Monitoring:** High-resolution 3D datasets like the HOA and segmentation datasets (LiTS, LiverHccSeg) can aid in precise surgical planning, radiation therapy, and monitoring treatment response in liver and kidney diseases.
*   **Improved Radiomic Analysis:** Datasets with comprehensive imaging and clinical information, such as those from TCIA and the Primary Liver Cancer CECT Imaging Dataset, can power the development of radiomic models to predict disease progression, treatment efficacy, and patient outcomes.
*   **Advancements in Medical Education:** Interactive 3D atlases like the HOA offer novel ways for medical professionals and students to learn anatomy and pathology, potentially leading to better-trained clinicians.
*   **Kidney Disease Management:** Clinical datasets like the Kaggle Kidney Disease Dataset and the UKRR CKD/AKI clinical dataset provide essential resources for developing predictive models for chronic kidney disease progression and management.

## Sources

*   Open Kidney Dataset | kidneyUS. (n.d.). Retrieved from [https://kidneyus.github.io/open-kidney-dataset/](https://kidneyus.github.io/open-kidney-dataset/)
*   Kidney Disease Dataset. (n.d.). Kaggle. Retrieved from [https://www.kaggle.com/datasets/mansoormemon/kidney-disease-dataset](https://www.kaggle.com/datasets/mansoormemon/kidney-disease-dataset)
*   UCI Machine Learning Repository. (n.d.). Retrieved from [https://archive.ics.uci.edu/datasets](https://archive.ics.uci.edu/datasets)
*   CT-ORG - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from [https://www.cancerimagingarchive.net/ct-org/](https://www.cancerimagingarchive.net/ct-org/)
*   synthetic_medical_imaging_data. (n.d.). Kaggle. Retrieved from [https://www.kaggle.com/datasets/dynamo14324/syntheticmedicalimagingdata](https://www.kaggle.com/datasets/dynamo14324/syntheticmedicalimagingdata)
*   Imaging Data Commons - CRDC - National Cancer Institute. (n.d.). Retrieved from [https://imaging.datacommons.cancer.gov/](https://imaging.datacommons.cancer.gov/)
*   Clinical Ultrasound Image Repository - Registry of Open Data on AWS. (n.d.). Retrieved from [https://registry.opendata.aws/clinical-ultrasound-image-data/](https://registry.opendata.aws/clinical-ultrasound-image-data/)
*   m-aryayi/Medical-Imaging-Datasets. (n.d.). GitHub. Retrieved from [https://github.com/m-aryayi/Medical-Imaging-Datasets](https://github.com/m-aryayi/Medical-Imaging-Datasets)
*   Explore the human body in stunning, 3D detail with a new online tool | Popular Science. (2026, March 11). Popular Science. Retrieved from [https://www.popsci.com/science/human-organ-atlas-3d-imaging/](https://www.popsci.com/science/human-organ-atlas-3d-imaging/)
*   UKRR CKD/AKI clinical dataset - UK Kidney Association. (n.d.). Retrieved from [https://ukkidney.org/professionals/ukrr-ckd-aki-clinical-dataset](https://ukkidney.org/professionals/ukrr-ckd-aki-clinical-dataset)
*   Human Kidney Benchmark Dataset | v1.0 | Virtual Cells Platform. (n.d.). Retrieved from [https://virtualcells.org/datasets/human-kidney-benchmark](https://virtualcells.org/datasets/human-kidney-benchmark)
*   Multi-modality medical image dataset for medical image processing in Python lesson. (n.d.). Zenodo. Retrieved from [https://zenodo.org/record/7838838](https://zenodo.org/record/7838838)
*   Samples of LIDC/IDRI dataset: (a) Original CT image; (b) Corresponding ground-truth mask. (n.d.). ResearchGate. Retrieved from [https://www.researchgate.net/figure/Samples-of-LIDC-IDRI-dataset-a-Original-CT-image-b-Corresponding-ground-truth-mask_fig7_351278027](https://www.researchgate.net/figure/Samples-of-LIDC-IDRI-dataset-a-Original-CT-image-b-Corresponding-ground-truth-mask_fig7_351278027)
*   LiMT: a multi-task liver image benchmark dataset. (n.d.). arXiv. Retrieved from [https://arxiv.org/abs/2311.13578](https://arxiv.org/abs/2311.13578)
*   3D Atlas of Human Organs made available online. (2026, March 11). UCL News. Retrieved from [https://www.ucl.ac.uk/news/2026/mar/3d-atlas-human-organs-made-available-online](https://www.ucl.ac.uk/news/2026/mar/3d-atlas-human-organs-made-available-online)
*   Noteworthy Datasets on Liver Diseases. (2022, May 25). Elucidata. Retrieved from [https://www.elucidata.io/blog/noteworthy-datasets-on-liver-diseases](https://www.elucidata.io/blog/noteworthy-datasets-on-liver-diseases)
*   AI generated annotations for Breast, Brain, Liver, Lungs, and Prostate cancer collections in the National Cancer Institute Imaging Data Commons. (2025, July 21). ResearchGate. Retrieved from [https://www.researchgate.net/publication/382679878_AI_generated_annotations_for_Breast_Brain_Liver_Lungs_and_Prostate_cancer_collections_in_the_National_Cancer_Institute_Imaging_Data_Commons](https://www.researchgate.net/publication/382679878_AI_generated_annotations_for_Breast_Brain_Liver_Lungs_and_Prostate_cancer_collections_in_the_National_Cancer_Institute_Imaging_Data_Commons)
*   Dataset from proteomic analysis of human liver, lung, kidney and intestine microsomes. (n.d.). Data in Brief. Retrieved from [https://www.sciencedirect.com/science/article/pii/S235234091500077X](https://www.sciencedirect.com/science/article/pii/S235234091500077X)
*   'Google Earth' for human organs made available online | UCL News. (2026, March 13). UCL News. Retrieved from [https://www.ucl.ac.uk/news/2026/mar/-google-earth-human-organs-made-available-online](https://www.ucl.ac.uk/news/2026/mar/-google-earth-human-organs-made-available-online)
*   Deep Learning for Segmentation-based Hepatic Steatosis Detection on Open Data. (n.d.). arXiv. Retrieved from [https://arxiv.org/abs/2007.05829](https://arxiv.org/abs/2007.05829)
*   Top Liver Datasets and Models | Roboflow Universe. (n.d.). Roboflow. Retrieved from [https://universe.roboflow.com/search?q=liver](https://universe.roboflow.com/search?q=liver)
*   Liver Tumor Segmentation - Kaggle. (n.d.). Kaggle. Retrieved from [https://www.kaggle.com/datasets/andrewmvd/liver-tumor-segmentation](https://www.kaggle.com/datasets/andrewmvd/liver-tumor-segmentation)
*   LIDC-IDRI - Kaggle. (n.d.). Kaggle. Retrieved from [https://www.kaggle.com/datasets/kmydu/lidc-idri](https://www.kaggle.com/datasets/kmydu/lidc-idri)
*   Duke Liver Dataset: A Publicly Available Liver MRI Dataset with Liver Segmentation Masks and Series Labels - PMC. (2023, April 24). PubMed Central. Retrieved from [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10136172/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10136172/)
*   Browse Collections - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from [https://www.cancerimagingarchive.net/collections/](https://www.cancerimagingarchive.net/collections/)
*   LIDC-IDRI - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from [https://www.cancerimagingarchive.net/lidc-idri/](https://www.cancerimagingarchive.net/lidc-idri/)
*   AHEP0731-TUMOR-ANNOTATIONS - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from [https://www.cancerimagingarchive.net/ahep0731-tumor-annotations/](https://www.cancerimagingarchive.net/ahep0731-tumor-annotations/)
*   Primary Liver Cancer CECT Imaging Dataset. (2024, August 25). Kaggle. Retrieved from [https://www.kaggle.com/datasets/ljwa2323/primary-liver-cancer-cect-imaging-dataset](https://www.kaggle.com/datasets/ljwa2323/primary-liver-cancer-cect-imaging-dataset)
*   Characteristics and Features of the LIDC-IDRI Dataset for Lung Cancer Detection and Diagnosis. (n.d.). ResearchGate. Retrieved from [https://www.researchgate.net/publication/355688495_Characteristics_and_Features_of_the_LIDC-IDRI_Dataset_for_Lung_Cancer_Detection_and_Diagnosis](https://www.researchgate.net/publication/355688495_Characteristics_and_Features_of_the_LIDC-IDRI_Dataset_for_Lung_Cancer_Detection_and_Diagnosis)
*   Liver Cancer Multiclass Dataset - Kaggle. (n.d.). Kaggle. Retrieved from [https://www.kaggle.com/datasets/shreyacg11/liver-cancer-multiclass-dataset](https://www.kaggle.com/datasets/shreyacg11/liver-cancer-multiclass-dataset)
*   Public Medical Image Datasets for Segmentation Foundation Models. (n.d.). GitHub. Retrieved from [https://github.com/ycsn2013/Public-Medical-Image-Datasets-for-Segmentation-Foundation-Models](https://github.com/ycsn2013/Public-Medical-Image-Datasets-for-Segmentation-Foundation-Models)
*   A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC. (2023, October 10). PubMed Central. Retrieved from [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10567749/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10567749/)
*   Enhanced pulmonary nodule detection and classification using artificial intelligence on LIDC-IDRI data - ecancer. (2026, February 17). ecancer. Retrieved from [https://ecancer.org/en/journal/article/2748-enhanced-pulmonary-nodule-detection-and-classification-using-artificial-intelligence-on-lidc-idri-data](https://ecancer.org/en/journal/article/2748-enhanced-pulmonary-nodule-detection-and-classification-using-artificial-intelligence-on-lidc-idri-data)
*   A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma - MDPI. (2023, April 27). MDPI. Retrieved from [https://www.mdpi.com/2077-0383/14/9/1283](https://www.mdpi.com/2077-0383/14/9/1283)
*   20 Best Free Healthcare Datasets for ML in 2026. (2025, August 11). Unidata. Retrieved from [https://unidata.ai/blog/20-best-free-healthcare-datasets-for-ml-in-2026](https://unidata.ai/blog/20-best-free-healthcare-datasets-for-ml-in-2026)
*   LIDC-IDRI-DRR. (n.d.). The Cancer Imaging Archive (TCIA). Retrieved from [https://www.cancerimagingarchive.net/lidc-idri-drr/](https://www.cancerimagingarchive.net/lidc-idri-drr/)
*   B-MODE-AND-CEUS-LIVER - The Cancer Imaging Archive (TCIA). (n.d.). Retrieved from [https://www.cancerimagingarchive.net/b-mode-and-ceus-liver/](https://www.cancerimagingarchive.net/b-mode-and-ceus-liver/)
*   LIDC-IDRI - Kaggle. (n.d.). Kaggle. Retrieved from [https://www.kaggle.com/datasets/yegorvaskevich/lidc-idri-slices](https://www.kaggle.com/datasets/yegorvaskevich/lidc-idri-slices)
*   Community Liver Alliance | Global Awareness. Local Impact. (n.d.). Retrieved from [https://www.communityliveralliance.com/](https://www.communityliveralliance.com/)
*   Classification results on LIDC-IDRI dataset. | Download Scientific Diagram - ResearchGate. (n.d.). ResearchGate. Retrieved from [https://www.researchgate.net/figure/Classification-results-on-LIDC-IDRI-dataset_fig4_378537745](https://www.researchgate.net/figure/Classification-results-on-LIDC-IDRI-dataset_fig4_378537745)
*   UK Liver Alliance: Home. (n.d.). Retrieved from [https://www.ukliveralliance.org/](https://www.ukliveralliance.org/)
*   Lung Nodule Segmentation (LIDC-IDRI) — Preparing Data for Inference | by Hannah Do. (2025, September 15). Towards Data Science. Retrieved from [https://towardsdatascience.com/lung-nodule-segmentation-lidc-idri-preparing-data-for-inference-3b41843b83c1](https://towardsdatascience.com/lung-nodule-segmentation-lidc-idri-preparing-data-for-inference-3b41843b83c1)
*   Fatty Liver Alliance - NAFLD/MASLD and NASH/MASH Liver Patient Support in Canada, Fatty Liver Disease in Canada, Nonprofit, Nash and Nafld Liver Patient Support in Canada. (n.d.). Retrieved from [https://fattyliver.ca/](https://fattyliver.ca/)
*   datasets and codes for LiveFbr - GitHub. (n.d.). GitHub. Retrieved from [https://github.com/chentianlu/LiveFbr](https://github.com/chentianlu/LiveFbr)