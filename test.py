from transformers import pipeline


pipe = pipeline(
    "text-generation", 
    model = "kingabzpro/mistral_7b_guanaco",
    device_map="auto"
)

prompt = "How do I become a data engineer in 6 months?"

sequences = pipe(
    f"<s>[INST] {prompt} [/INST]",
    do_sample=True,
    max_new_tokens=200, 
    temperature=0.7, 
    top_k=50, 
    top_p=0.95,
    num_return_sequences=1,)

print(sequences[0]['generated_text'])