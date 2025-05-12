import google.generativeai as genai
from promps import master_prompt, diary_prompt, test_prompt

# Key
genai.configure(api_key="AIzaSyC7WPj7zze9leGeKiMGoY7GzGWvERe30HQ")

# Pick the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash") 

# Send the prompt
response = model.generate_content(
    master_prompt + test_prompt
)

# Output
print(response.text)

# Send the prompt
diary_response = model.generate_content(
    diary_prompt + test_prompt
)



# Output
print(diary_response.text)
