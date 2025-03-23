import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model():
    """Загружает модель WhiteRabbitNeo и токенизатор"""
    model_name = "WhiteRabbitNeo/Llama-3.1-WhiteRabbitNeo-2-8B"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.float16, device_map="auto"
    )
    
    return model, tokenizer
