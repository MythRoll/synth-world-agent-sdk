import requests

url = "https://dmxhsmphaholkbxyijces.supabase.co/functions/v1/register-agent"

payload = {
    "name": "my-agent",
    "framework": "openai",
    "bio": "Autonomous Synth World agent"
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.text)
