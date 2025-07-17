import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_post(activities):  # <- Fix: accepts data from main.py
    if not activities:
        return "No coding activity yesterday. Taking time to plan and learn! 🚀"

    posts = []
    for act in activities:
        prompt = f"""
You're a developer sharing your daily coding update on social media.

Yesterday, you committed to the GitHub repo "{act['repo']}" with message:
"{act['message']}"

Here’s a brief summary of changes:
{act['summary']}

Now write a short, casual, and inspiring post for Twitter/LinkedIn under 100 words. 
Include what was improved, learned, or built.
Include this GitHub link: {act['url']}
Add relevant hashtags like #Coding, #DSA, or #WebDev.
"""
        try:
            res = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful and concise developer assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=300
            )
            content = res.choices[0].message.content.strip()
            posts.append(content)
        except Exception as e:
            print(f"Error generating post for {act['repo']}: {e}")
            continue

    return "\n\n---\n\n".join(posts)
