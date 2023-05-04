# Identifying sub-fields of Business English by clustering text embeddings

This repository shares the content of the research project "Identifying sub-fields of Business English by clustering text embeddings" which 
I've been working on for 6 months and recently published at ISSI 2023. 

## Introduction

Business English is a popular field of English for Specific Purposes (ESP) as it helps non-English speakers better interact with business organizations across the world (Bhatia & Bremner, 2012). Understanding the structure of sub-fields of Business English is essential to improve education materials and contribute to facilitating business communications. This study aims to identify sub-fields of Business English by clustering academic works based on text embeddings. 

We analyzed 3,096 works tagged with the concept “Business English” and classified as “journal-article” in OpenAlex (Priem, Piwowar & Orr, 2022). The data were retrieved on July 7, 2022. In OpenAlex, the only lower-level concept of “Business English” is “English as a lingua franca”, which does not reflect the knowledge structure of Business English and confirms the importance of this study. 

To identify sub-fields of Business English, SPECTER (Cohan et al., 2020), a pre-trained embedding model specialized for scientific texts, was used for converting the concatenation of the title and the abstract of a paper into an embedding vector. The embeddings for all target journal articles were clustered through BERTopic (Grootendorst, 2022) to assign the articles into sub-fields. The sub-fields were labeled by the authors and drawn in a tree map. 


#### References:

Bhatia, V.K. & Bremner, S. (2012). English for Business Communication. Language Teaching, 45(4),410-445. 

Cohan, A., Feldman, S., Beltagy, I., Downey, D., & Weld, D. S. (2020). SPECTER: Document-level representation learning using citation-informed transformers. arXiv:2004.07180. 

Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure. arXiv:2203.05794.

Priem, J., Piwowar, H., & Orr, R. (2022). OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts. ArXiv. https://arxiv.org/abs/2205.01833
