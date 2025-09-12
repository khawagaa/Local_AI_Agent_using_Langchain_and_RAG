from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
you are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}

"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


# question = input("Ask your question (type q to quit): ")
# docs = retriever.invoke(question)   # you're currently using .invoke; keep that
# print("TYPE:", type(docs))
# print("LENGTH:", len(docs))
# for i, d in enumerate(docs, 1):
#     # doc.page_content and doc.metadata are the usual fields
#     print(f"[{i}] TYPE: {type(d)}  ID: {getattr(d,'id', d.metadata.get('id',''))}")
#     print("    preview:", repr(d.page_content[:200]))

while True:
    print("\n\n----------------------------")
    question = input("Ask your question (type q to quit): ")
    print("\n\n----------------------------")
    if question == "q":
        break

    reviews = retriever.invoke(question)
    reviews_text = "\n\n".join([
        f"(ID: {doc.metadata.get('id', doc.id)}, Rating: {doc.metadata.get('rating')}, Date: {doc.metadata.get('date')})\n{doc.page_content}"
        for doc in reviews
    ])

    result = chain.invoke({"reviews":reviews_text, "question": question})
    print(result)