from rag import get_answer

def main():
    question = input("Ask Question: ")
    answer = get_answer(question)
    print(answer)

if __name__ == "__main__":
    main()