import openai

openai.api_key = "YOUR_API_KEY"

def explain_code(code, language="python"):
    prompt = f"""
You are a senior software engineer. Explain the following {language} code in simple terms.
Also provide any improvements or bugs if you find any.

```{language}
{code}
```
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response['choices'][0]['message']['content']
