def copy_html_contents(source_file, destination_file):
    try:
        # Read the content from the source HTML file
        with open(source_file, 'r') as source:
            source_content = source.read()

        # Read the content from the destination HTML file
        with open(destination_file, 'r') as destination:
            destination_lines = destination.readlines()

        # Find the line numbers where the <main> tag starts and ends
        main_start_line = None
        main_end_line = None
        for i, line in enumerate(destination_lines):
            if '<main>' in line:
                main_start_line = i
            if '</main>' in line:
                main_end_line = i

        if main_start_line is not None and main_end_line is not None:
            # Remove the old content between <main> tags
            destination_lines = (
                destination_lines[:main_start_line + 1]
                + ['\n']
                + source_content.split('\n')
                + ['\n']
                + destination_lines[main_end_line:]
            )

            # Write the modified content back to the destination HTML file
            with open(destination_file, 'w') as destination:
                destination.writelines(destination_lines)

            print("Contents copied successfully.")
        else:
            print("Destination file does not contain <main> and/or </main> tags.")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    source_file = "utils/scraped_publications.html"  # Replace with your source HTML file's path
    destination_file = "publications.html"  # Replace with your destination HTML file's path

    copy_html_contents(source_file, destination_file)
