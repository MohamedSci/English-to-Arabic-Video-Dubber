import os



def organize_arabic_article(input_file_path,output_file_path):
    # Read the unorganized article from the text file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        unorganized_article = file.read()
    # Split the unorganized article into paragraphs
    paragraphs = unorganized_article.split('\n\n')
    # Reorganize the paragraphs to form the organized article
    organized_article = ""
    for paragraph in paragraphs:
        if paragraph.strip() != "":
            organized_article += paragraph.strip() + "\n"
            # Write the organized article to a new file
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(organized_article)
                print("Organized article has been written to:", output_file_path)


input_folder_path = "D:\\video_summary\\processing\\Transcripts\\personal_translated"
output_folder_path = "D:\\video_summary\\processing\\Transcripts\\personal_translated_treated"

def main():
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path, exist_ok=True)
        print(f"output_folder_Directory '{output_folder_path}' created successfully.")
        for filenameEx in os.listdir(input_folder_path):        
            if filenameEx.endswith('.txt'):
                 input_file_path= input_folder_path+ "\\"+filenameEx
                 output_file_path= output_folder_path+ "\\"+filenameEx
                 organize_arabic_article(input_file_path,output_file_path)

if __name__ == "__main__":
    main()



