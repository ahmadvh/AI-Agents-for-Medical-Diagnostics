# AI-Agents-for-Medical-Diagnostics
A Python project to create specialized LLM-based AI agents that analyze complex medical cases. The system integrates insights from various medical professionals to provide comprehensive assessments and personalized treatment recommendations, showcasing the potential of AI in multidisciplinary medicine.

In the current version, there are three AI agents implemented based on GPT-4. The medical report is passed to each of these agents, who then synchronously analyze the report using threading, based on their respective expertise. Each agent provides recommendations and diagnoses from their perspective. Once all AI agents have completed their analyses, the results are combined and passed to a large language model, which is responsible for summarizing the findings and identifying three final potential health issues for the patient.

**1- Cardiologist Agent**
Focus: Identify any potential cardiac issues that could explain the patient's symptoms. This includes ruling out conditions such as arrhythmias or structural abnormalities that might not be apparent on initial evaluations.

Recommendation: Advise on additional cardiovascular testing or continuous monitoring if needed to uncover any hidden heart-related problems. Suggest management strategies if a cardiovascular issue is found.

**2- Psychiatrist Agent**
Focus: Determine if the symptoms align with a psychological condition such as panic disorder or another anxiety-related issue. Evaluate the influence of stress, anxiety, and lifestyle on the patient’s overall condition.

Recommendation: Propose appropriate psychological interventions (e.g., therapy, stress management techniques) or medications to address the psychological aspects of the symptoms. Consider if adjustments to current psychological management are necessary.

**3- Pulmonologist Agent**
Focus: Determine if symptoms like shortness of breath and dizziness are due to a respiratory condition, such as asthma or a breathing disorder, which could be confused with cardiac symptoms.

Recommendation: Suggest additional respiratory evaluations, such as lung function tests or stress tests, to rule out any underlying lung conditions. Recommend breathing techniques or other treatments if a respiratory issue is suspected.

<img width="950" alt="image" src="https://github.com/user-attachments/assets/d33bb192-c0c1-4fb0-8346-fd7e0a61b329">

In future versions, the system could expand to include a broader range of AI agents, each specialized in different medical fields, such as neurology, endocrinology, and immunology, to provide even more comprehensive analyses. These AI agents could be implemented using the [Assistant API from OpenAI](https://platform.openai.com/docs/assistants/overview) and use function calling and code interpreter capabilities to enhance their intelligence and effectiveness. Additionally, we could introduce advanced parsing methodologies to handle medical reports with more complex structures, allowing the system to accurately interpret and analyze a wider variety of medical data.
