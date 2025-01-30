

"""
Go to DeepSeek's API Platform
Sign up/Create an account
Navigate to API Keys section
Create a new API key and copy it
"""

# https://platform.deepseek.com/usage
# https://api-docs.deepseek.com/quick_start/pricing/
# https://api-docs.deepseek.com/

from openai import OpenAI, APIError, AuthenticationError
# pip3 install openai

client = OpenAI(
    api_key="your-api-key-here",
    base_url="https://api.deepseek.com"
)

### Text Response
try:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": "Explain quantum computing in simple terms"}
        ],
        temperature=0.7,
        max_tokens=500
    )
    print(response.choices[0].message.content)
    
except AuthenticationError:
    print("Authentication failed - check your API key")
except APIError as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
    

### Stream Output
try:
    stream = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": "Tell me a story about AI"}],
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

except AuthenticationError:
    print("Authentication failed - check your API key")
except APIError as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
