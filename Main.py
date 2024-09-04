# importing the required libraries
from openai import OpenAI
from dotenv import load_dotenv
import os 
from concurrent.futures import ThreadPoolExecutor
from Agents.Cardiologist import Cardiologist
from Agents.Psychologist import Psychologist
from Agents.Pulmonogist import Pulmonogist

# Loading API key and organization ID from a dotenv file
load_dotenv(dotenv_path='apikey.env')

# Retrieving API key and organization ID from environment variables
APIKEY = os.getenv("APIKEY")
ORGID = os.getenv("ORGID")

# Creating an instance of the OpenAI client with the provided API key and organization ID
client = OpenAI(
  organization= ORGID,
  api_key=APIKEY
)

# read the medical report
with open("Medical Reports\Medical Rerort - Michael Johnson - Panic Attack Disorder.txt", "r") as file:
    medical_report = file.read()

# print(medical_report)

# define the agents
agent1 = Cardiologist(medical_report, client)
agent2 = Psychologist(medical_report, client)
agent3 = Pulmonogist(medical_report, client)

# define a function to get the response of an agent
def get_response(agent):
    return agent.generate_response()

# Run all agents concurrently using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks to the executor
    future_cardiologist = executor.submit(get_response, agent1)
    future_psychologist = executor.submit(get_response, agent2)
    future_pulmonologist = executor.submit(get_response, agent3)

    # Collect results
    cardiologist_response = future_cardiologist.result()
    psychologist_response = future_psychologist.result()
    pulmonogist_response = future_pulmonologist.result()


# Prompt for the GPT-4o model to combine the responses of the agents and generate a final diagnosis

prompt = f"""
Act like a multidisciplinary team of healthcare professionals.
You will receive a medical report of a patient visited by a Cardiologist, Psychologist, and Pulmonogist.
Task: Review the patient's medical report from the Cardiologist, Psychologist, and Pulmonogist, analyze them and come up with a list of 3 possible health issues of the patient.
Just return a list of bulletpoints of 3 possible health issues of the patient and for each issue provide the reason.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": prompt
        },
        {
            "role": "assistant",
            "content": cardiologist_response
        },
        {
            "role": "assistant",
            "content": psychologist_response
        },
        {
            "role": "assistant",
            "content": pulmonogist_response
        }
    ],
    max_tokens=1000,
    top_p=1
)

response_text = response.choices[0].message.content

# save the respnse to a file 
with open("Results\Results - Michael Johnson", "w") as file:
    file.write(response_text)

print("the diagnosis has been saved to a file.")