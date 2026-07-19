"""
===========================================
Portfolio AI Chatbot
===========================================
Run:
python chatbot.py
"""
from rag.chain import RAGChain
def main():
    print("=" * 60)
    print("Portfolio AI Chatbot")
    print("Type 'exit' to quit.")
    print("Type 'clear' to clear memory.")
    print("=" * 60)
    chatbot = RAGChain()
    while True:
        question = input("\nYou: ").strip()
        if not question:
            continue
        if question.lower() == "exit":
            print("\nGoodbye!")
            break
        if question.lower() == "clear":
            chatbot.clear_memory()
            print("\nConversation memory cleared.")
            continue
        try:
            result = chatbot.ask(question)
            print("\nAI:")
            print(result["answer"])
            print("\n📚 Referenced From")
            seen = set()
            for source in result["sources"]:
                key = (source["title"], source["category"])
                if key in seen:
                    continue
                seen.add(key)
                print(f"• {source['title']} ({source['category']})")
            else:
                print("No sources found.")
        except Exception as e:
            print(f"\nError: {e}")
if __name__ == "__main__":
    main()