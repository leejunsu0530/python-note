"""
1. ov로 npu 감지
2. 번역 모델(LLM) 테스트
https://huggingface.co/models?search=llama
https://huggingface.co/yanolja

"""
import transformers
import openvino

# check npu
# from openvino.intel # 이것도 안불러와지고
from openvino.runtime import Core # 이거 안불러와지는데?

core = Core()
devices = core.available_devices

print(devices)