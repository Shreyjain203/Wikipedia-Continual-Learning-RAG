from auto_gptq import AutoGPTQForCausalLM
from transformers import AutoTokenizer, TextStreamer
from transformers import pipeline
from langchain import HuggingFacePipeline
import torch


def pipeline(
        model_name_or_path="TheBloke/Llama-2-13B-chat-GPTQ",
        model_basename="model"
        ):
    DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

    model = AutoGPTQForCausalLM.from_quantized(
        model_name_or_path,
        revision="gptq-4bit-128g-actorder_True",
        model_basename=model_basename,
        use_safetensors=True,
        trust_remote_code=True,
        inject_fused_attention=False,
        device=DEVICE,
        quantize_config=None,
        disable_exllama=True,
        auto_devices=True
    )

    tokenizer = AutoTokenizer.from_pretrained(
        model_name_or_path,
        use_fast=True
        )
    streamer = TextStreamer(
        tokenizer,
        skip_prompt=True,
        skip_special_tokens=True
        )

    text_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=1024,
        temperature=0,
        top_p=0.95,
        repetition_penalty=1.15,
        streamer=streamer
    )

    return HuggingFacePipeline(
        pipeline=text_pipeline,
        model_kwargs={"temperature": 0}
        )
    