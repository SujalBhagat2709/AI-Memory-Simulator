from memory_engine import AIMemoryEngine


class MemoryConsole:

    def __init__(self):

        self.engine = AIMemoryEngine()

    def menu(self):

        while True:

            print("\n")

            print("=" * 55)

            print("           AI MEMORY SIMULATOR")

            print("=" * 55)

            print("1. Add Memory")

            print("2. View All Memories")

            print("3. Recall Memory")

            print("4. Forget Memory")

            print("5. View Important Memories")

            print("6. Memory Statistics")

            print("7. Auto Cleanup")

            print("8. Exit")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":

                self.engine.add_memory()

            elif choice == "2":

                self.engine.show_memories()

            elif choice == "3":

                self.engine.recall_memory()

            elif choice == "4":

                try:

                    self.engine.forget_memory()

                except ValueError:

                    print("\nInvalid Memory ID.")

            elif choice == "5":

                self.engine.important_memories()

            elif choice == "6":

                self.engine.statistics()

            elif choice == "7":

                self.engine.auto_cleanup()

            elif choice == "8":

                print("\nThank You For Using AI Memory Simulator!")

                break

            else:

                print("\nInvalid Choice.")


if __name__ == "__main__":

    console = MemoryConsole()

    console.menu()