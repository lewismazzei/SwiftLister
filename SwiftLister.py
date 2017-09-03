import re
import csv
from tkinter import filedialog
html_file = str(open(<PATH OF DOWNLOADED AUCTIVA HTML>, 'rb').readlines()) #Reads html source code document

titles = list(re.findall(r'<span id="dg_Images__ctl[0-9]*_lbl_ImageName">(.*?)</span></h3>', html_file)) #Finds all titles and puts them into a list
urls = list(re.findall(r'id="dg_Images__ctl[0-9]*_lbl_URL" readonly="readonly" style="width: 264px" value="(.*?)" /></li>', html_file)) #Finds all urls and puts them into a list

unique_titles = list(set(re.findall(r'<span id="dg_Images__ctl[0-9]*_lbl_ImageName">(.*?)</span></h3>', html_file))) #Finds all titles and puts them into a set
unique_urls = list(set(re.findall(r'id="dg_Images__ctl[0-9]*_lbl_URL" readonly="readonly" style="width: 264px" value="(.*?)" /></li>', html_file))) #Finds all urls and puts them into a set

if len(titles) != len(unique_titles) or len(urls) != len(unique_urls): #Checks that the lists and sets have the same number of elements as if duplicates are present the list will have more (sets eliminate dupes)
    title_duplicates_count = len(titles) - len(unique_titles)
    url_duplicates_count = len(urls) - len(unique_urls)
    title_duplicates = []
    url_duplicates = []
    if title_duplicates_count > 0:
        for title in titles:
            if title in unique_titles:
                unique_titles.remove(title)
            else:
                title_duplicates.append(title)
    if url_duplicates_count > 0:
        for url in urls:
            if url in unique_urls:
                unique_urls.remove(url)
            else:
                url_duplicates.append(url)
    program_pause = input('DUPLICATES FOUND (Title Dupes: {}, URL Dupes: {}) [Titles: {}, Urls: {}] - REMOVE DUPES FROM Turbolister_Import.csv AFTER THIS PROCESS (Press <ENTER> to continue)'.format(title_duplicates_count, url_duplicates_count, [title_duplicate for title_duplicate in title_duplicates], [url_duplicate for url_duplicate in url_duplicates])) #Warns user that duplicates must be found and removed manually in csv file

#name_of_file = filedialog.askopenfilename()#Prompts user to select what template they want to use
name_of_file = <PATH OF TURBOLISTER TEMPLATE>

with open(name_of_file, 'r') as f_read_only:
    reader = csv.reader(f_read_only)
    tl_file_template = list(reader) #Makes a list containing both header and first data row

tl_file = tl_file_template[0]  #Makes a list containing just the header
tl_data_row = tl_file_template[1] #Defines a data row
tl_data = tl_file_template[1:] #Makes a list containing the first and all future data rows

with open('Turbolister_Import.csv', 'w', newline='') as f_write_only: #Opens a temporary file that will be imported into TL
    writer = csv.writer(f_write_only)
    writer.writerow(tl_file) #Writes the header information into file
    for row in range(0,len(titles)):
        tl_data.append(tl_data_row) #Adds a data row to the list
        current_row = tl_data[row] #Assigns a temporary variable for the newly appended row
        current_row[3] = titles[row] #Enters the title
        current_row[13] = urls[row] #Enters the URL
        writer.writerow(current_row) #Writes the current row into file