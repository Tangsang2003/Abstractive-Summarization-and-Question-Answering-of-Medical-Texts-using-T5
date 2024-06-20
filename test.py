import os
import pathlib
import textwrap

import google.generativeai as genai



def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Summarize in intermediatory language where the person knows basic things" + ''' 

Chronic Obstructive Pulmonary Disease (COPD): An In-Depth Overview

Introduction
Chronic Obstructive Pulmonary Disease (COPD) is a progressive inflammatory lung disease characterized by increasing breathlessness. It encompasses chronic bronchitis and emphysema, and is primarily caused by long-term exposure to irritating gases or particulate matter, most often from cigarette smoke. Other risk factors include air pollution, occupational dusts, and genetic factors such as alpha-1 antitrypsin deficiency.

Pathophysiology
COPD is characterized by airflow limitation that is not fully reversible. The pathology involves chronic inflammation of the airways, parenchyma, and pulmonary vasculature. Key pathophysiological changes include:

Chronic inflammation: Inflammatory cells such as neutrophils, macrophages, and T lymphocytes infiltrate the airways.
Airway remodeling: Structural changes include mucus gland hypertrophy, epithelial metaplasia, and fibrosis.
Alveolar destruction: Emphysematous changes result in the loss of alveolar walls, leading to decreased surface area for gas exchange.
Clinical Features
Symptoms:

Progressive dyspnea on exertion
Chronic cough with sputum production
Wheezing and chest tightness
Signs:

Hyperinflated chest on physical examination
Decreased breath sounds with prolonged expiration
Use of accessory muscles of respiration
Diagnosis
The diagnosis of COPD is confirmed by spirometry, which demonstrates a post-bronchodilator FEV1/FVC ratio of less than 0.70. Additional diagnostic tools and tests include:

Chest X-ray: To rule out other causes of dyspnea and to assess for hyperinflation.
CT Scan: High-resolution CT scans provide detailed images of the lungs and help in the assessment of emphysematous changes.
Arterial Blood Gas Analysis: Used to assess the severity of hypoxemia and hypercapnia.
Management
Lifestyle Modifications
Smoking Cessation: The most critical intervention to slow the progression of COPD.
Pulmonary Rehabilitation: A comprehensive program including exercise training, education, and behavior change.
Pharmacotherapy
Bronchodilators: Short-acting beta-agonists (SABA) and long-acting beta-agonists (LABA).
Inhaled Corticosteroids (ICS): Used in combination with LABAs for patients with frequent exacerbations.
Phosphodiesterase-4 Inhibitors: Such as roflumilast, for patients with chronic bronchitis and frequent exacerbations.
Oxygen Therapy
Long-term oxygen therapy (LTOT) improves survival in patients with severe COPD and chronic hypoxemia.
Surgical Interventions
Lung Volume Reduction Surgery (LVRS): For patients with severe emphysema.
Lung Transplantation: Considered for select patients with end-stage disease.
Complications
Common complications include:

Respiratory Infections: Increased susceptibility due to impaired lung defense mechanisms.
Cor Pulmonale: Right heart failure secondary to pulmonary hypertension.
Pneumothorax: Particularly in patients with severe bullous disease.
Prognosis
The prognosis of COPD varies widely. Factors influencing prognosis include the severity of airflow limitation, the presence of comorbidities, and the patient’s ability to cease smoking. Early diagnosis and appropriate management can significantly improve quality of life and survival rates.

Conclusion
COPD remains a major global health burden. Advances in our understanding of its pathophysiology and treatment options continue to evolve. Effective management requires a multidisciplinary approach, focusing on patient education, pharmacotherapy, and lifestyle modifications to improve clinical outcomes and enhance the quality of life for patients.


''')
print(response)
