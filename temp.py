import os
import json

def generate_video_data(captions_file, output_file, base_directory="videos"):
    """
    Reads captions from a text file, checks for the existence of corresponding .mp4 files,
    and generates a JSON file with the desired structure.
    """
    try:
        # Read the captions from the file
        with open(captions_file, 'r', encoding='utf-8') as file:
            captions = file.readlines()
        
        # Trim whitespace and remove empty lines
        captions = [caption.strip() for caption in captions if caption.strip()]

        # Generate video data structure
        video_data = []
        for index, caption in enumerate(captions):
            # Define the expected file paths
            aesthetic_path = f"{base_directory}/1aesthetic_hps/samples/{index:04d}.mp4"
            pickscore_path = f"{base_directory}/1pickscore/samples/{index:04d}.mp4"
            videocrafter_path = f"{base_directory}/1videocrafter/samples/{index:04d}.mp4"
            
            # Check if all required files exist
            if os.path.exists(aesthetic_path) and os.path.exists(pickscore_path) and os.path.exists(videocrafter_path):
                # Append the data if all files exist
                video_entry = {
                    "caption": caption,
                    "aestheticPath": aesthetic_path,
                    "pickscorePath": pickscore_path,
                    "videocrafterPath": videocrafter_path
                }
                video_data.append(video_entry)
            else:
                print(f"Skipping caption: '{caption}' (missing .mp4 files)")

        # Write the video data to a JSON file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(video_data, json_file, indent=4, ensure_ascii=False)
        
        print(f"Video data JSON saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output file paths
captions_file = "captions.txt"  # Input file containing captions
output_file = "video_data.json"  # Output JSON file

# Generate video data
generate_video_data(captions_file, output_file)