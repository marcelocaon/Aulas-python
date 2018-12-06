import win32com.client as win32

wordApp = win32.gencache.EnsureDispatch('Word.Application') #create a word application object
wordApp.Visible = False # hide the word application
doc = wordApp.Documents.Add() # create a new application

doc.PageSetup.RightMargin = 20
doc.PageSetup.LeftMargin = 20
doc.PageSetup.Orientation = win32.constants.wdOrientLandscape
# a4 paper size: 595x842
doc.PageSetup.PageWidth = 595
doc.PageSetup.PageHeight = 842
header_range= doc.Sections(1).Headers(win32.constants.wdHeaderFooterPrimary).Range
header_range.ParagraphFormat.Alignment = win32.constants.wdAlignParagraphCenter
header_range.Font.Bold = True
header_range.Font.Size = 20
header_range.Text = "Header Of The Document"

total_column = 4
total_row = 5
rng = doc.Range(0,0)
rng.ParagraphFormat.Alignment = win32.constants.wdAlignParagraphCenter
table = doc.Tables.Add(rng,total_row, total_column)
table.Borders.Enable = False
if total_column > 1:
	table.Columns.DistributeWidth()

frame_max_width = 167  # the maximum width of a picture
frame_max_height = 125  # the maximum height of a picture

for index, filename in enumerate(filenames):  # loop through all the files and folders for adding pictures
    if os.path.isfile(
            os.path.join(os.path.abspath("."), filename)):  # check whether the current object is a file or not
        if filename[
           len(filename) - 3: len(filename)].upper() == 'JPG':  # check whether the current object is a JPG file

            # calculating the position of each image to be put into the correct table cell
            cell_column = index % total_column + 1
            cell_row = index / total_column + 1
            print
            'cell_column=%s,cell_row=%s' % (cell_column, cell_row)

            # we are formatting the style of each cell
            cell_range = table.Cell(cell_row, cell_column).Range
            cell_range.ParagraphFormat.LineSpacingRule = win32.constants.wdLineSpaceSingle
            cell_range.ParagraphFormat.SpaceBefore = 0
            cell_range.ParagraphFormat.SpaceAfter = 3

            # this is where we are going to insert the images
            current_pic = cell_range.InlineShapes.AddPicture(os.path.join(os.path.abspath("."), filename))
            width, height = (frame_max_height * width / height, frame_max_height)

            # changing the size of each image to fit the table cell
            current_pic.Height = height
            current_pic.Width = width

            # putting a name underneath each image which can be handy
            table.Cell(cell_row, cell_column).Range.InsertAfter("\n" + filename)