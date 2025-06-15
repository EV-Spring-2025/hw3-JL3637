# EV-HW3: PhysGaussian
### B10902033 林祐辰

## Part 1

The two materials I chose are jelly and metal, and I simulated them on the Ficus model. The simulation videos are in the `part_1_video`, and the configuration files I used are in `config/part_1`. A small finding in this part is that, to simulate metal material, the parameter `yield_stress` needs to be added to the config.

## Part 2

For Part 2, I tried adjusting four parameters (`n_grid`, `substeps`, `grid_v_damping_scale`, and `softening`) on the Ficus model. However, only two of them had a noticeable effect: `substeps` and `grid_v_damping_scale`. I think this may due to the pretrained Ficus model not being configured to use the other two parameters. Therefore, I conducted experiments by adjusting `substep_dt` and `grid_v_damping_scale`. The simulation videos are in the `part_2_video`, and the configuration files I used are in `config/part_2`.

1. `substep_dt` (stadard: `1e-4`, tested: `5e-5`, `8e-5`)

    Psnr score:
    1. Jelly_5e-5: `22.53` dB
    2. Jelly_8e-5: `25.19` dB
    3. Metal_5e-5: `15.64` dB
    4. Metal_8e-5: `17.68` dB
    
    Key takeaways & finding:

    Visually, a larger substep_dt leads to greater movement of the Ficus in the simulation video, likely due to increased numerical integration per step, allowing more dynamics to unfold.

2. `grid_v_damping_scale` (stadard: `0.9999`, tested: `0.999`, `0.9995`)

    Psnr score:
    1. Jelly_0.999: `22.13` dB
    2. Jelly_0.9995: `22.49` dB
    3. Metal_0.999: `15.31` dB
    4. Metal_0.9995: `17.80` dB

    Key takeaways & finding:

    This parameter controls the velocity damping in the grid; a larger value retains more velocity, resulting in more movement in the simulation.The visual effect is similar to substep_dt, higher values produce livelier, more dynamic motion in the ficus, potentially improving the perceptual realism but also increasing numerical sensitivity.

### Bonus part answer:

Design a learning-based inverse framework:

1. Input: Observed video of material behavior (e.g., deformation, motion).
2. Feature Extraction: Use a pretrained vision backbone (e.g., ResNet, ViT) to extract spatiotemporal features.
3. Material Parameter Regressor: Feed features into a neural network that regresses simulation parameters (e.g., Young’s modulus, damping, friction).
4. Simulation Loop: Plug predicted parameters into a differentiable physics simulator (e.g., Taichi or DiffTaichi).
5. Loss Function: Compute photometric or perceptual loss between simulated and real video.
6. Optimization: Train end-to-end with supervised or self-supervised learning on a dataset of known material behaviors.

This enables parameter inference for unseen materials from real-world observations.

## Youtube video link:

https://youtu.be/cnugiYee5Dw


# Reference
```bibtex
@inproceedings{xie2024physgaussian,
    title     = {Physgaussian: Physics-integrated 3d gaussians for generative dynamics},
    author    = {Xie, Tianyi and Zong, Zeshun and Qiu, Yuxing and Li, Xuan and Feng, Yutao and Yang, Yin and Jiang, Chenfanfu},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    year      = {2024}
}
```
