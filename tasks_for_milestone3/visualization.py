import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_heatmap(similarity_matrix, resume_skills, jd_skills):
    df = pd.DataFrame(similarity_matrix, index=resume_skills, columns=jd_skills)
    sns.heatmap(df, annot=True, cmap="YlGnBu")
    plt.xlabel("Job Description Skills")
    plt.ylabel("Resume Skills")
    plt.title("Skill Similarity Heatmap")
    plt.show()
