
import os
from dotenv import load_dotenv
from mem0 import MemoryClient
from google import genai

# 1. Load API keys
load_dotenv()

MEM0_API_KEY = os.getenv("MEM0_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not MEM0_API_KEY or not GEMINI_API_KEY:
    raise ValueError(
        "Check that both API keys are present in your .env file."
    )

# 2. Connect to Mem0 and Gemini
memory = MemoryClient(api_key=MEM0_API_KEY)
gemini = genai.Client(api_key=GEMINI_API_KEY)

USER_ID = "student_demo_001"


def save_memory():
    text = input("What should I remember? ").strip()

    if not text:
        print("Please enter something to remember.")
        return

    memory.add(
        [{"role": "user", "content": text}],
        user_id=USER_ID
    )
    print("Memory submitted to Mem0!")


def ask_question():
    question = input("Ask your question: ").strip()

    if not question:
        print("Please enter a question.")
        return

    # 3. Search Mem0 for relevant information
    results = memory.search(
        query=question,
        filters={"user_id": USER_ID}
    )

    # 4. Extract and display retrieved memories
    memories = results.get("results", [])

    print("\n--- Retrieved Memories ---")
    memory_texts = []

    for item in memories:
        saved_text = item.get("memory", "").strip()

        if saved_text:
            memory_texts.append(saved_text)
            print("-", saved_text)

    if memory_texts:
        memory_context = "\n".join(memory_texts)
    else:
        memory_context = "No relevant saved memories were found."
        print("No relevant memories found.")

    # 5. Ask Gemini to answer using retrieved context
    prompt = f"""
You are a helpful personal AI memory assistant.

Use the saved memories below when they are relevant.
Do not invent personal facts. If the memories do not
contain the answer, say that you do not know from the
saved information.

Saved memories:
{memory_context}

User's question:
{question}
"""

    response = gemini.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    print("\nAssistant:", response.text)


def view_all_memories():
    print("\n--- Your Saved Memories ---")

    result = memory.get_all(user_id=USER_ID)

    memories = result.get("results", [])

    if not memories:
        print("No saved memories found.")
        return

    for index, item in enumerate(memories, start=1):
        saved_text = item.get("memory", "")

        if saved_text:
            print(f"{index}. {saved_text}")

def main():
    while True:
        print("\n===== AI MEMORY ASSISTANT =====")
        print("1. Save a memory")
        print("2. Ask a question")
        print("3. view all memories")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            save_memory()
        elif choice == "2":
            ask_question()
        elif choice == "3":
            view_all_memories()
        elif choice == "4":
            print("goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
