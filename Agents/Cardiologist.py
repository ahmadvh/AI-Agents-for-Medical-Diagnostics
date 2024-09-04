
class Cardiologist:
    def __init__(self, medical_report, openAI_client):
        self.prompt = f"""
        Act like a cardiologist. You will receive a medical report of a patient. 
        Task: Review the patient's cardiac workup, including ECG, blood tests, Holter monitor results, and echocardiogram.
        Focus: Determine if there are any subtle signs of cardiac issues that could explain the patient’s symptoms. Rule out any underlying heart conditions, such as arrhythmias or structural abnormalities, that might be missed on routine testing.
        Recommendation: Provide guidance on any further cardiac testing or monitoring needed to ensure there are no hidden heart-related concerns. Suggest potential management strategies if a cardiac issue is identified.
        Please only return the possible causes of the patient's symptoms and the recommended next steps.
        Medical Report: {medical_report}
        """
        self.openAI_client = openAI_client

    def generate_response(self):
        print("Cardiologist is generating response...")
        response = self.openAI_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "user",
            "content": self.prompt
            }
        ],
        max_tokens=1200,
        top_p=1
        )

        response_text = response.choices[0].message.content
        return response_text