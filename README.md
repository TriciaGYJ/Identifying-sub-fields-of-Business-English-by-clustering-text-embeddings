# Research-project

This paper is published at ISSI 2023. The topic is "Identifying sub-fields of Business English by clustering text embeddings". 


# Introduction
Business English is a popular field of English for Specific Purposes (ESP) as it helps non-English speakers better interact with business organizations across the world (Bhatia & Bremner, 2012). Understanding the structure of sub-fields of Business English is essential to improve education materials and contribute to facilitating business communications. This study aims to identify sub-fields of Business English by clustering academic works based on text embeddings. 

We analyzed 3,096 works tagged with the concept “Business English” and classified as “journal-article” in OpenAlex (Priem, Piwowar & Orr, 2022). The data were retrieved on July 7, 2022. In OpenAlex, the only lower-level concept of “Business English” is “English as a lingua franca”, which does not reflect the knowledge structure of Business English and confirms the importance of this study. 
To identify sub-fields of Business English, SPECTER (Cohan et al., 2020), a pre-trained embedding model specialized for scientific texts, was used for converting the concatenation of the title and the abstract of a paper into an embedding vector. The embeddings for all target journal articles were clustered through BERTopic (Grootendorst, 2022) to assign the articles into sub-fields. The sub-fields were labeled by the authors and drawn in a tree map. 
