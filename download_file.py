import wget

links = ["https://api.mziq.com/mzfilemanager/v2/d/25fdf098-34f5-4608-b7fa-17d60b2de47d/9927d138-016a-6c32-b098-f8e02e52f076?origin=2","https://api.mziq.com/mzfilemanager/v2/d/25fdf098-34f5-4608-b7fa-17d60b2de47d/c4f893be-19ef-2a0a-7b62-b7ed3a1c02a0?origin=2"]

extension = '.pdf'

counter = 1

for link in links:
    file_name = "file" + str(counter) + extension
    wget.download(link, file_name)
    counter += 1