# List of extensions we are looking for
extensions = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]

# Map of extensions
extensions_dict = {
    "gif" : "image/gif",
    "jpg" : "image/jpeg",
    "jpeg": "image/jpeg",
    "png" : "image/png",
    "pdf" : "application/pdf",
    "txt" : "text/plain",
    "zip" : "application/zip"
}

def main():
    print(process_File_Name(input("File name: ").strip().lower()))

def process_File_Name(answer):
    answer = answer.split(".")

    if len(answer) > 1 and answer[1] in extensions:
        return  extensions_dict[answer[(len(answer) -1)]]
    else:
        return "application/octet-stream"


main()