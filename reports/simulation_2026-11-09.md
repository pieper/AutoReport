# Research Report: Simulation
*Generated: 2026-11-09 UTC*

**Executive Summary**

Recent advancements in physics simulation platforms are characterized by a growing emphasis on open-source accessibility, enhanced computational efficiency, and broader applicability across diverse scientific and engineering domains. Key developments include the expansion of multi-physics frameworks, the integration of AI for more accurate and faster simulations, and specialized platforms for complex biological and medical applications. While commercial software continues to offer robust solutions, the open-source community is rapidly innovating, providing powerful, customizable, and often more accessible alternatives. This report details notable open-source simulation packages, with a particular focus on those relevant to soft tissue and bioelectromagnetic simulations, and highlights their features, licensing, and potential clinical impact.

## Key Announcements and Developments

### Simulation Platforms for General Physics and Multiphysics

*   **Project Chrono:** This open-source, cross-platform C++ multiphysics simulation infrastructure has been recognized as one of the most complete platforms for coupled physical systems. It supports rigid and flexible multibody dynamics, finite element analysis, vehicle dynamics, granular materials, and fluid-solid interaction. The inclusion of PyChrono provides Python access, lowering the barrier for researchers and data scientists. Chrono is released under a BSD-3 license.
*   **MOOSE Framework:** MOOSE is a finite element framework designed for coupled multiphysics simulations. Its modular design allows for extensive customization and extension through C++ development, making it suitable for research groups needing to prototype new constitutive behaviors or specialized constraints. It supports nonlinear and time-dependent problems and is oriented towards high-performance computing.
*   **Elmer:** This open-source multiphysics finite element software package is built around a configurable finite element workflow. Elmer supports equation-driven multiphysics assembly and is known for its flexibility in solver selection and mesh-driven boundary conditions. It's valuable for systematic comparisons through reusable file-based cases.
*   **OpenFOAM:** A widely-used open-source framework for computational fluid dynamics (CFD) and continuum simulations. OpenFOAM offers extensive solver customization and supports dynamic meshes and transient solvers. It's a powerful tool for engineers and researchers in CFD and related multiphysics workflows.
*   **4C (Comprehensive Computational Community Code):** Recently open-sourced under the LGPL license, 4C is a comprehensive multiphysics simulation framework designed for complex problems in science, engineering, and biomedicine. It offers ready-to-use simulation capabilities for various physical models and a modular environment for research in mathematical modeling. It has been applied to human cardiovascular and respiratory systems and engineering applications.
*   **AI-driven Simulation (WorldParticle, GeoPT):**
    *   **WorldParticle:** Developed by researchers at MIT and UBC, this single deep-learning system aims to model diverse physical phenomena from sliding sand to folding proteins. It uses a Lagrangian representation and tracks particles to simulate material dynamics, offering potentially faster and more accurate simulations than traditional numerical methods.
    *   **GeoPT:** This pre-training approach from MIT and Tsinghua University allows AI models to learn physics more broadly and efficiently. It reenacts mechanical interactions to give models a sense of how physics works, leading to more accurate real-world modeling and faster training times. It has the potential to predict how vehicles, everyday items, and robots respond to physical elements.

### Specialized Simulations

*   **Surgical Simulation (Soft Tissue):**
    *   **iMSTK (Interactive Medical Simulation Toolkit):** An open-source platform specifically for medical simulation, iMSTK uses extended position-based dynamics (xPBD) for realistic soft-body mechanics and haptics. It has been used for various surgical simulations, including hernia repair, cholecystectomy, osteotomy, and kidney biopsy procedures. iMSTK is released under the flexible Apache 2.0 license.
    *   **CRESsim:** Based on PhysX 5, CRESsim is a realistic surgical simulator designed for the da Vinci Research Kit (dVRK). It supports simulating contact-rich surgical tasks involving soft tissue, fluids, and instruments, with parameters like Young's modulus and Poisson's ratio being controllable. It enables real-time teleoperation and has been demonstrated for tissue grasping, blood suction, and cutting.
    *   **SOFA (Simulation Open Framework Architecture):** An open-source framework for multi-physics simulation with a strong emphasis on medical applications. SOFA supports modeling of soft and rigid body dynamics, fluid dynamics, and heat transfer. It is used for surgical planning, training, and testing medical instruments, with applications in eye operations, neurosurgery, and liver surgery.
    *   **Flamingo Biolab:** Flamingo Biolab specializes in creating highly realistic surgical simulators with customizable elasticity, hardness, and viscosity to mimic human tissues. Their simulators prioritize haptic feedback and are used for practicing maneuvers like dissection and suturing.
    *   **Kitware:** Offers an end-to-end ecosystem for surgical simulation and planning using tools like VTK, 3D Slicer, and Pulse. Their solutions enable virtual and augmented reality simulations, real-time image-guided navigation, and cross-disciplinary collaboration.
*   **Bioelectromagnetic Simulations (TMS, TES, PNS):**
    *   **SimNIBS:** An open-source software package for simulating non-invasive brain stimulation, including Transcranial Magnetic Stimulation (TMS) and Transcranial Electrical Stimulation (TES). It allows for realistic calculations of electric fields induced by these methods, uses fast FEM solvers, and can generate high-quality head models from MRI data. SimNIBS is licensed under GPL v3. Recent updates include new optimization methods for TMS and TES, and new TMS coil models.
    *   **NeuroSimo:** An open-source software platform designed for closed-loop EEG- or EMG-guided TMS. It allows researchers to rapidly prototype and develop novel stimulation paradigms using Python and C++. NeuroSimo leverages ROS 2 for inter-process communication and aims to advance personalized brain stimulation by enabling real-time closed-loop control.
    *   **Open rTMS:** A project focused on Transcranial Magnetic Stimulation (TMS), consisting of multiple subprojects including PC-based control software and signal generators. It is licensed under the GNU General Public License version 3.0 (GPLv3).

### Licensing Considerations

The trend towards open-source adoption is facilitated by permissive licenses. Many prominent platforms like Project Chrono (BSD-3 license), iMSTK (Apache 2.0 license), and 4C (LGPL license) offer non-restrictive licenses. SimNIBS (GPL v3) and Open rTMS (GPL v3) are also open-source but under copyleft licenses. It is important to note that some widely used simulation resources, such as PhET Interactive Simulations, are licensed under Creative Commons Attribution–NonCommercial (CC BY-NC 4.0), which restricts commercial use.

## Notable Papers

*   **PhysiCell: An open source physics-based cell simulator for 3-D multicellular systems:** This paper introduces PhysiCell, an agent-based simulator for 3D multicellular systems, capable of simulating cell interactions and microenvironmental conditions. It is noted for its minimal dependencies and cross-platform compatibility.
*   **The interactive medical simulation toolkit (iMSTK): an open source platform for surgical simulation:** Details the development and capabilities of iMSTK, highlighting its use of extended position-based dynamics for accurate soft-body mechanics and haptics in surgical simulations, with a focus on real-time performance and compatibility with visualization and haptic devices.
*   **An open-source framework for multi-physics simulations and optimization:** Presents a simulation framework built entirely on open-source technologies, integrating tools like OpenFOAM for CFD and DAKOTA for optimization, demonstrating its capability for complex engineering tasks.
*   **Soft Tissue Modeling for Surgical Simulation:** This work focuses on developing biomechanical models of soft tissue, specifically the liver, from experimental measurements to create reality-based models for surgical simulation and haptic feedback. It discusses modeling tissue response to various deformations and the development of cutting models.
*   **Electric Field Simulations for Transcranial Brain Stimulation using FEM: an efficient implementation and error analysis:** This paper introduces an efficient Finite Element Method (FEM) implementation for TMS and TES simulations, showing it to be significantly faster than previous methods. It also highlights the importance of anatomical fidelity for accurate simulations and makes the new FEM code available as part of SimNIBS 3.0.

## What to Watch

*   **AI Integration in Simulation:** The increasing role of AI, as seen with WorldParticle and GeoPT, suggests a future where AI-driven models will provide faster, more accurate, and more generalizable simulations across various physics domains. Keep an eye on how these AI models are integrated into existing simulation frameworks and their impact on traditional numerical solvers.
*   **Advancements in Real-Time Simulation:** For medical applications, especially surgical simulation, real-time performance with haptic feedback is crucial. Developments in techniques like eXtended Position-Based Dynamics (XPBD) used in iMSTK and other surgical simulators will continue to push the boundaries of what is achievable in immersive training environments.
*   **Quantum Simulation Platforms:** While still an emerging field, quantum science and technology are seeing significant advancements in simulation. Tools for simulating qubits and quantum materials are being developed, often as open-source packages, which could revolutionize fields like materials science and computing.

## Possible Clinical Relevance

*   **Surgical Training and Planning:** Platforms like iMSTK, CRESsim, and SOFA offer highly realistic virtual environments for surgical training. They allow surgeons to practice complex procedures, refine techniques, and plan interventions on patient-specific models, potentially reducing errors, improving patient outcomes, and decreasing recovery times. The accurate simulation of soft tissue mechanics and haptic feedback is key to achieving this realism.
*   **Neuromodulation Therapies (TMS, TES):** Simulators like SimNIBS and NeuroSimo are invaluable for optimizing non-invasive brain stimulation therapies such as TMS and TES. By accurately modeling electric fields induced in the brain, these tools can help researchers and clinicians personalize stimulation parameters, target specific brain regions more effectively, and develop new therapeutic approaches for neurological and psychiatric disorders.
*   **Medical Device Development:** The ability to simulate the interaction of medical instruments with biological tissues, as demonstrated by systems like CRESsim and SOFA, can accelerate the design and testing of new surgical tools, implants, and devices, reducing the need for costly and time-consuming physical prototyping.

## Sources

*   Ghaffarizadeh A, Heiland R, Friedman SH, Mumenthaler SM, Macklin P (2018) PhysiCell: An open source physics-based cell simulator for 3-D multicellular systems. PLoS Comput Biol. 2018;14(2): e1005904.
*   Moore J, Scheirich H, Jadhav S, Enquobahrie A, Paniagua B, Wilson AA, et al. (2023) The interactive medical simulation toolkit (iMSTK): an open source platform for surgical simulation. Front Comput Sci. 5.
*   Guerrero J, R. J, M. A, B. J. (2015, April 15). An open-source framework for multi-physics simulations and optimization.
*   Guideflow Blog. (2026, October 19). 21 best physics engine software for 2026.
*   RoboMed Lab. Soft Tissue Modeling for Surgical Simulation.
*   Gitnux. (2026, July 03). Top 10 Best Physics Simulation Software of 2026.
*   MIT News. (2026, November 09). A single AI model simulates the behavior of many substances, from sliding sand to folding proteins.
*   arXiv. (2024, April 08). A Realistic Surgical Simulator for Non-Rigid and Contact-Rich Manipulation in Surgeries with the da Vinci Research Kit.
*   Kitware Inc. Surgical Planning and Simulation.
*   GitHub Pages. SimNIBS 4.6 documentation.
*   Flamingo Biolab. Surgical Simulators for Surgery & Planning.
*   Interoperable Europe Portal - European Union. (2017, February 13). Open source human body simula….
*   DTU Research Database. Tutorial: E-field modeling with simNIBS.
*   University of Colorado Boulder. Licensing Information | PhET Simulations.
*   Algoryx Simulation. Project Chrono - An Open-Source Physics Engine.
*   Universität der Bundeswehr München. (2025, January 13). Open-Source Release of Multi-Physics Simulation Framework 4C.
*   UChicago News. (2024, April 12). World Quantum Day 2024: The latest developments in quantum science and technology.
*   EurekAlert!. (2026, July 21). Researchers expand simulation tool to help design the next generation of photonic and quantum devices.
*   DTU Research Database. (2018, October 24). Electric Field Simulations for Transcranial Brain Stimulation using FEM: an efficient implementation and error analysis.
*   bioRxiv. (2025, April 09). NeuroSimo: an open-source software for closed-loop EEG- or EMG-guided TMS.
*   SourceForge. Open rTMS.
*   MIT News. (2026, August 10). With a feel for physics, AI models simulate a wider range of real-world scenarios.
*   GitHub. physicsnemo/LICENSE.txt at main.