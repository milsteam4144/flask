import panel as pn

# Initialize Panel
pn.extension()

# Create a FileInput widget
file_input = pn.widgets.FileInput(accept='.py')

# Create a layout
layout = pn.Column(
    pn.pane.Markdown("# Python File Uploader"),
    file_input
)

# Display the layout
layout.servable()

# This function executes when the file is uploaded
def handle_upload(event):
    if event.new:
        print(f"File uploaded: {file_input.filename}")
        # To read the content:
        content = file_input.value.decode('utf-8')
        return (content)

file_input.param.watch(handle_upload, 'value')

handle_upload()