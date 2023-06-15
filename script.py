from urllib import request
from zipfile import ZipFile

class ProcessFile:
    # def __init__(self):
    #     self.filename = ""
    
    def file_name_clean(self, file_url):
        url_split = file_url.split("/")
        file_name_zip = url_split[-1]

        print(url_split, file_name_zip)
        return file_name_zip

    def download(self, file_url, file_name):
        request.urlretrieve(file_url, file_name)
    
    def extract_file(self, file_name):
        zip = ZipFile(file_name, "r")
        zip.extractall()
        zip.close()
        extracted_file_name = zip.namelist()[0]
        print("zipfile:::", extracted_file_name)

        return extracted_file_name

    
    def convert_csv_to_json(self, extracted_file_name):
        with open(extracted_file_name, encoding="utf-8") as csv_file:
            with open("file_json", "w", encoding="utf-8") as json_file:
                
                for rows in csv_file:
                    print()



    def main(self, file_url):
        try:
            file_name_zip = self.file_name_clean(file_url)
            
            # self.download(file_url, file_name_zip)
            extracted_file_name = self.extract_file(file_name_zip)

            self.convert_csv_to_json(extracted_file_name)

            

        except Exception as error:
            print("Internal error:", error)
            


if __name__ == "__main__":
    file_url = "https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip"
    process_file = ProcessFile()
    process_file.main(file_url)


