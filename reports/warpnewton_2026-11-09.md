# Research Report: Warpnewton
*Generated: 2026-11-09 UTC*

# Executive Summary

NVIDIA's Warp and Newton-Physics communities are experiencing significant and rapid development, particularly in the last year. Newton, a GPU-accelerated physics simulation engine built on NVIDIA Warp, has seen a major push with its beta release in September 2025 and a General Availability (GA) release in March 2026. It's being actively integrated into NVIDIA's robotics ecosystem, including Isaac Lab, and is seeing adoption by industrial partners. Warp, a Python framework for GPU-accelerated simulation, robotics, and machine learning, continues to evolve with frequent releases and a growing community, evidenced by its million-plus downloads per month. Both frameworks emphasize differentiable programming, enabling advanced AI-driven workflows.

## Key Announcements and Developments

### NVIDIA Warp

*   **Continued Development and Releases:** Warp has seen consistent releases, with versions like v1.18.0 and v1.19.0 introducing new features such as geometry modules, improved CPU block execution, reusable sparse assembly, and new sparse preconditioners.
*   **Growing Adoption:** Warp has reached over 1 million downloads per month and has a growing community of contributors.
*   **Differentiable Programming and AI Integration:** Warp's ability to accelerate and differentiate computational physics code makes it crucial for AI-driven workflows. It bridges CUDA and Python, allowing developers to write high-performance kernels as Python functions that are JIT-compiled for GPU execution.
*   **Application in Various Domains:** Beyond robotics, Warp is being used for Computational Fluid Dynamics (CFD), healthcare robotics simulations, and general scientific computing and optimization.

### Newton-Physics

*   **Beta and General Availability:** The Newton physics engine, built on NVIDIA Warp, had a beta release in September 2025 and reached General Availability (GA) in March 2026.
*   **Linux Foundation Project:** Newton is now managed by the Linux Foundation, with contributions from NVIDIA, Google DeepMind, and Disney Research.
*   **Integration with NVIDIA Ecosystem:** Newton is being deeply integrated into NVIDIA's robotics offerings, including Isaac Lab and Isaac Sim. This integration aims to accelerate robot learning and development by providing a robust simulation backend.
*   **Key Features and Performance:** Newton offers GPU-accelerated, extensible, and differentiable physics simulation. It supports multiple solvers for various use cases, including MuJoCo Warp, Kamino, and VBD solvers. It aims to bridge the "sim-to-real" gap with high-fidelity simulations.
*   **Industrial Adoption:** Companies like Skild AI, Samsung, and Lightwheel are using Newton for industrial robotics applications such as assembly and cable manipulation. ETH Zurich has also used Newton and Isaac Lab to train and deploy locomotion policies.

## Notable Papers and Research

*   **"Kamino: GPU-based Simulation of Rigid Multi-Body Physics with Kinematic Loops"**: This paper introduces Kamino, a GPU-based physics solver implemented in Python using NVIDIA Warp and integrated into the Newton framework. It enables large-scale reinforcement learning on complex robotic systems with kinematic loops.
*   **"CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation"**: This 2026 publication highlights the use of Warp for differentiable simulation in manipulation tasks.
*   **"SceneFactory-3D: Lifting 2D Traffic Scenes into 3D Physical Counterfactuals for Scalable Physically Grounded Safety Evaluation"**: Another 2026 publication utilizing Warp for advanced simulation in safety evaluations.
*   **"Asking the World: Generalist Physical Reasoning through Agentic World Modeling and Probing"**: This research leverages Warp for physical reasoning and world modeling.
*   **"CollisionSplatting: Collision-Aware Motion Planning in 3DGS Scenes with Image-Conditioned Objectives and Adjustable Conservatism"**: A 2026 paper showcasing Warp's application in motion planning.
*   **"Bundled Contact Gradients: Stabilizing Differentiable Simulation for Deployable Dynamic Tasks"**: This 2026 research focuses on improving differentiable simulation with Warp.
*   **"Real-Time Force Regulation for Whole-Hand Dexterous Grasping"**: A 2026 paper demonstrating Warp's use in dexterous manipulation.
*   **"NVIDIA Warp Accelerates Differentiable Computational Physics Code for AI"**: This article discusses how Warp is accelerating AI-driven engineering and simulation workflows, mentioning its use in CFD and robotics.
*   **"MuJoCo Warp (MJWarp), built on NVIDIA Warp, takes compatible MuJoCo models into that GPU-scale regime."**: This highlights the acceleration of MuJoCo physics simulation on GPUs using Warp.
*   **"NeRD: Neural Robot Dynamics for learned simulation"**: This research uses Newton for learned simulation in robotics.

## What to Watch

*   **Continued Integration of Newton into Isaac Lab:** Expect further development and feature expansion in the integration of Newton with NVIDIA's Isaac Lab, enabling more sophisticated robot learning workflows.
*   **Warp's Evolving Feature Set:** Keep an eye on upcoming Warp releases for new modules, performance improvements, and expanded support for various simulation and machine learning tasks.
*   **Newton's Solver Ecosystem:** The expansion of Newton's solver ecosystem, with new backends and specialized solvers, will be crucial for its adoption in diverse robotics applications.
*   **Sim-to-Real Transfer Advancements:** Both Warp and Newton are foundational to improving the sim-to-real transfer gap in robotics, so expect ongoing research and demonstrations in this area.
*   **Community Contributions:** The open-source nature of both projects suggests continued growth driven by community contributions to solvers, extensions, and applications.

## Possible Clinical Relevance

The advancements in Newton and Warp have significant potential for clinical relevance, particularly in:

*   **Medical Robotics Simulation:** Developing and training surgical robots with high precision and safety through accurate physics simulations. Warp's ability to handle complex physical interactions and Newton's integration into robotics platforms can enable more realistic training environments for surgeons and robot control systems.
*   **Rehabilitation Robotics:** Simulating and designing robotic devices for physical therapy and rehabilitation. Accurate physics simulation can help optimize the design and control of these devices for effective patient recovery.
*   **Prosthetics and Orthotics Design:** Utilizing advanced simulation to design and test more functional and comfortable prosthetic limbs and orthotic devices, considering complex biomechanical interactions.
*   **Drug Discovery and Development:** While not directly related to robotics, Warp's capability in accelerating computational physics simulations could indirectly benefit fields like molecular dynamics and material science relevant to drug discovery, by providing faster and more accurate simulations of molecular interactions.

## Sources

*   NVIDIA warp Announcements · Discussions - GitHub. (n.d.). Retrieved November 9, 2026, from https://github.com/NVIDIA/warp/discussions/categories/announcements
*   Releases · NVIDIA/warp - GitHub. (n.d.). Retrieved November 9, 2026, from https://github.com/NVIDIA/warp/releases
*   A Comprehensive Guide to the Physics Engine "Newton" 1.0 by NVIDIA, Disney, and Google DeepMind: What Changes for Robot Learning｜アイドリ | AI-Driven Lab - note. (n.d.). Retrieved November 9, 2026, from 
*   Newton Physics Engine: How NVIDIA, Google DeepMind & Disney Are Reshaping Sim-to-Real Robotics - Robolabs AI. (n.d.). Retrieved November 9, 2026, from https://www.rolabs.ai/blog/newton-physics-engine-how-nvidia-google-deepmind-disney-are-reshaping-sim-to-real-robotics
*   Newton Physics Integration — Isaac Lab Documentation. (n.d.). Retrieved November 9, 2026, from 
*   NVIDIA at CoRL: GR00T 2, Isaac Lab 3.0 and why physical AI lags behind LLMs | daily.dev. (n.d.). Retrieved November 9, 2026, from 
*   Newton Adds Contact-Rich Manipulation and Locomotion Capabilities for Industrial Robotics | NVIDIA Technical Blog. (n.d.). Retrieved November 9, 2026, from https://developer.nvidia.com/blog/newton-adds-contact-rich-manipulation-and-locomotion-capabilities-for-industrial-robotics/
*   Physics Simulation for Robotics | NVIDIA Use Case. (n.d.). Retrieved November 9, 2026, from 
*   NVIDIA launches Newton physics engine and GR00T AI at CoRL 2025 - The Robot Report. (n.d.). Retrieved November 9, 2026, from 
*   Tag: Warp | NVIDIA Technical Blog. (n.d.). Retrieved November 9, 2026, from https://developer.nvidia.com/blog/tag/warp/
*   NVIDIA Warp accelerates differentiable physics code for AI | Trending Stories | HyperAI. (n.d.). Retrieved November 9, 2026, from 
*   NVIDIA Warp Documentation — Warp 1.14.0. (n.d.). Retrieved November 9, 2026, from https://docs.warp.dev/
*   Build Accelerated, Differentiable Computational Physics Code for AI with NVIDIA Warp. (n.d.). Retrieved November 9, 2026, from https://developer.nvidia.com/blog/build-accelerated-differentiable-computational-physics-code-for-ai-with-nvidia-warp/
*   NVIDIA Warp Python. (n.d.). Retrieved November 9, 2026, from https://www.nvidia.com/en-us/on-demand/session/gtc21-s41192-nvid-warp-python-1619627702000v00/
*   GitHub - newton-physics/newton: An open-source, GPU-accelerated physics simulation engine built upon NVIDIA Warp, specifically targeting roboticists and simulation researchers. (n.d.). Retrieved November 9, 2026, from https://github.com/newton-physics/newton
*   Newton Physics - GitHub. (n.d.). Retrieved November 9, 2026, from https://github.com/newton-physics
*   From a Physics Prototype to a Million Downloads a Month: What NVIDIA Warp 1.17 Actually Is | by James Fahey | Medium. (n.d.). Retrieved November 9, 2026, from 
*   With Great Physics Comes Great Responsibility: A Deep Dive into NVIDIA Newton. (n.d.). Retrieved November 9, 2026, from 
*   A Comprehensive Guide to the Physics Engine "Newton" 1.0 by NVIDIA, Disney, and Google DeepMind: What Changes for Robot Learning｜アイドリ | AI-Driven Lab - note. (n.d.). Retrieved November 9, 2026, from 
*   newton-physics newton Announcements · Discussions - GitHub. (n.d.). Retrieved November 9, 2026, from https://github.com/newton-physics/newton/discussions/categories/announcements
*   warp/PUBLICATIONS.md at main · NVIDIA/warp - GitHub. (n.d.). Retrieved November 9, 2026, from https://github.com/NVIDIA/warp/blob/main/PUBLICATIONS.md
*   Kamino: GPU-based Simulation of Rigid Multi-Body Physics with Kinematic Loops - arXiv. (n.d.). Retrieved November 9, 2026, from https://arxiv.org/abs/2603.16536
*   Kamino: GPU-based Massively Parallel Simulation of Multi-Body Systems with Challenging Topologies - arXiv. (n.d.). Retrieved November 9, 2026, from https://arxiv.org/abs/2603.16536v2
*   How to Use NVIDIA Warp and MjWarp to Accelerate Robotics Simulation and Learning Workflows - Hugging Face. (n.d.). Retrieved November 9, 2026, from 
*   A tutorial on kinematics and optimization using NVIDIA Warp. (n.d.). Retrieved November 9, 2026, from 
*   Newton: Open-Source GPU Physics for Robot Simulation | Physical AI Day at SIGGRAPH 2026 - YouTube. (n.d.). Retrieved November 9, 2026, from https://www.youtube.com/watch?v=Q6yYmXz8x1c
*   NVIDIA Newton Physics Engine 2026 - RoboCloud Hub. (n.d.). Retrieved November 9, 2026, from 