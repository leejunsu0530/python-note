# https://huggingface.co/docs/optimum-intel/en/openvino/optimization
# OVModelForCausalLM.from_pretrained('TinyLlama/TinyLlama-1.1B-Chat-v1.0', quantization_config=OVWeightQuantizationConfig(bits=8)).save_pretrained('save_dir')
#이걸로 데이터 없이 양자화