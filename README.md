# Harry Potter Webcam Cloak Effect

This project applies a "cloak effect" on a webcam feed in real-time, inspired by the **Invisibility Cloak** from the **Harry Potter** series! The effect works by detecting **blue regions** in the video stream and replacing them with a background (essentially masking out the blue color). This simulates the magical invisibility effect seen in the movies, where the character wearing the cloak becomes partially or completely invisible.

### Key Features:
- Real-time webcam feed manipulation.
- Detects and masks **blue regions** in the feed, creating the invisibility cloak effect.
- Replaces the blue regions with a custom background.
- Exit the application with the **Esc** key.

---

## Requirements

- **Python 3.x**: You must have Python installed on your system.
- **OpenCV**: This project uses OpenCV for video processing and computer vision tasks.
  
### Install Required Libraries

You can install the necessary libraries using `pip`. If you don't have OpenCV installed, you can do so by running:

```bash
pip install opencv-python
