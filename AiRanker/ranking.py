import numpy as np

def combine_similarities(text_sim, skill_sim, text_weight=0.7, skill_weight=0.3):
    return text_weight * text_sim + skill_weight * skill_sim

def get_top_matches(similarity_matrix, top_n=3):
    top_matches = []
    for i in range(similarity_matrix.shape[0]):
        top_indices = np.argsort(similarity_matrix[i])[::-1][:top_n]
        top_scores = similarity_matrix[i][top_indices]
        top_matches.append(list(zip(top_indices, top_scores)))
    return top_matches
