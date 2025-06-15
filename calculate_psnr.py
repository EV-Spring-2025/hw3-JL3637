import cv2
import numpy as np

def calculate_psnr(img1, img2):
    mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
    if mse == 0:
        return float('inf')  # Perfect match
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))

def psnr_video(reference_path, test_path):
    ref_cap = cv2.VideoCapture(reference_path)
    test_cap = cv2.VideoCapture(test_path)

    if not ref_cap.isOpened() or not test_cap.isOpened():
        raise IOError("Error opening video files.")

    total_psnr = 0.0
    frame_count = 0

    while True:
        ret1, ref_frame = ref_cap.read()
        ret2, test_frame = test_cap.read()

        if not ret1 or not ret2:
            break

        if ref_frame.shape != test_frame.shape:
            raise ValueError("Frames are not the same size.")

        psnr = calculate_psnr(ref_frame, test_frame)
        total_psnr += psnr
        frame_count += 1

    ref_cap.release()
    test_cap.release()

    if frame_count == 0:
        raise ValueError("No frames compared.")
    
    avg_psnr = total_psnr / frame_count
    print(f"Average PSNR: {avg_psnr:.2f} dB")
    return avg_psnr

# Example usage
reference_video_jelly = './part_1_video/jelly_output.mp4'
reference_video_metal = './part_1_video/metal_output.mp4'
reference_video = reference_video_metal 
test_video_substep_dt = './part_2_video/substep_dt/metal_8e-5.mp4'
test_video_grid_v_damping_scale = './part_2_video/grid_v_damping_scale/metal_0.9995.mp4'
test_video = test_video_grid_v_damping_scale


psnr_video(reference_video, test_video)