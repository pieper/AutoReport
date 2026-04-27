# Research Report: Warpnewton
*Generated: 2026-04-27 UTC*

## Executive Summary

NVIDIA's Warp and Newton-Physics communities are experiencing significant activity, primarily driven by advancements in physics simulation for robotics and AI. Warp, a Python framework for GPU-accelerated simulation, is seeing regular updates and expanding its interoperability with machine learning frameworks like JAX and PyTorch. Newton, a newer, open-source physics engine built on Warp, is rapidly maturing and being adopted for complex robotics simulations, with a focus on closing the "sim-to-real" gap. Both projects are actively releasing new versions, engaging with the community through GitHub, and contributing to cutting-edge research in areas like autonomous robotics, computational physics, and AI-driven scientific discovery.

## Key Announcements

### NVIDIA Warp

*   **Upcoming Removals and Deprecations (Warp v1.13.0):** Support for Python 3.9 will be removed, making Python 3.10 the minimum supported version. Functions like `wp.isfinite()`, `wp.isnan()`, and `wp.isinf()` will no longer accept integer types, and private API deprecations will be finalized, requiring migration to public APIs.
*   **Warp v1.12.1 Release:** This bugfix release addresses issues in tile correctness, silent correctness bugs, and type system/tooling. It also includes new examples for differentiable 2D Navier-Stokes optimization and `warp.fem` applications.
*   **Warp v1.12.0 Release:** Introduced experimental hardware-accelerated texture sampling, extended tile programming with element-wise arithmetic operators and differentiable FFT, and improved JAX interoperability with `jax.vmap` support. It also added new quaternion and approximate-math builtins, and `warp.fem` shape functions.
*   **Warp v1.11 Release:** Enhanced geometry query functions, including `wp.mesh_query_ray_anyhit()`, `wp.mesh_query_ray_count_intersections()`, and `wp.mesh_query_point_sign_parity()`, along with a `max_dist` parameter for spatial queries.
*   **Community Engagement:** NVIDIA actively engages with the Warp community through GitHub discussions, soliciting feedback on deployment, AOT & C++ workflows, and announcing training labs.

### Newton-Physics

*   **Newton 1.0 GA Release (March 16, 2026):** This release provides a production-ready foundation for dexterous manipulation and locomotion tasks, built on NVIDIA Warp and OpenUSD. It emphasizes accelerated, extensible physics simulation for robotics.
*   **Beta Release of Newton (September 29, 2025):** Announced as an open-source, GPU-accelerated physics engine managed by the Linux Foundation, Newton is co-developed with Google DeepMind and Disney Research. It aims to enable simulation of complex robot actions for real-world deployment.
*   **Newton Integration with Isaac Lab:** Newton is integrated into NVIDIA Isaac Lab, offering a unified framework for robot learning and simulation. This integration streamlines workflows from simulation to real-world deployment and addresses the "sim-to-real" gap.
*   **Production Deployments:** Samsung is using Newton for cable manipulation in refrigerator assembly lines, and Skild AI is using Newton with Isaac Lab to train reinforcement learning policies for GPU rack assembly.
*   **Community Project:** Newton is a Linux Foundation project, community-built and maintained, with contributions from NVIDIA, Google DeepMind, and Disney Research.

## Notable Papers

*   **GeoWarp: An automatically differentiable and GPU-accelerated implicit MPM framework for geomechanics based on NVIDIA Warp:** This paper introduces GeoWarp, an implicit Material Point Method (MPM) framework for geomechanics built on NVIDIA Warp, utilizing GPU parallelism and automatic differentiation for Jacobian computation.
*   **Post-Render Warp with Late Input Sampling Improves Aiming Under High Latency Conditions:** This research investigates the effectiveness of image warping for latency compensation in interactive graphics systems, providing guidance for designing future systems.
*   **AI-Newton: A Concept-Driven Physical Law Discovery System without Prior Physical Knowledge:** This paper proposes AI-Newton, a system that autonomously discovers physical laws from noisy experimental data without prior physical knowledge, successfully rediscovering fundamental laws of Newtonian mechanics.
*   **Neural Robot Dynamics (NeRD):** This work focuses on learned simulation for robots, with NeRD models trained using the simulation module in Newton, aiming to enable simulation of dynamic robots using neural physics solvers.

## What to Watch

*   **Warp 1.13.0 Release:** Expected to finalize deprecations, including the removal of Python 3.9 support and stricter type checking for mathematical functions.
*   **Newton Development:** Continued integration with NVIDIA Isaac Lab and expansion of supported features for reinforcement learning and imitation learning workflows.
*   **Community Growth:** Active participation in GitHub discussions and the release of new examples and tutorials for both Warp and Newton are anticipated.
*   **GTC 2026:** NVIDIA Warp for Computational Physics training labs are scheduled for March 16-19, 2026, indicating ongoing focus on educational outreach and community engagement.

## Possible Clinical Relevance

While Warp and Newton-Physics are primarily geared towards robotics, simulation, and scientific computing, their advancements in physics simulation and differentiable programming could have indirect clinical relevance:

*   **Medical Robotics:** Enhanced physics simulation capabilities can accelerate the development and training of surgical robots, leading to more precise and safer medical procedures.
*   **Drug Discovery and Development:** Warp's application in simulating protein docking and other molecular dynamics can expedite the discovery of new drugs and therapies.
*   **Biomechanics and Prosthetics:** Accurate physics simulations can aid in the design and testing of advanced prosthetics and exoskeletons, improving their functionality and patient comfort.
*   **Rehabilitation Robotics:** Sophisticated simulation environments can be used to train robots for patient rehabilitation, offering personalized and effective therapy.

## Sources

*   NVIDIA / warp - GitHub: https://github.com/NVIDIA/warp
*   Publications using Warp - GitHub Pages: 
*   NVIDIA Accelerates Robotics Research and Development With New Open Models and Simulation Libraries - NVIDIA Investor Relations: 
*   Announcing Newton, an Open-Source Physics Engine for Robotics Simulation - NVIDIA Technical Blog: https://developer.nvidia.com/blog/announcing-newton-an-open-source-physics-engine-for-robotics-simulation/
*   With Great Physics Comes Great Responsibility: A Deep Dive into NVIDIA Newton - Medium: 
*   [2507.09435] GeoWarp: An automatically differentiable and GPU-accelerated implicit MPM framework for geomechanics based on NVIDIA Warp - arXiv: https://arxiv.org/abs/2507.09435
*   Post-Render Warp with Late Input Sampling Improves Aiming Under High Latency Conditions - Research at NVIDIA: 
*   Newton Adds Contact-Rich Manipulation and Locomotion Capabilities for Industrial Robotics - NVIDIA Technical Blog: https://developer.nvidia.com/blog/newton-adds-contact-rich-manipulation-and-locomotion-capabilities-for-industrial-robotics/
*   NVIDIA Announces Isaac GR00T N1 — the World's First Open Humanoid Robot Foundation Model — and Simulation Frameworks to Speed Robot Development: https://www.globenewswire.com/news-release/2025/03/18/2194797/0/en/NVIDIA-Announces-Isaac-GR00T-N1-the-World-s-First-Open-Humanoid-Robot-Foundation-Model-and-Simulation-Frameworks-to-Speed-Robot-Development.html
*   NVIDIA warp Announcements · Discussions - GitHub: https://github.com/NVIDIA/warp/discussions
*   This Python Package Makes Differentiable Physics Simulations Practical - Towards AI: 
*   Build Accelerated, Differentiable Computational Physics Code for AI with NVIDIA Warp: https://developer.nvidia.com/blog/build-accelerated-differentiable-computational-physics-code-for-ai-with-nvidia-warp/
*   NVIDIA Warp Python: 
*   Warp Speed: NVIDIA Open-Source Framework Accelerates Scientific Computing in Python: 
*   Recent posts for: “Announcement” - NVIDIA Developer: 
*   Eric Heiden - Warp: Advancing Simulation AI with Differentiable GPU Computing in Python | SciPy 2024 - YouTube: https://www.youtube.com/watch?v=e0i5-9X7BwE
*   NVIDIA Newton 1.0: Open-Source Physics Engine for Robotics Sim-to-Real - Medium: 
*   Activity · NVIDIA/warp - GitHub: https://github.com/NVIDIA/warp/activity
*   NVIDIA Accelerates Robotics Research and Development With New Open Models and Simulation Libraries: https://www.globenewswire.com/news-release/2025/09/29/2304071/0/en/NVIDIA-Accelerates-Robotics-Research-and-Development-With-New-Open-Models-and-Simulation-Libraries.html
*   Activity · newton-physics/newton - GitHub: https://github.com/newton-physics/newton/activity
*   NVIDIA Warp Python: 
*   Nvidia Warp: Python framework for high-performance simulation and graphics code: 
*   Newton Physics Engine: How NVIDIA, Google DeepMind & Disney Are Reshaping Sim-to-Real Robotics - Robolabs AI: 
*   Newton Physics - GitHub: https://github.com/newton-physics
*   GitHub - newton-physics/newton: An open-source, GPU-accelerated physics simulation engine built upon NVIDIA Warp, specifically targeting roboticists and simulation researchers.: https://github.com/newton-physics/newton
*   Pull requests · newton-physics/newton - GitHub: https://github.com/newton-physics/newton/pulls
*   Warp-Consolidation: A Novel Execution Model for GPUs - Super Scientific Software Laboratory: 
*   Advancing Robotics Development with Neural Dynamics in Newton - NVIDIA Technical Blog: https://developer.nvidia.com/blog/advancing-robotics-development-with-neural-dynamics-in-newton/
*   Issues · NVIDIA/warp - GitHub: https://github.com/NVIDIA/warp/issues
*   Newton Physics Integration — Isaac Lab Documentation: 
*   AI-Newton: A Concept-Driven Physical Law Discovery System without Prior Physical Knowledge - arXiv: https://arxiv.org/abs/2504.01538
*   newton-physics newton · Discussions - GitHub: https://github.com/newton-physics/newton/discussions