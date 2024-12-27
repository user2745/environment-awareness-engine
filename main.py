from engines.core_engine import CoreEngine
import os

def run_physical_environment_integration():
    # Initialize Core Engine
    engine = CoreEngine()
    model_path = "model.onnx"  # Replace with your model file path
    labels_path = "labels.txt"  # Replace with your labels file path
    state_file = "environment_state.json"

    try:
        engine.initialize_engine(model_path, labels_path)
        if os.path.exists(state_file):
            engine.load_state(state_file)

        print("Welcome to the Physical Environment Integration System!")
        while True:
            command = input("Enter command (analyze live, analyze video <file>, status, reset, exit): ").strip()

            if command.startswith("analyze live"):
                result = engine.process_live_feed()
                print(f"\nEnvironment Report:\n{result}\n")

            elif command.startswith("analyze video"):
                _, video_path = command.split(maxsplit=1)
                results = engine.process_video(video_path)
                for i, result in enumerate(results):
                    print(f"\nFrame {i+1} Report:\n{result}\n")

            elif command == "status":
                print("System is active and ready to analyze.")

            elif command == "reset":
                engine.close_resources()
                print("System has been reset.")

            elif command == "exit":
                print("Saving system state...")
                engine.save_state(state_file)
                print("Goodbye!")
                break

            else:
                print("Invalid command. Please try again.")

    finally:
        engine.close_resources()
        engine.save_state(state_file)

if __name__ == "__main__":
    run_physical_environment_integration()
