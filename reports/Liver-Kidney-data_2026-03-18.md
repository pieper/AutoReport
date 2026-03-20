# Research Report: Liver-Kidney-Data
*Generated: 2026-03-18 UTC*

## Executive Summary

This report synthesizes information on freely available liver and kidney datasets, focusing on those with well-described diseases like cancers. Key datasets identified include the KiTS19 and KiTS23 challenges for kidney tumors, and the ATLAS dataset and TCGA-LIHC for liver cancer. These datasets vary in size, scan quality, and annotation depth, with a general trend towards increasing availability of clinical data and advanced imaging modalities. Notably, there's a growing emphasis on multi-center, multi-phase imaging and the integration of genomic and clinical data, facilitated by platforms like The Cancer Imaging Archive (TCIA) and the NCI Imaging Data Commons (IDC). Recent developments highlight the expansion of the Human Organ Atlas, offering high-resolution 3D organ datasets that can aid AI model training.

## Key Announcements and Datasets by Organization

### The Cancer Imaging Archive (TCIA)

TCIA serves as a crucial repository for cancer-related medical imaging data, including significant collections for liver and kidney diseases.

*   **TCGA-KIRC (The Cancer Genome Atlas Kidney Renal Clear Cell Carcinoma):** Provides CT and MRI scans for kidney cancer patients, linked with genomic and clinical data. It contains 267 subjects, 439 studies, and over 192,000 images, licensed under CC BY 3.0.
*   **TCGA-LIHC (The Cancer Genome Atlas Liver Hepatocellular Carcinoma):** Offers CT and MRI scans for liver cancer patients, also integrated with genomic and clinical data. This collection includes 97 subjects, 237 studies, and over 125,000 images, licensed under CC BY 3.0.
*   **C4KC-KiTS (Kidney and Kidney Tumor Segmentation Challenge):** A foundational dataset for kidney tumor segmentation, containing CT scans and manual segmentations for 210 patients. It is licensed under CC BY 3.0.
*   **Colorectal-Liver-Metastases:** This collection provides CT scans and segmentation objects for 197 patients with colorectal liver metastases, including detailed segmentation of liver, tumors, and vessels.

### NCI Imaging Data Commons (IDC)

The IDC, part of the NCI Cancer Research Data Commons, aggregates and harmonizes cancer imaging data from various sources, emphasizing open access and commercial-friendly licenses.

*   **Harmonized Collections:** IDC ingests data from TCIA, TCGA, and other initiatives, harmonizing it into DICOM format. Over 95% of the data is under a CC BY license, promoting commercial reuse.
*   **Expanding Data:** As of Spring 2025, IDC houses over 85 TB of data, including radiology, microscopy images, annotations, segmentations, and clinical data, with ongoing expansion.

### Kidney and Kidney Tumor Segmentation (KiTS) Challenges

The KiTS challenges have generated significant datasets for kidney tumor research.

*   **KiTS19:** This dataset, originating from the 2019 challenge, comprises CT scans and manual segmentations for 210 kidney cancer patients. It is available under a CC BY-NC-SA license.
*   **KiTS23:** The latest iteration of the challenge, featuring an expanded training set of 489 cases and a new test set of 110 cases. It includes kidney tumors and cysts segmentation and is licensed under CC BY-NC-SA.

### ATLAS (A Tumour and Liver Automatic Segmentation) Dataset

*   **HCC CE-MRI Data:** This dataset provides contrast-enhanced MRI scans for 90 patients with unresectable Hepatocellular Carcinoma (HCC), along with liver and tumor segmentation masks. It is noted as the first public dataset of its kind for HCC CE-MRI.

### Human Organ Atlas (HOA)

A recent initiative providing high-resolution 3D datasets of human organs.

*   **Expanded Access:** Building on an initial 2023 release, the HOA now offers access to detailed 3D scans of 56 organs, including the liver and kidneys. It utilizes Hierarchical Phase-Contrast Tomography (HiP-CT) for near-cellular resolution imaging.
*   **AI Training Potential:** The high-quality, large-scale 3D datasets are suitable for training advanced medical AI systems for disease detection and analysis.

### MedMNIST

A collection of standardized biomedical image datasets designed for machine learning.

*   **Lightweight Datasets:** MedMNIST offers various 2D and 3D datasets, including those relevant to abdominal organs. Most are licensed under CC BY 4.0, facilitating educational and research use.

## Notable Papers and Datasets

*   **KiTS19 Challenge:** Focused on accelerating progress in automatic 3D semantic segmentation of kidneys and kidney tumors using CT scans. The winning team achieved a composite score of 0.912.
*   **ATLAS Dataset:** Presented as the first public dataset providing contrast-enhanced MRI of HCC with annotations, aiming to facilitate automated tools for liver and tumor segmentation in treatment planning.
*   **Primary Liver Cancer CECT Imaging Dataset:** A large dataset from a single institution with 278 liver cancer cases (HCC, ICC, cHCC-CCA) and 83 non-cancer subjects, featuring full-phase CECT images to improve diagnostic classification and lesion segmentation.
*   **LiverHccSeg:** Provides a publicly available resource with multiphasic contrast-enhanced MRI scans and manual segmentations by two radiologists for liver and HCC tumor segmentation tasks, facilitating algorithm validation.
*   **Duke Liver Dataset (DLDS):** Contains abdominal MRI series from 105 patients with liver cirrhosis, including manually segmented liver masks, suitable for series classification and liver segmentation models.
*   **Human Organ Atlas (HOA):** Offers high-resolution 3D datasets of organs like the liver and kidneys, created using Hierarchical Phase-Contrast Tomography (HiP-CT), enabling detailed anatomical exploration and AI model training.
*   **KidneyNeXt:** Proposed a lightweight CNN architecture for multi-class renal tumor classification in CT imaging, achieving high accuracy on several datasets, including the Kaggle CT KIDNEY dataset.
*   **TCGA-KIRC and TCGA-LIHC:** These collections within TCIA provide matched imaging, clinical, and genomic data for kidney and liver cancer, respectively, supporting research into cancer phenotypes and genotypes.
*   **LiTS (Liver Tumor Segmentation Benchmark):** Contains 130 CT scans with masks for liver, tumor, bone, arteries, and kidneys, facilitating slice-based segmentation.
*   **MedMNIST:** A large-scale collection of standardized biomedical images for machine learning, including datasets relevant to abdominal organs, licensed under CC BY 4.0.

## What to Watch

*   **Ongoing Expansion of Imaging Data Commons (IDC):** The IDC continues to grow, with over 85 TB of data and a strong commitment to open-access and commercially permissive licenses. Future additions of harmonized data from various NCI initiatives are expected.
*   **Human Organ Atlas (HOA) Updates:** The HOA, launched with an expanded collection in March 2026, is expected to continuously add new data, providing increasingly comprehensive 3D organ datasets for research and education.
*   **Future KiTS Challenges:** The Kidney Tumor Segmentation challenges have a history of recurring iterations (2019, 2021, 2023). Future challenges are likely to continue pushing the boundaries of kidney tumor segmentation.
*   **Development of Multi-Modal and Multi-Organ Datasets:** There's a growing trend towards datasets that integrate various imaging modalities (CT, MRI, Ultrasound) and encompass multiple organs, providing a more holistic view for AI development. Datasets like the "Blood–Liver–Kidney Tri-Organ Imaging Dataset" hint at this direction.

## Possible Clinical Relevance

The datasets discussed hold significant clinical relevance for advancing diagnostic and therapeutic capabilities in liver and kidney diseases:

*   **Improved Cancer Detection and Diagnosis:** High-quality annotated datasets are crucial for training AI models to detect and classify liver and kidney cancers with greater accuracy and speed. This can lead to earlier diagnosis and better patient outcomes, especially for subtle or early-stage lesions.
*   **Enhanced Treatment Planning and Personalization:** Detailed segmentations of tumors and organs allow for more precise surgical planning, radiation therapy, and personalized treatment strategies. Datasets with associated clinical and genomic information can help identify biomarkers for predicting treatment response and prognosis.
*   **Development of Automated Segmentation Tools:** The availability of datasets with expert annotations accelerates the development of automated segmentation tools, reducing the time and variability associated with manual segmentation by radiologists and clinicians.
*   **Advancements in Radiomics and Radiogenomics:** Datasets with rich imaging and clinical data enable radiomic analysis, which extracts quantitative features from medical images to correlate with clinical outcomes, genetics, and treatment response. This can lead to a deeper understanding of disease biology and the development of novel therapeutic targets.
*   **Medical Education and Training:** High-resolution 3D atlases, such as the Human Organ Atlas, provide invaluable resources for medical education, allowing students and practitioners to explore complex anatomy and pathology in an interactive and detailed manner.
*   **Bridging Data Gaps:** Datasets that include diverse patient populations and varied imaging protocols are essential for developing AI models that are robust and generalizable to real-world clinical settings, thus helping to mitigate biases in AI-driven healthcare.

## Sources

 Data from the training set of the 2019 Kidney and Kidney Tumor Segmentation Challenge (C4KC-KiTS) - Cancer Imaging Archive Wiki. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRkgKCtjt3I98Lvfu8GGskA8_255ThMKhJ62Mv4HVVdavjT1UMp7fx2I9nHLQj_pv7dOrrH5x8d2-vexDwSFximMuV85XlHxeGYW-qUa70Wg8VhmGXnPQeigoEJeyARIQn5IrGIL0-2IE=
 A Tumour and Liver Automatic Segmentation (ATLAS) Dataset on Contrast-Enhanced Magnetic Resonance Imaging for Hepatocellular Carcinoma - MDPI. 
 Challenge Data - KiTS19. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtq-bX5Y6xo6BMY-2dyN4ZZP_jYrn-rQF-hr3qkv1jTfLuu_Unx_ZSobbwPtQQouvaKn6ANwpxSyPQfqmaxEqo9uQ6ygQF288J6nkDou6UU6Jk26b76geeXcu-na7M_QJmZF8=
 Primary Liver Cancer CECT Imaging Dataset. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKiyRbRxGvH2ZFv4OZptwuwyknAxiISO2algZd6Ris5P7oEVMeO9h7POF6cxEJBP1HI9DwGHPIWQiuMgeS089xuS2jyNktryW2t-_frVEwxIXCB5DrDviulZzIjeXKaZxU7CusU8VtELiIS62DUH-UQaM68zqcbShgy0jyhc-94cb4w68=
 Liver Cancer Multiclass Dataset - Kaggle. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUPiq2hPkyKUbe0wjVl8HetWFWF7FMprdF2s9J-vv-iocSDriLHYTWUoRcB1nW4mSMGNaP5rqEQAXcKXm76fvpo_X56Vxu-xdRA3lSTtDVWTaIVuONzZU5N6uWQxhit7JEGLlMsLIINJvLaW0n_t0fgc_26IC2ZvvjhKUriJ688q-P_IHFgjE8yLVI51c=
 LiMT: a multi-task liver image benchmark dataset - arXiv. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbf8cgU4h3dBW3FTx6DDrDOVVUyK0l_vVoi6LPpkN638H6QJ1vzhgusOFD_upl_9dZfy4OxM5eEM62kiYCvLSnXEmf0-BA7eCqYezHTp4o6Y_JWSFf_QdZRnKXfCIh
 A publicly available multiphasic MRI dataset with liver and HCC tumor segmentations and inter-rater agreement analysis - PMC. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYPXnvfbFtLTbs_xeGJoMBaO74RoO3c4BOcuZZcdPRnp5APpo5fYvrNyJkWixdObHkCxDk4Uf343MN0ECRD0W2_GqurFtQ8zSKPulARxchPvwRv5eaX-iFD5OBHnEsm5vitU0Wc1BmbWZFo4Fn
 Explore the human body in stunning, 3D detail with a new online tool | Popular Science. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGkI--8ns0FFepJhHdaSJ8saUwZziMIYfWAEFNHlFS7RnQY6z_3WoKdujn_9wmyZsv0df6yYNo6krGtiFrfOko8mn3BstqaOsJRC0iGSb0KSMKSyxcgnA6C3p9Fbo_XCE2_wmtOOCnknNvJA==
 C4KC-KiTS - The Cancer Imaging Archive (TCIA). https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe4qhBQLrGh-sEF6foOS1aH43ph0jOg7ZXPrfKdTkGrQL_7X1fk-1u_8eGaSB6zZ3JzS7Acg_b6B9m6OGYxEpvXhYK6YuWDG4mg3Ap1pDaA0vTvW9Xy_mFeIVrF_oAotXpWKNrkL6uGjHSFma2QfXOe5ZkWQk=
 TCGA-KIRC - The Cancer Imaging Archive (TCIA). https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnogd1X2W6lmh1z4AOPi-SX_zXAuV9GSrFC7HzYbIeNeiFjG28mk1FoG5XQX3ZuQLxjqxoI5WCrGQsE0w6JJl2YdzWpzhWcs_UW6GAvxvJ05753LAEe5eCYoIr9EFGnqZj1SDgq80_Zsfb_2gnl4ahRhzyfqM=
 Imaging Data Commons - CRDC - National Cancer Institute. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRWR9AbftgteKSWvTjLyJ8PLX3DwY7uAHgVBn8Csa_f-ijMQGIH4QWJNfNJICjZmieLcek7-mafxXNoR8vZ7sC06UN8eyjKUB9R4xX5y83cbaJ71aTSbc_005EaS4v6ID42_uvqlN9U_lFwf-wv-Ev2zC3VIv4hb0M
 Automatic Segmentation of Kidneys and Kidney Tumors: The KiTS19 International Challenge - PMC. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3toTRnb2U2lY0wxxZoMz5FeWWbRkh0YnXEUD-8AeN4L7lYSpXx4vO_Nf1pXojCg_gZMdOoUxaGtrsxJEtv59Jmf8qi16oXoGxTCd21UBX3TDNvwPYTTajcHGVJ29sUMM2UH3K2KcLZiMhDR0=
 Home - KiTS19 - Grand Challenge. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4C2hzolxikBmNm3bjj8BFa9uXlFUcTizOfEsxD0fTZ-awsxnLMkTHREgHPa8wmAUoJbR3NU8ImoOI3B5xKRaz87l9rQr3wcXZbxEW1sd47WsWflJk4PSTCs3w4a-b
 AI in Medical Imaging: The Kidney Tumor Segmentation Challenge | Banook. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHG85uzxLaBZNg3FGAznsNj8E5Yxh7qBt-IqohPutalbqFjY79wsatOhfwk4kLu2c4dO5HUOivRJtZgRp7t-mkKDalizZXmiYIn4Nf2A-6n4FMzrgt7sIrHS-GqL9fl-e22UTNJ_uMF8E98m1LzmqWICIXvyyOsPDF89HTLTeo1irx0KH5eZAamNq1Kjol_sYFnUcTuPzqYzRpdzhB-g==
 Diversity in Renal Mass Data Cohorts: Implications for Urology AI Researchers - PMC. https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5zjHAFZWywAS_liia60frNqOpHXPqAY809h7N50GOVMJCgYvcUIL_ZRFLlzoeSA_qAFIpfvVU4_hx1oE5PtSQP3cz5jkDbGKcbhNyUjZ1tUEriNnBAg67h7N_whxZe-KQMyhyug0JSO4sLt1D
 TCGA-LIHC - The Cancer Imaging Archive (TCIA). 