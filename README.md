This is a project on natural language processing. The purpose of this is to create a chatbot using a transformer model. I also apply BERT embeddings to the transformer model to see how the results of the chatbot change somewhat.

The data set used used was a data set related to all inquiries or refunds regarding packages extracted from AIhub's 'purpose conversation data for each purpose', which consists of a json file. 

How to build a dataset: The experimental environment is GeForce RTX 2060 SUPER GPU, which limits learning depending on the size of the data, so only the "refund exchange" dataset is trained.

The total number of data is 1910 QAs.

Question is put in for training of the chatbot, and Answer is put in as the label of the chatbot.

However, one consideration was made while refining the dataset.

If a data set is created by dividing the interactive structure data set only into speakers Q and A, can the model understand the Q&A of the interactive structure data set?

Thus, in preparation for the fact that the desired answers of the chatbot will not all end with a single sentence sequence, Answer's data set was also manufactured in a structure that teaches learning with a training set.
