from openai import OpenAI


client = OpenAI()

response = client.images.edit(
    image=open("ejemplo1.png", "rb"),
    mask=open("ejemplo1_mask.png", "rb"),
    prompt="Agrega un avion apunto de estrellarse",
    n=1,
    size="1024x1024",
    response_format="url"
)

print(response)
