# Route CLIPs through HuggingFace cache
SDXL_CLIP1_PATH = 'openai/clip-vit-large-patch14'
SDXL_CLIP2_CKPT_PTH = 'laion/CLIP-ViT-bigG-14-laion2B-39B-b160k'

# Point directly to where our Docker image will download the safetensors
SUPIR_ckpt_F_path = '/root/models/SUPIR/SUPIR-v0F_fp16.safetensors'
SUPIR_ckpt_Q_path = '/root/models/SUPIR/SUPIR-v0Q_fp16.safetensors'
