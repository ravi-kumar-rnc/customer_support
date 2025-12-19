import pandas as pd
from langchain_core.documents import Document


class data_converter:
    def __init__(self):
        print("Data Transformation class initialized")
        self.product_data = pd.read_csv("C:\\customer_support\\data\\flipkart_product_review.csv")
        #print(self.product_data.head())

    def data_transformation(self):
        required_columns = self.product_data.columns[1:]  
        pdt_list = []      
        for index, row in self.product_data.iterrows():
            object = {"product_name": row["product_title"],
                      "rating": row["rating"],
                      "summary": row["summary"],
                        "review": row["review"]}
            pdt_list.append(object)
            #print(pdt_list[0])

        docs = []
        for dtls in pdt_list:
            metadata = {"product_name": dtls["product_name"], 
                        "rating": dtls["rating"], 
                        "summary": dtls["summary"]}
            doc = Document(page_content=dtls["review"], metadata=metadata)
            docs.append(doc)
        print(docs[0])
        return docs

if __name__=="__main__":
    data_conv = data_converter()
    data_conv.data_transformation()