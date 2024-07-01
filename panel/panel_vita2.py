import panel as pn

pn.extension()

# Create the file input widget
file_input = pn.widgets.FileInput(accept='.py')

# Create a text area to display the file content
content_display = pn.widgets.TextAreaInput(
    value="No file uploaded yet.",
    height=300,
    width=600,
    disabled=True
)

# Callback function to update the content display
def update_content(event):
    if event.new is None:
        content_display.value = "No file uploaded yet."
    else:
        content_display.value = event.new.decode('utf-8')

# Connect the callback function to the file input
file_input.param.watch(update_content, 'value')

# Create the layout
layout = pn.Column(
    pn.pane.Markdown("# Python File Uploader"),
    pn.Row(
        pn.Column(
            pn.pane.Markdown("## Upload a Python File"),
            file_input
        ),
        pn.Column(
            pn.pane.Markdown("## File Content"),
            content_display
        )
    )
)

# Make the layout servable
layout.servable()