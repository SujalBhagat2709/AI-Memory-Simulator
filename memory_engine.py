import json
import os
from datetime import datetime


class AIMemoryEngine:

    def __init__(self):

        self.file_name = "memory_store.json"

        self.memories = []

        self.load()

    def load(self):

        if os.path.exists(self.file_name):

            try:

                with open(
                    self.file_name,
                    "r",
                    encoding="utf-8"
                ) as file:

                    self.memories = json.load(file)

            except:

                self.memories = []

    def save(self):

        with open(
            self.file_name,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.memories,
                file,
                indent=4
            )

    def add_memory(self):

        print("\n========== ADD MEMORY ==========\n")

        text = input("Memory: ").strip()

        if text == "":

            print("\nMemory cannot be empty.")
            return

        print("\nPriority")

        print("1. Low")

        print("2. Medium")

        print("3. High")

        choice = input("\nChoose Priority: ")

        priorities = {

            "1": "Low",

            "2": "Medium",

            "3": "High"

        }

        if choice not in priorities:

            print("\nInvalid Choice.")
            return

        memory = {

            "id": len(self.memories) + 1,

            "text": text,

            "priority": priorities[choice],

            "created": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            ),

            "recall_count": 0

        }

        self.memories.append(memory)

        self.save()

        print("\nMemory Saved Successfully.")

    def show_memories(self):

        if not self.memories:

            print("\nNo Memories Found.")
            return

        print("\n========== MEMORY STORE ==========\n")

        for memory in self.memories:

            print("ID :", memory["id"])

            print("Memory :", memory["text"])

            print("Priority :", memory["priority"])

            print("Created :", memory["created"])

            print("Recall Count :", memory["recall_count"])

            print("-" * 50)

    def recall_memory(self):

        if not self.memories:

            print("\nNo Memories Available.")
            return

        keyword = input("\nSearch Keyword: ").lower()

        found = False

        print()

        for memory in self.memories:

            if keyword in memory["text"].lower():

                memory["recall_count"] += 1

                print("ID :", memory["id"])

                print("Memory :", memory["text"])

                print("Priority :", memory["priority"])

                print("Recall Count :", memory["recall_count"])

                print("-" * 40)

                found = True

        if not found:

            print("No Matching Memory Found.")

        self.save()

    def forget_memory(self):

        if not self.memories:

            print("\nNo Memories Available.")
            return

        memory_id = int(input("\nMemory ID: "))

        for memory in self.memories:

            if memory["id"] == memory_id:

                self.memories.remove(memory)

                self.save()

                print("\nMemory Forgotten.")

                return

        print("\nMemory Not Found.")

    def important_memories(self):

        print("\n========== IMPORTANT MEMORIES ==========\n")

        found = False

        for memory in self.memories:

            if memory["priority"] == "High":

                print("ID :", memory["id"])

                print("Memory :", memory["text"])

                print("Recall Count :", memory["recall_count"])

                print("-" * 40)

                found = True

        if not found:

            print("No High Priority Memories.")

    def statistics(self):

        total = len(self.memories)

        high = 0

        medium = 0

        low = 0

        recalls = 0

        for memory in self.memories:

            recalls += memory["recall_count"]

            if memory["priority"] == "High":

                high += 1

            elif memory["priority"] == "Medium":

                medium += 1

            else:

                low += 1

        print("\n========== MEMORY STATISTICS ==========\n")

        print("Total Memories :", total)

        print("High Priority  :", high)

        print("Medium Priority:", medium)

        print("Low Priority   :", low)

        print("Total Recalls  :", recalls)

    def auto_cleanup(self):

        before = len(self.memories)

        self.memories = [

            memory

            for memory in self.memories

            if not (

                memory["priority"] == "Low"

                and

                memory["recall_count"] == 0

            )

        ]

        after = len(self.memories)

        self.save()

        print(

            f"\nRemoved {before-after} unused low priority memories."
        )