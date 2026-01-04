from src.libs.resume_and_cover_builder.template_base import prompt_header_template, prompt_education_template, prompt_working_experience_template, prompt_projects_template, prompt_achievements_template, prompt_certifications_template, prompt_additional_skills_template, prompt_summary_template

prompt_header = """
Act as an HR expert and resume writer specializing in ATS-friendly resumes. Your task is to create a professional and polished header for the resume. The header should:

1. **Contact Information**: Include your full name, city and country, phone number, email address, LinkedIn profile, GitHub profile, and Portfolio URL. Exclude any information that is not provided.
2. **Formatting**: Ensure the contact details are presented clearly and are easy to read.

- **My information:**  
  {personal_information}
""" + prompt_header_template


prompt_education = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to articulate the educational background for a resume. For each educational entry, ensure you include:

1. **Institution Name and Location**: Specify the university or educational institution’s name and location.
2. **Degree and Field of Study**: Clearly indicate the degree earned and the field of study.
3. **Grade**: Include your Grade if it is strong and relevant.
4. **Relevant Coursework**: List key courses with their grades to showcase your academic strengths.

- **My information:**  
  {education_details}
"""+ prompt_education_template


prompt_working_experience = """
Act as an HR expert and resume writer specializing in high-scoring technical resumes. Your task is to detail work experience with "Strategic Enhancement" for the Job Description.

**Strategic Enhancement Rules:**
1. **Tailoring**: Intelligently align bullet points with the keywords and responsibilities in the Job Description. 
2. **Impact Optimization**: It is acceptable to "strategically enhance" achievements (e.g., slightly optimizing metrics or emphasizing relevant sub-tasks) as long as they remain professional, credible, and undetectable by recruiters.
3. **Format**: Follow the [Template to Use] exactly. Provide 4-6 high-impact bullet points per role.
4. **Action Verbs**: Start every bullet point with a strong, diverse professional action verb.
5. **Metrics**: Every responsibility MUST include a metric (%, $, numbers) to demonstrate impact.

- **My information:**  
  {experience_details}
- **Job Description Context:**
  {job_description}
"""+ prompt_working_experience_template


prompt_projects = """
Act as an HR expert and resume writer with a specialization in high-impact technical resumes. Your task is to highlight notable side projects. Provide 3-4 substantial bullet points per project to ensure a dense, professional look.

1. **Highlight Scalability**: Emphasize how projects solve technical problems or handle scale.
2. **Tech Stack**: Clearly mention specific tools and languages used.
3. **Format**: Every project bullet must show a result or a technical achievement.
4. **Detail**: Expand on the "why" and "how" of your technical choices to fill out the section effectively.

- **My information:**  
  {projects}
- **Job Description Context:**
  {job_description}
"""+ prompt_projects_template


prompt_summary = """
Act as an HR expert and resume writer specializing in professional branding. Your task is to create a powerful, 3-4 sentence Professional Summary. 

1. **Impact**: Start with a strong title and years of experience.
2. **Alignment**: Tailor the summary to align key strengths with the job description.
3. **ATS keywords**: Naturally integrate top technical keywords from the job description.
4. **Tone**: Professional, confident, and achievement-oriented.

- **My Information:**
  {personal_information}
  {technical_skills}
  {skills}
- **Job Description Context:**
  {job_description}
"""+ prompt_summary_template


prompt_achievements = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list significant achievements. For each achievement, ensure you include:

1. **Award or Recognition**: Clearly state the name of the award, recognition, scholarship, or honor.
2. **Description**: Provide a brief description of the achievement and its relevance to your career or academic journey.

- **My information:**  
  {achievements}
"""+ prompt_achievements_template


prompt_certifications = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list significant certifications based on the provided details. For each certification, ensure you include:

1. **Certification Name**: Clearly state the name of the certification.
2. **Description**: Provide a brief description of the certification and its relevance to your professional or academic career.

Ensure that the certifications are clearly presented and effectively highlight your qualifications.

To implement this:

If any of the certification details (e.g., descriptions) are not provided (i.e., None), omit those sections when filling out the template.

- **My information:**  
  {certifications}

"""+ prompt_certifications_template


prompt_additional_skills = """
Act as an HR expert and resume writer specializing in technical resumes. Your task is to extract and categorize technical skills from the provided information. 

1. **Strategic Selection**: prioritize and emphasize skills that are mentioned in the Job Description.
2. **Categorization**: Group skills into logical labels like "Languages", "Frameworks", "Databases", "DevOps/Tools", "Cloud", etc.
3. **Professional Format**: Each bullet point MUST have a bold Category Header followed by a comma-separated list of technologies.
4. **Languages**: Include a "Languages" category for spoken languages (e.g., English, Hindi).

- **My information:**  
  {languages}
  {interests}
  {technical_skills}
  {skills}
- **Job Description Context (if relevant):**
  {job_description}
"""+ prompt_additional_skills_template
