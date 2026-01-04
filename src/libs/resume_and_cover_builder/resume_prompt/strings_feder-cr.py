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
Act as an HR expert and resume writer with a specialization in creating high-scoring ATS-friendly resumes. Your task is to detail the work experience for a resume. To achieve an ATS score > 90, follow these strict rules:

1. **Format**: Follow the [Template to Use] exactly.
2. **Action Verbs**: Start every bullet point with a strong, diverse professional action verb (e.g., "Engineered", "Orchestrated", "Spearheaded").
3. **Metrics & Quantifiable Results**: Every responsibility MUST include a metric (e.g., %, $, numbers). Use the [Action Verb] + [Task] + [Result/Metric] format.
4. **Keyword Optimization**: Intelligently integrate technical keywords from the job description context if provided.
5. **Readability**: Ensure bullet points are concise yet high-impact. Avoid "bogus" or "fluff" language.

- **My information:**  
  {experience_details}
- **Job Description Context:**
  {job_description}
"""+ prompt_working_experience_template


prompt_projects = """
Act as an HR expert and resume writer with a specialization in high-impact technical resumes. Your task is to highlight notable side projects. For a >90 ATS score:

1. **Highlight Scalability**: Emphasize how projects solve technical problems or handle scale (e.g., "handled 10k+ requests").
2. **Tech Stack**: Clearly mention specific tools and languages used.
3. **Format**: Every project bullet must show a result or a technical achievement.

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
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list additional skills relevant to the job. For each skill, ensure you include:

1. **Skill Category**: Clearly state the category or type of skill.
2. **Specific Skills**: List the specific skills or technologies within each category.
3. **Proficiency and Experience**: Briefly describe your experience and proficiency level.

- **My information:**  
  {languages}
  {interests}
  {skills}
"""+ prompt_additional_skills_template
