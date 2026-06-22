# Research Report: Simulation
*Generated: 2026-06-22 UTC*

## Executive Summary

Recent advancements in physics simulation technologies are enhancing accuracy, efficiency, and programmability across various fields. Open-source packages are becoming increasingly sophisticated, offering modern architectures and active communities. In biomechanics and medical simulation, significant progress has been made in soft tissue deformation for surgical applications, with new frameworks enabling patient-specific models and realistic interaction. Bioelectromagnetic simulations for TMS, TES, and PNS are also benefiting from open-source tools that allow for individualized head models and precise electric field calculations. The trend towards cloud-based simulation and AI-driven workflows promises further acceleration and accessibility in the coming years.

## Key Announcements and Developments

### MuJoCo

*   **MuJoCo**: This free and open-source physics engine is designed for robotics, biomechanics, graphics, and animation. It offers a combination of speed, accuracy, and modeling power, with a focus on model-based optimization, particularly through contacts. Its architecture is performance-tuned with preallocated data structures and an XML-based compiler. It includes built-in visualization and a native graphical interface.
*   **MuJoCo** is owned and curated by Google DeepMind and has become popular in reinforcement learning research.

### Open Source Physics Collection (OSP)

*   The OSP Collection provides curriculum resources, code libraries, tools, and simulations for physics, computation, and computer modeling, aimed at engaging students and researchers.
*   **Tracker** is a tool within OSP that extends video analysis by allowing users to create particle models based on Newton's laws, synchronizing models with real-world videos for experimental testing.
*   **Easy Java Simulations (EJS)** provides tools for exploring physics without requiring deep programming knowledge.
*   While comprehensive, OSP has noted gaps in areas like Fluid Mechanics, Relativity, and Medical Physics. Many of its models are older Java files, which may present compatibility issues with modern browsers.

### Project Chrono

*   **Project Chrono** is an open-source, C++ based physics simulation infrastructure designed for embedding into other software projects. It supports rigid and flexible parts, motors, and contacts, with a Python interface (PyChrono) also available.
*   It is designed for customization and can be used for simulating robotics, vehicle dynamics, mechatronics, and fluid-solid interactions, with capabilities for large-scale and co-simulation with other FEA/CFD software.
*   Chrono is released under a BSD-3 license.

### Interactive Medical Simulation Toolkit (iMSTK)

*   **iMSTK** is an open-source platform for surgical simulation, featuring position-based dynamics, continuous collision detection, and compatibility with game engines like Unity and Unreal.
*   It is designed to model biological tissues and their interactions with medical tools, offering real-time simulation capabilities with visualization and haptics.
*   iMSTK uses extended position-based dynamics and has been applied to simulations of various surgical procedures, including laparoscopic surgeries and kidney biopsies.
*   It is released under a flexible Apache 2.0 license, encouraging adoption in research and commercial communities.

### SimNIBS

*   **SimNIBS** is an open-source software package for simulating electric fields induced by Transcranial Electrical Stimulation (TES) and Transcranial Magnetic Stimulation (TMS).
*   It generates individualized head models from MRI scans, calculates electric fields using the Finite Element Method (FEM), and offers post-processing tools.
*   SimNIBS supports optimization of TMS coil positions and TES montages for precise targeting of brain regions and is developed under the GPL v3 license.
*   Recent updates include new optimization methods for coil positions and TES montages, including those for bent and flexible coils, and leadfield-free optimization.

### 4C (Comprehensive Computational Community Code)

*   **4C** is a newly released open-source multi-physics simulation framework designed for complex problems in science, engineering, and biomedicine.
*   It offers modularity for research in mathematical modeling and numerical methods, with capabilities for single-field and multi-physics coupling.
*   4C has been applied to modeling human cardiovascular and respiratory systems and has potential applications in engineering and material science.
*   It is released under an open-source license, encouraging community contributions and collaboration.

### ORBIT-Surgical

*   **ORBIT-Surgical** is an open-source surgical robotics simulator built on NVIDIA Isaac Sim, featuring GPU-accelerated physics, contact-rich interactions, and high-fidelity rendering.
*   It supports simulations with both rigid and deformable materials and is designed for reinforcement learning (RL) and imitation learning (IL) workflows.
*   It includes simulated surgical subtasks and supports robotic platforms like the da Vinci Research Kit (dVRK).

### Newton

*   **Newton** is an open-source, GPU-accelerated physics simulation engine built on NVIDIA Warp, specifically targeting roboticists and simulation researchers.
*   It emphasizes GPU computation, OpenUSD support, differentiability, and user-defined extensibility.
*   Newton is a Linux Foundation project licensed under Apache-2.0.

## Notable Papers

*   "Soft tissue deformation for surgical simulation: a position-based dynamics approach" introduces a framework for volumetric deformation of soft tissue using a position-based dynamics approach, enabling realistic interaction and ultrasound simulation.
*   "Deformable Models for Surgical Simulation: A Survey" provides a comprehensive overview of deformable models used in soft tissue modeling for interactive surgical simulation, discussing various methodologies and challenges.
*   "Soft-Tissue Simulation for Computational Planning of Orthognathic Surgery" proposes a methodology for soft-tissue simulation that achieves high accuracy and computational efficiency, focusing on the coupling of rigid-bone and soft-tissue components.
*   "An Evaluation of Open Source Physics Engines for Use in Virtual Reality Assembly Simulations" compares freely available physics engines for robotic assembly simulation in virtual reality, assessing collision detection, constraint reliability, and body inter-penetration.
*   "The interactive medical simulation toolkit (iMSTK): an open source platform for surgical simulation" details iMSTK, an open-source platform for surgical simulation that uses position-based dynamics and offers real-time simulation capabilities with visualization and haptics.
*   "A Realistic Surgical Simulator for Non-Rigid and Contact-Rich Manipulation in Surgeries with the da Vinci Research Kit" presents CRESSim, a realistic surgical simulator based on PhysX 5 for the dVRK, capable of simulating various contact-rich surgical tasks.
*   "Review on Biophysical Modelling and Simulation Studies for Transcranial Magnetic Stimulation" summarizes TMS dosimetry studies, highlighting the importance of anatomical and biophysical parameters and computational methods for calculating induced electric fields in the brain.
*   "SimNIBS: an open source tool for simulating TES & TMS electric fields in individualized head models" introduces SimNIBS as an open-source tool for simulating electric fields from non-invasive brain stimulation techniques.

## What to Watch

*   **Continued Development of GPU-Accelerated Simulators:** Tools like Newton and the ongoing enhancements in engines like PhysX (used in CRESSim) suggest a strong trend towards leveraging GPU power for faster and more complex simulations.
*   **Advancements in Soft Tissue Modeling:** Expect further refinement in position-based dynamics (PBD) and finite element methods (FEM) for more accurate and real-time soft tissue simulations in surgery.
*   **AI and Machine Learning Integration:** AI is poised to reshape simulation workflows, enabling faster answers through surrogate models and advanced optimization techniques. COMSOL is already incorporating deep-neural-network-based surrogate models.
*   **Cloud-Based Simulation Platforms:** The move towards cloud-based simulation will likely increase collaboration and accessibility, offering powerful computing infrastructure and centralized data management.
*   **Bioelectromagnetics and Personalized Medicine:** Continued development in tools like SimNIBS will further enable personalized treatment planning for TMS and TES by providing accurate, individualized electric field simulations.

## Possible Clinical Relevance

*   **Surgical Training and Planning:** Advanced soft tissue simulation platforms like iMSTK and ORBIT-Surgical can provide realistic environments for training surgeons, planning complex procedures, and improving patient outcomes by allowing for practice on patient-specific models.
*   **Neuromodulation Therapies:** Simulators such as SimNIBS are crucial for the precise planning and delivery of Transcranial Magnetic Stimulation (TMS) and Transcranial Electrical Stimulation (TES) therapies. This can lead to more effective treatments for neurological and psychiatric conditions by optimizing stimulation parameters for individual patients.
*   **Rehabilitation and Medical Device Development:** The ability to simulate biomechanical interactions and human body dynamics (e.g., using OpenSim or SOFA) has direct applications in designing rehabilitation strategies, testing new medical devices like catheters and stents, and understanding movement disorders.
*   **Diagnosis and Pre-operative Assessment:** Patient-specific soft tissue models derived from medical imaging can aid in diagnosis and pre-operative assessment, allowing clinicians to better understand anatomical structures and predict how tissues will behave during surgery.

## Sources

 MuJoCo — Advanced Physics Simulation. https://mujoco.org/
 Open Source Physics. https://www.compadre.org/osp/
 Open Source Physics Collection - PhysPort Methods and Materials. https://www.compadre.org/osp/
 Best Open Source Physics Software 2026 - SourceForge. 
 Project Chrono - An Open-Source Physics Engine. https://projectchrono.org/
 Soft tissue deformation for surgical simulation: a position-based dynamics approach - PMC. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9160539/
 Deformable Models for Surgical Simulation: A Survey - arXiv. https://arxiv.org/abs/2109.14860
 Soft-Tissue Simulation for Computational Planning of Orthognathic Surgery - MDPI. 
 COMSOL License Options for Commercial and Academic Use. 
 An Evaluation of Open Source Physics Engines for Use in Virtual Reality Assembly Simulations | Request PDF - ResearchGate. 
 An Evaluation of Open Source Physics Engines for Use in Virtual Reality Assembly Simulations - Semantic Scholar. https://www.semanticscholar.org/paper/An-Evaluation-of-Open-Source-Physics-Engines-for-Hummel-Wolff/9e277338e49f850918c88344903305f8d8722a0a
 SOFT TISSUE MODELING FOR VIRTUAL SURGERY SIMULATION - Canal 6 Editora. 
 Real-time simulation of soft tissue deformation for surgical simulation. )/;jsessionid=85AD8DAF28CF7398055C1E619C477BB7
 Licensing - Design Simulation Technologies. 
 license - InteractiveComputerGraphics/physics-simulation - GitHub. https://github.com/InteractiveComputerGraphics/physics-simulation/blob/main/LICENSE
 Licensing Information - PhET - University of Colorado Boulder. https://phet.colorado.edu/en/licensing
 pyModSurgical provides tools to generate modal analysis of surgical video and learn soft tissue dynamics. - GitHub. https://github.com/mikelitu/pymodsurgical
 SIMULIA Student License Program | Dassault Systèmes. 
 Open Source Motion Simulation | OpenSimCraft. https://opensimcraft.com/
 JOSS Papers: Computational physics - Journal of Open Source Software. https://joss.theoj.org/papers?category=computational+physics
 Newton: An open-source, GPU-accelerated physics simulation engine built upon NVIDIA Warp. https://github.com/newton-physics/newton
 Open-Source Release of 4C (“Comprehensive Computational Community Code”) - Universität der Bundeswehr München. 
 The interactive medical simulation toolkit (iMSTK): an open source platform for surgical simulation - Frontiers. 
 ORBIT-Surgical: An Open-Simulation Framework for Learning Surgical Augmented Dexterity - UC Berkeley's AUTOLAB. 
 Open source human body simula… | Interoperable Europe Portal - European Union. https://ec.europa.eu/digital-building-blocks/wikis/display/interop/Open+source+human+body+simulator
 A Realistic Surgical Simulator for Non-Rigid and Contact-Rich Manipulation in Surgeries with the da Vinci Research Kit - arXiv. https://arxiv.org/abs/2404.04973
 A Review of Nine Physics Engines for Reinforcement Learning Research - arXiv. https://arxiv.org/abs/2307.04213
 Outcome measures for electric field modeling in tES and TMS: A systematic review and large-scale modeling study - PMC. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10534813/
 Best open source simulation & CAE software February 2026 | FitGap. 
 The Top 8 Free and Open Source Simulation Software - Goodfirms. 
 Modeling and Simulation Predictions for 2025 | COMSOL Blog. 
 Quantum simulation breakthrough will lead to 'discoveries impossible in today's fastest supercomputers,' Google scientists claim | Live Science. 
 SimNIBS: an open source tool for simulating TES & TMS electric fields in individualized head models - YouTube. https://www.youtube.com/watch?v=hH64R4-rU1g
 SimNIBS 4.6.0 documentation - GitHub Pages. https://simnibs.github.io/simnibs/build/html/index.html
 Tutorial: E-field modeling with simNIBS - FCBG Platforms. 
 Simulation of evoked responses to transcranial magnetic stimulation using a multiscale cortical circuit model - PMC. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7761036/
 Review on Biophysical Modelling and Simulation Studies for Transcranial Magnetic Stimulation - arXiv. https://arxiv.org/abs/2007.00469
 10 trends in simulation software for 2025 - machineering. 
 A Systematic Review and Large-Scale tES and TMS Electric Field Modeling Study Reveals How Outcome Measure Selection Alters Results in a Person- and Montage-Specific Manner | bioRxiv. 
 Top 10 Breakthroughs of the Year in physics for 2025 revealed. https://physicsworld.com/a/top-10-breakthroughs-of-the-year-in-physics-for-2025-revealed/
 Review on Biophysical Modelling and Simulation Studies for Transcranial Magnetic Stimulation - arXiv. https://arxiv.org/abs/2007.00469
 Future Trends in Electromagnetics Simulation Physics AI Compute Power - YouTube. https://www.youtube.com/watch?v=0R93m6P_19I
 SimNIBS - Simulation of Non-Invasive Brain Stimulation - GitHub. https://simnibs.github.io/simnibs/
 Computational Research | Opitz Lab. 