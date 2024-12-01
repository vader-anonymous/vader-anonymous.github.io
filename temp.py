import os
import json

def generate_video_data(captions_file, output_file, base_directory="videos"):
    """
    Reads captions from a text file, checks for the existence of corresponding .mp4 files,
    and generates a JSON file with the desired structure.
    """
    try:
        # # Read the captions from the file
        # with open(captions_file, 'r', encoding='utf-8') as file:
        #     captions = file.readlines()
        
        # # Trim whitespace and remove empty lines
        # captions = [caption.strip() for caption in captions if caption.strip()]

        video_files = os.listdir(f"{base_directory}/flower_a_hps")

        # Generate video data structure
        video_data = []
        for index, video in enumerate(video_files):
            # Define the expected file paths
            aesthetic_path = f"{base_directory}/flower_a_hps/{video}"
            pickscore_path = f"{base_directory}/flower_pick/{video}"
            videocrafter_path = f"{base_directory}/flower_origin/{video}"
            
            # Check if all required files exist
            if os.path.exists(aesthetic_path) and os.path.exists(pickscore_path) and os.path.exists(videocrafter_path):
                # Append the data if all files exist
                video_entry = {
                    "caption": 'A fairy tends to enchanted, glowing flowers.',
                    "aestheticPath": aesthetic_path,
                    "pickscorePath": pickscore_path,
                    "videocrafterPath": videocrafter_path
                }
                video_data.append(video_entry)
            # else:
            #     print(f"Skipping caption: '{caption}' (missing .mp4 files)")

        # Write the video data to a JSON file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(video_data, json_file, indent=4, ensure_ascii=False)
        
        print(f"Video data JSON saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output file paths
captions_file = "captions.txt"  # Input file containing captions
output_file = "diversity_video_data_flower.json"  # Output JSON file

# Generate video data
generate_video_data(captions_file, output_file)