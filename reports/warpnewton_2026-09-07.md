# Research Report: Warpnewton
*Generated: 2026-09-07 UTC*

| **Category** | **URL** | **Original Text** | **Revised Text** |
|---|---|---|---|
| NVIDIA Warp |  | NVIDIA Warp has reached 10 million downloads. | NVIDIA Warp has surpassed 10 million downloads, indicating widespread adoption by developers and researchers for building GPU-accelerated workflows. |
| NVIDIA Warp |  | Warp was launched as an open-source project at GTC 2024, with monthly releases and support across Windows, Linux, and macOS. | Warp was launched as an open-source project at GTC 2024, with monthly releases and support across Windows, Linux, and macOS. |
| NVIDIA Warp |  | Warp is being integrated into NVIDIA Omniverse, enabling GPU-accelerated 3D simulation workflows and dynamic content creation within the platform. | Warp is being integrated into NVIDIA Omniverse, enabling GPU-accelerated 3D simulation workflows and dynamic content creation within the platform. |
| NVIDIA Warp |  | NVIDIA is hosting events like a livestream on "Accelerate Computational Engineering and Robotics With NVIDIA Warp" to showcase its capabilities and provide guidance. | NVIDIA is hosting events like a livestream on "Accelerate Computational Engineering and Robotics With NVIDIA Warp" to showcase its capabilities and provide guidance. |
| NVIDIA Warp | https://developer.nvidia.com/blog/build-accelerated-differentiable-computational-physics-code-for-ai-with-nvidia-warp/ | Notable recent releases include v1.15.0 and v1.14.0, with v1.15.0 introducing tile-based programming and integration with NVIDIA MathDx libraries for accelerated linear algebra. | Notable recent releases include v1.15.0 and v1.14.0, with v1.15.0 introducing tile-based programming and integration with NVIDIA MathDx libraries for accelerated linear algebra. |
| Newton Physics Engine |  | Newton has been contributed to the Linux Foundation, fostering a more open and community-governed development environment. | Newton has been contributed to the Linux Foundation, fostering a more open and community-governed development environment. |
| Newton Physics Engine | https://github.com/newton-physics/newton | The Newton physics engine has reached its Alpha stage, offering a range of solvers including MuJoCo Warp, Featherstone, VBD, and more. | The Newton physics engine has reached its Alpha stage, offering a range of solvers including MuJoCo Warp, Featherstone, VBD, and more. |
| Newton Physics Engine |  | Newton is specifically designed for roboticists and simulation researchers, aiming to bridge the sim-to-real gap with high-fidelity, GPU-accelerated simulations. | Newton is specifically designed for roboticists and simulation researchers, aiming to bridge the sim-to-real gap with high-fidelity, GPU-accelerated simulations. |
| Notable Papers |  | Autodesk Research Brings Warp Speed to Computational Fluid Dynamics on NVIDIA GH200 | Autodesk Research Brings Warp Speed to Computational Fluid Dynamics on NVIDIA GH200. |
| Notable Papers | https://developer.nvidia.com/blog/build-accelerated-differentiable-computational-physics-code-for-ai-with-nvidia-warp/ | This resource likely details how Warp's differentiable programming capabilities can be used to create computational physics code for AI applications, including optimization and data generation. | This resource likely details how Warp's differentiable programming capabilities can be used to create computational physics code for AI applications, including optimization and data generation. |
| What to Watch |  | As Newton is built on Warp, its progress will closely follow Warp's updates. Expect further refinements in solvers, integrations, and performance optimizations for robotics applications. | As Newton is built on Warp, its progress will closely follow Warp's updates. Expect further refinements in solvers, integrations, and performance optimizations for robotics applications. |
| What to Watch | https://github.com/newton-physics/newton | The open-source nature of both projects encourages community involvement, which will likely lead to new features, integrations, and extended use cases. | The open-source nature of both projects encourages community involvement, which will likely lead to new features, integrations, and extended use cases. |
| What to Watch |  | NVIDIA often uses GTC (GPU Technology Conference) for major announcements. Keep an eye on future GTC events for potential new releases or roadmap updates for Warp and Newton. | NVIDIA often uses GTC (GPU Technology Conference) for major announcements. Keep an eye on future GTC events for potential new releases or roadmap updates for Warp and Newton. |

## Executive Summary

NVIDIA Warp and the Newton physics engine are experiencing significant development and community engagement. Warp, an open-source Python framework for GPU-accelerated simulation, has reached 10 million downloads and is being adopted for a wide range of applications including robotics, computational engineering, and AI. Recent activity includes frequent commits, pull requests, and the release of new versions, such as v1.17.0. Newton, built on Warp, is a GPU-accelerated physics simulation engine for robotics, which has seen major milestones like its Alpha release and contributions from major players like Disney Research, Google DeepMind, and NVIDIA. Both projects are actively maintained and are foundational to advancements in physical AI and simulation.

## Key Announcements

### NVIDIA Warp

*   **10 Million Downloads:** NVIDIA Warp has surpassed 10 million downloads, indicating widespread adoption by developers and researchers for building GPU-accelerated workflows.
*   **Warp 1.17.0 Release:** The latest version of Warp (v1.17.0) has been released, featuring ongoing development and contributions from over 80 developers. This version continues to be the foundation for Newton and other NVIDIA projects, including potential use in DLSS training for differentiable image processing.
*   **GTC 2024 Launch:** Warp was launched as an open-source project at GTC 2024, with monthly releases and support across Windows, Linux, and macOS.
*   **Omniverse Integration:** Warp is being integrated into NVIDIA Omniverse, enabling GPU-accelerated 3D simulation workflows and dynamic content creation within the platform.
*   **Public Training and Livestreams:** NVIDIA is hosting events like a livestream on "Accelerate Computational Engineering and Robotics With NVIDIA Warp" to showcase its capabilities and provide guidance.
*   **Recent Releases:** Notable recent releases include v1.15.0 and v1.14.0, with v1.15.0 introducing tile-based programming and integration with NVIDIA MathDx libraries for accelerated linear algebra.

### Newton Physics Engine

*   **Linux Foundation Project:** Newton has been contributed to the Linux Foundation, fostering a more open and community-governed development environment.
*   **Alpha Release:** The Newton physics engine has reached its Alpha stage, offering a range of solvers including MuJoCo Warp, Featherstone, VBD, and more.
*   **Robotics Focus:** Newton is specifically designed for roboticists and simulation researchers, aiming to bridge the sim-to-real gap with high-fidelity, GPU-accelerated simulations.
*   **OpenUSD Integration:** Newton integrates with OpenUSD, facilitating real-time simulation of various physical elements for advancing robot learning.
*   **Early Use Cases:** Initial use cases include multi-physics examples like cloth manipulation and quadruped locomotion, with experimental integration in NVIDIA Isaac Lab.

## Notable Papers

*   **Autodesk Research Brings Warp Speed to Computational Fluid Dynamics on NVIDIA GH200:** This paper details how Autodesk Research used NVIDIA Warp to achieve significant speedups in large-scale fluid simulations, leveraging the GH200 Grace Hopper Superchip for out-of-core computation.
*   **Building Robotic Mental Models with NVIDIA Warp and Gaussian Splatting:** Explores the use of NVIDIA Warp in conjunction with Gaussian Splatting for creating robotic mental models, likely for applications in perception and spatial computing.
*   **Developing Healthcare Robotics with GPU-Native Medical Physics Simulation:** This work highlights the application of NVIDIA Warp for medical physics simulations in healthcare robotics, addressing the unique challenges of this field.
*   **Build Accelerated, Differentiable Computational Physics Code for AI with NVIDIA Warp:** This resource likely details how Warp's differentiable programming capabilities can be used to create computational physics code for AI applications, including optimization and data generation.

## What to Watch

*   **Newton's Continued Development:** As Newton is built on Warp, its progress will closely follow Warp's updates. Expect further refinements in solvers, integrations, and performance optimizations for robotics applications.
*   **Warp's Role in Physical AI:** Warp is increasingly positioned as a core technology for NVIDIA's "Physical AI" stack, bridging simulation and AI. Its adoption in areas like DLSS training suggests broader implications beyond traditional simulation.
*   **Community Contributions:** The open-source nature of both projects encourages community involvement, which will likely lead to new features, integrations, and extended use cases.
*   **GTC 2026 Events:** NVIDIA often uses GTC (GPU Technology Conference) for major announcements. Keep an eye on future GTC events for potential new releases or roadmap updates for Warp and Newton.

## Possible Clinical Relevance

While Warp and Newton are primarily focused on simulation, robotics, and computational engineering, their advancements could have indirect clinical relevance in several areas:

*   **Robotics in Healthcare:** The sophisticated simulation capabilities of Newton, powered by Warp, can accelerate the development and training of surgical robots, assistive devices, and rehabilitation robots. This could lead to more precise and effective robotic-assisted procedures and therapies.
*   **Medical Imaging and Diagnostics:** Warp's ability to accelerate complex simulations and its differentiability could be applied to advanced medical imaging techniques, improving image reconstruction, noise reduction, and the development of AI models for diagnostics.
*   **Drug Discovery and Development:** High-performance simulations, like those enabled by Warp, can model molecular interactions and complex biological systems, potentially speeding up the process of drug discovery and personalized medicine.
*   **Medical Device Design:** The ability to simulate intricate physical interactions and material properties with Warp and Newton could aid in the design and testing of advanced medical devices, ensuring safety and efficacy before physical prototypes are built.

## Sources

*   NVIDIA/warp - GitHub. <a href="https://github.com/NVIDIA/warp" target="_blank">https://github.com/NVIDIA/warp</a>
*   newton-physics/newton - GitHub. <a href="https://github.com/newton-physics/newton" target="_blank">https://github.com/newton-physics/newton</a>
*   NVIDIA Warp Announcements · Discussions - GitHub. <a href="https://github.com/NVIDIA/warp/discussions/categories/announcements" target="_blank">https://github.com/NVIDIA/warp/discussions/categories/announcements</a>
*   Warp Speed: NVIDIA Open-Source Framework Accelerates Scientific Computing in Python. 
*   NVIDIA Warp Reaches 10 Million Downloads. 
*   Autodesk Research Brings Warp Speed to Computational Fluid Dynamics on NVIDIA GH200. 
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   newton-physics newton Announcements · Discussions - GitHub. <a href="https://github.com/newton-physics/newton/discussions/categories/announcements" target="_blank">https://github.com/newton-physics/newton/discussions/categories/announcements</a>
*   A new experiment deepens the physics mystery over “big G” | by Ethan Siegel - Medium. <a href="https://ethan-seigel.medium.com/a-new-experiment-deepens-the-physics-mystery-over-big-g-9421651f6b6a" target="_blank">https://ethan-seigel.medium.com/a-new-experiment-deepens-the-physics-mystery-over-big-g-9421651f6b6a</a>
*   Newton's 300-Year-Old Law Passes Its Biggest Cosmic Test Yet - SciTechDaily. <a href="https://scitechdaily.com/newtons-300-year-old-law-passes-its-biggest-cosmic-test-yet/" target="_blank">https://scitechdaily.com/newtons-300-year-old-law-passes-its-biggest-cosmic-test-yet/</a>
*   Newton's 300-year-old law just passed its biggest test yet | ScienceDaily. 
*   Build Accelerated, Differentiable Computational Physics Code for AI with NVIDIA Warp. <a href="https://developer.nvidia.com/blog/build-accelerated-differentiable-computational-physics-code-for-ai-with-nvidia-warp/" target="_blank">https://developer.nvidia.com/blog/build-accelerated-differentiable-computational-physics-code-for-ai-with-nvidia-warp/</a>
*   Linux Foundation Welcomes Newton: The Next Open Physics Engine for Robotics. 
*   From a Physics Prototype to a Million Downloads a Month: What NVIDIA Warp 1.17 Actually Is | by James Fahey - Medium. <a href="https://james-fahey.medium.com/from-a-physics-prototype-to-a-million-downloads-a-month-what-nvidia-warp-1-17-actually-is-e59a2e9f5022" target="_blank">https://james-fahey.medium.com/from-a-physics-prototype-to-a-million-downloads-a-month-what-nvidia-warp-1-17-actually-is-e59a2e9f5022</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Physics-Aware RTX Apps with NVIDIA Omniverse Libraries | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=xH4pWb0Hncs" target="_blank">https://www.youtube.com/watch?v=xH4pWb0Hncs</a>
*   NVIDIA Warp Python. 
*   Pull requests · NVIDIA/warp - GitHub. <a href="https://github.com/NVIDIA/warp/pulls" target="_blank">https://github.com/NVIDIA/warp/pulls</a>
*   Pull requests · newton-physics/newton - GitHub. <a href="https://github.com/newton-physics/newton/pulls" target="_blank">https://github.com/newton-physics/newton/pulls</a>
*   Issues · NVIDIA/warp - GitHub. <a href="https://github.com/NVIDIA/warp/issues" target="_blank">https://github.com/NVIDIA/warp/issues</a>
*   Issues · newton-physics/newton - GitHub. <a href="https://github.com/newton-physics/newton/issues" target="_blank">https://github.com/newton-physics/newton/issues</a>
*   Activity · NVIDIA/warp - GitHub. <a href="https://github.com/NVIDIA/warp/activity" target="_blank">https://github.com/NVIDIA/warp/activity</a>
*   Activity · newton-physics/newton - GitHub. <a href="https://github.com/newton-physics/newton/activity" target="_blank">https://github.com/newton-physics/newton/activity</a>
*   NVIDIA Warp - GitHub Discussions. <a href="https://github.com/NVIDIA/warp/discussions" target="_blank">https://github.com/NVIDIA/warp/discussions</a>
*   newton-physics newton Discussions - GitHub. <a href="https://github.com/newton-physics/newton/discussions" target="_blank">https://github.com/newton-physics/newton/discussions</a>
*   Warp wide reduction operations significant slowdown since CUDA 12.4 for sm_80. 
*   How is NVIDIA Warp accelerating computational engineering and robotics applications? Join tomorrow's livestream to see how this open-source CUDA-X library helps developers accelerat - Facebook. <a href="https://www.facebook.com/NVIDIADeveloper/posts/pfbid02GtxUf9t2a1pMmjM6sN35n8MypV4Kk1P6mF8a6q5T9bQpDszS2QjC3g4fQn3qGfjl" target="_blank">https://www.facebook.com/NVIDIADeveloper/posts/pfbid02GtxUf9t2a1pMmjM6sN35n8MypV4Kk1P6mF8a6q5T9bQpDszS2QjC3g4fQn3qGfjl</a>
*   Are there still gaps in Newtonian physics? : r/askscience - Reddit. 
*   NVIDIA/warp: A Python framework for GPU-accelerated simulation, robotics, and machine learning. - GitHub. <a href="https://github.com/NVIDIA/warp" target="_blank">https://github.com/NVIDIA/warp</a>
*   Redesigning the Inference Chip: From Nvidia GPU's Flaws to OpenAI Jalapeño - zartbot.github.io. 
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Pull requests · newton-physics/newton-actuators - GitHub. <a href="https://github.com/newton-physics/newton-actuators/pulls" target="_blank">https://github.com/newton-physics/newton-actuators/pulls</a>
*   Pull requests · newton-physics/newton-assets - GitHub. <a href="https://github.com/newton-physics/newton-assets/pulls" target="_blank">https://github.com/newton-physics/newton-assets/pulls</a>
*   Newton Alpha Announcement #639 - GitHub. <a href="https://github.com/newton-physics/newton/issues/639" target="_blank">https://github.com/newton-physics/newton/issues/639</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Latest Announcements topics - NVIDIA Developer Forums. 
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub Pages. <a href="https://docs.warp.dev/" target="_blank">https://docs.warp.dev/</a>
*   Newton (newton-physics/newton) | Context7. <a href="https://context7.com/newton-physics/newton" target="_blank">https://context7.com/newton-physics/newton</a>
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. <a href="https://www.youtube.com/watch?v=U_6hR_Q950k" target="_blank">https://www.youtube.com/watch?v=U_6hR_Q950k</a>
*   NVIDIA Warp Documentation — Warp 1.17.0 - GitHub