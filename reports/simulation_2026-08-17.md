# Research Report: Simulation
*Generated: 2026-08-17 UTC*

## Executive Summary

The field of physics simulation platforms is experiencing rapid advancements, driven by open-source initiatives and the integration of AI. Key developments include enhanced accuracy, efficiency, and programmability, making these tools more accessible for research and development. Particular progress has been seen in medical simulation, with a focus on realistic soft tissue modeling for surgical training and bioelectromagnetic simulations for neurostimulation techniques. The trend towards non-restrictive licenses like CC-BY is also notable, promoting wider adoption and collaboration within the scientific community. Recent innovations are also making these simulations faster and more data-efficient, promising to accelerate design cycles and improve our understanding of complex physical phenomena.

## Key Announcements and Developments

### NVIDIA, Google DeepMind, and Disney Research

*   **Newton:** A new open-source physics engine developed collaboratively by NVIDIA, Google DeepMind, and Disney Research. Built on NVIDIA Warp, Newton aims to advance robot learning and development by offering a unified, scalable, and customizable solution for modeling real-world physics. It features differentiable physics for gradient propagation and is highly extensible for multiphysics simulations. Newton is compatible with learning frameworks like MuJoCo Playground and NVIDIA Isaac Lab.

### Quanscient

*   **Cloud-Based Multiphysics Simulation Platform:** Quanscient has expanded its cloud-based platform, integrating physics-based modeling with quantum-ready algorithms and AI-driven workflows. This expansion, supported by a €10 million Series A funding round, aims to accelerate engineering applications by enabling larger datasets, faster processing, and scalable experimentation. The platform allows for extensive virtual testing, reducing reliance on physical prototypes.

### Siemens

*   **PhysicsX:** Emerging from numerical physics and Formula One, PhysicsX, founded in 2019 and gaining traction in 2023, offers tools that can simulate complex systems rapidly. It claims to automatically iterate through millions of designs for performance optimization while adhering to constraints. PhysicsX joined the AWS Generative AI Accelerator in November 2024.

### Siemens EDA

*   **Converge CFD:** Convergent Science's flagship product has seen upgrades, including new solver options for speed and accuracy, enhanced modeling capabilities, and improved user experience in Version 4. The cloud computing platform, Converge Horizon, was upgraded in 2024 to streamline job submission, monitoring, and billing, with expanded collaborative features.

### Wildkatze Digital Solutions Co.

*   **Wildkatze CFD:** Launched in 2018, this Japanese CFD software package utilizes robust Finite Volume and Finite Difference solvers. Its flexibility and advanced solver customization through user algorithms and C++ coding allow for the integration of different physics models and schemes in various regions, enhancing the reproducibility of physical phenomena.

### MIT CSAIL and Tsinghua University

*   **GeoPT:** This new pre-training approach enables AI models to learn physics more broadly and efficiently, simulating how objects respond to forces like wind and water with increased accuracy and speed. GeoPT surpasses state-of-the-art models in speed and accuracy, requiring significantly less labeled data for training. Researchers believe this could lead to a physics foundation model for AI.

## Notable Papers and Projects

*   **The interactive medical simulation toolkit (iMSTK): an open source platform for surgical simulation:** This paper introduces iMSTK, an open-source C++ platform for physics simulation in the medical field, focusing on surgical training. It leverages Unity and extended Position Based Dynamics (xPBD) for realistic soft tissue deformation and haptic feedback. Future work includes adding connective tissue, improving dissection methods, and incorporating electrosurgery.
*   **A Realistic Surgical Simulator for Non-Rigid and Contact-Rich Manipulation in Surgeries with the da Vinci Research Kit:** This work presents CRESSim, a surgical simulator built on PhysX 5 for the da Vinci Research Kit (dVRK). It enables simulation of various surgical tasks involving soft tissue, fluids, and instruments, with teleoperation capabilities through VR. CRESSim can simulate soft bodies, cloth, and fluids, utilizing GPU-based FEM for soft body simulation.
*   **pyModSurgical provides tools to generate modal analysis of surgical video and learn soft tissue dynamics:** This Python package implements modal analysis for soft tissue based on surgical videos, allowing for realistic simulations of tissue deformation and force calculation. It can generate simulations with user-interactive forces and synthesize videos based on interaction commands.
*   **SimNIBS: an open source tool for simulating TES & TMS electric fields in individualized head models:** This presentation and associated software package allow for realistic calculations of electric fields induced by Transcranial Magnetic Stimulation (TMS) and Transcranial Electrical Stimulation (TES). SimNIBS uses individualized head meshes derived from MRI scans to estimate and visualize electrical fields.
*   **Open-Source Release of Multi-Physics Simulation Framework 4C:** The release of 4C (Comprehensive Computational Community Code) provides a framework for simulating complex problems in science, engineering, and biomedicine. It supports various physical models and multi-physics coupling, with applications in modeling human cardiovascular and respiratory systems.

## What to Watch

*   **Newton's Development:** Continued development and community contributions to Newton, particularly in its integration with robotics and AI frameworks, will be key.
*   **iMSTK's Enhancements:** Look for the addition of more advanced features in iMSTK, such as connective tissue simulation, improved dissection techniques, and electrosurgery capabilities.
*   **GeoPT's Scalability:** The research team's efforts to scale GeoPT to simulate more complex physical phenomena and its potential development into a physics foundation model for AI.
*   **Advancements in Cloud-Based Simulation:** Continued growth and integration of AI and quantum computing capabilities within platforms like Quanscient's.

## Possible Clinical Relevance

*   **Surgical Training and Planning:** Platforms like iMSTK and CRESSim offer highly realistic virtual environments for surgical training, allowing surgeons to practice complex procedures in a risk-free setting, potentially improving patient outcomes.
*   **Neurosurgical Interventions:** Simulators using frameworks like SOFA can be adapted to plan specific surgeries, such as eye operations, neurosurgery, or liver surgery, by incorporating patient-specific data.
*   **Non-Invasive Brain Stimulation:** SimNIBS provides tools for precise calculations of electric fields for TMS and TES, aiding in the optimization of stimulation parameters for targeted brain regions. This can advance research and therapeutic applications for neurological and psychiatric conditions.
*   **Medical Device Development:** Simulators can be used to create and test new medical instruments, such as catheters and stents, before they are physically manufactured, potentially reducing development time and cost.
*   **Biomechanical Research:** OpenSim, a biomechanics software, can be used to simulate surgical procedures and design medical devices, contributing to a better understanding of human movement and the development of improved treatments.

## Sources

1.  Frontiers | The interactive medical simulation toolkit (iMSTK): an open source platform for surgical simulation.
2.  Announcing Newton, an Open-Source Physics Engine for Robotics Simulation | NVIDIA Technical Blog.
3.  Multiphysics Simulation Platforms - Trend Hunter.
4.  Fifteen simulation tools to watch.
5.  A Realistic Surgical Simulator for Non-Rigid and Contact-Rich Manipulation in Surgeries with the da Vinci Research Kit - arXiv.
6.  With a feel for physics, AI models simulate a wider range of real-world scenarios | MIT News.
7.  The Top 8 Free and Open Source Simulation Software - Goodfirms.
8.  Tutorial: E-field modeling with simNIBS - FCBG Platforms.
9.  Free tDCS Modeling Tools.
10. Open-Source Release of Multi-Physics Simulation Framework 4C - Universität der Bundeswehr München.
11. SimNIBS 4.6.0 documentation - GitHub Pages.
12. SimNIBS - Simulation of Non-Invasive Brain Stimulation - GitHub.
13. SimNIBS: an open source tool for simulating TES & TMS electric fields in individualized head models - YouTube.
14. pyModSurgical provides tools to generate modal analysis of surgical video and learn soft tissue dynamics.
15. Open Source Human Body Simulator for Medical Training - Interoperability.
16. MuJoCo — Advanced Physics Simulation.
17. Open Source Physics - Wikipedia.
18. Best Open Source Simulation Software 2026 - SourceForge.
19. Project Chrono - An Open-Source Physics Engine.
20. Best open source simulation & CAE software February 2026 - FitGap.