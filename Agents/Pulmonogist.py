class Pulmonogist:
    def __init__(self, patient_report, openAI_client):
        self.prompt = f"""
        Act like a pulmonologist. You will receive a patient's report. 
        Task: Review the patient's report and provide a pulmonary assessment.
        Focus: Identify any potential respiratory issues, such as asthma, COPD, or lung infections, that may be affecting the patient's breathing.
        Recommendation: Offer guidance on how to address these respiratory concerns, including pulmonary function tests, imaging studies, or other interventions.
        Please only return the possible respiratory issues and the recommended next steps.
        Patient's Report: {patient_report}
        """
        self.openAI_client = openAI_client

    def generate_response(self):
        print("Pulmonogist is generating response...")
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
