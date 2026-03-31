import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "yanolja/YanoljaNEXT-Rosetta-4B-2511"
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
    max_memory={0: "23GB"},
)
tokenizer = AutoTokenizer.from_pretrained(model_id)

target_language = "Korean"
context = {
    "context": "Simple introduction about a tech company.",
    "tone": "Informative and helpful",
    "glossary": {
        "Yanolja NEXT": "야놀자넥스트",
        "travel industry": "여행 산업",
    }
}

system = [f"Translate the user's text to {target_language}."]
for key, value in context.items():
    key_pascal = key.capitalize()
    if isinstance(value, dict):
        system.append(f"{key_pascal}:")
        for f, t in value.items():
            system.append(f"- {f} -> {t}")
    else:
        system.append(f"{key_pascal}: {value}")

system.append("Output format: JSON")
system.append(
    "Provide the final translation immediately without any other text.")

source = {
    "company_name": "Yanolja NEXT",
    "description": "Yanolja NEXT is a company that provides cutting-edge "
    "technology for the global travel industry.",
}

messages = [
    {"role": "system", "content": "\n".join(system)},
    {"role": "user", "content": json.dumps(source, ensure_ascii=False)},
]

prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True)
print(prompt)
# <bos><start_of_turn>instruction
# Translate the user's text to Korean.
# Context: Simple introduction about a tech company.
# Tone: Informative and helpful
# Glossary:
# - Yanolja NEXT -> 야놀자넥스트
# - travel industry -> 여행 산업
# Output format: JSON
# Provide the final translation immediately without any other text.<end_of_turn>
# <start_of_turn>source
# {"company_name": "Yanolja NEXT", "description": "Yanolja NEXT is a company that provides cutting-edge technology for the global travel industry."}<end_of_turn>
# <start_of_turn>translation

inputs = tokenizer(prompt, return_tensors="pt").to("auto")
input_length = inputs["input_ids"].shape[1]

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=64,
    )

generated_tokens = outputs[0][input_length:]
translation = tokenizer.decode(generated_tokens, skip_special_tokens=True)

print(json.dumps(json.loads(translation), indent=2, ensure_ascii=False))
# {
#   "company_name": "야놀자넥스트",
#   "description": "야놀자넥스트는 글로벌 여행 산업에 최첨단 기술을 제공하는 회사입니다."
# }
