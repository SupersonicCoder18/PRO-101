import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = '84Bm-Aft9fUAAAAAAAAAAbz_eMV2RWYMeRqbcOvPO6pyRe4QsJ50f5k_dwQ3mMAg'
    transfer_data = TransferData(access_token)

    file_from = input("Enter the path of the file")
    file_to = input("Enter the full path to upload to dropbox")

    transfer_data.upload_file(file_from, file_to)
    print("File has been moved")

main()