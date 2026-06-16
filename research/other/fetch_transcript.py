from youtube_transcript_api import YouTubeTranscriptApi
import sys

def fetch_transcript(video_id, output_path):
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        text = " ".join([snippet.text for snippet in transcript])
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Saved transcript to {output_path}")
    except Exception as e:
        print(f"Error fetching transcript for {video_id}: {e}")

if __name__ == "__main__":
    video_id = sys.argv[1]
    output_path = sys.argv[2]
    fetch_transcript(video_id, output_path)