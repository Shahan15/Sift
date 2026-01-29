from extractors.youtube import get_insights
import sys
from utils.input_sanitisation import verify_input


def main():
    print('\n')
    print(f"🚀 SIFT SYSTEM ACTIVE | Researching: \n")

    while True:
        print("Type 'exit' or 'q' to shut down the app.\n")

        video_id = input(f'Please provide the video ID: '.strip())

        if video_id.lower() in ['q','exit']:
            sys.exit()

        if not video_id or not verify_input(video_id):
            continue
        
        print(f"PROCESSING {video_id}...")
        try:
            get_insights(video_id)
            print('---VIDEO PROCESSED---\n')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == "__main__":
    main()  