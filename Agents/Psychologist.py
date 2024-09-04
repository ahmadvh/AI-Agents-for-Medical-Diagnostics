class Psychologist:
    def __init__(self, patient_report, openAI_client):
        self.prompt = f"""
        Act like a psychologist. You will receive a patient's report. 
        Task: Review the patient's report and provide a psychological assessment.
        Focus: Identify any potential mental health issues, such as anxiety, depression, or trauma, that may be affecting the patient's well-being.
        Recommendation: Offer guidance on how to address these mental health concerns, including therapy, counseling, or other interventions.
        Please only return the possible mental health issues and the recommended next steps.
        Patient's Report: {patient_report}
        """
        self.openAI_client = openAI_client
    
    def generate_response(self):
        print("Psychologist is generating response...")
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