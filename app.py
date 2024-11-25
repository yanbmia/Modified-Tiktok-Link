from flask import Flask, request, render_template_string

app = Flask(__name__)

# Function to modify the URL
def modify_url(url):
    split_position = url.find("?_")
    if split_position != -1:
        return url[:split_position + 2]
    return url

# HTML Template for the web interface
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL Modifier</title>
</head>
<body>
    <h1>URL Modifier App</h1>
    <form method="POST" action="/modify_url">
        <label for="url">Enter URL:</label><br><br>
        <input type="text" id="url" name="url" style="width: 50%;" placeholder="Enter a URL" required><br><br>
        <button type="submit">Modify URL</button>
    </form>

    {% if original_url and modified_url %}
        <h2>Results:</h2>
        <p><strong>Original URL:</strong> {{ original_url }}</p>
        <p><strong>Modified URL:</strong> 
            <a href="{{ modified_url }}" target="_blank">{{ modified_url }}</a>
        </p>
    {% endif %}
</body>
</html>
"""

# Home route
@app.route('/', methods=['GET'])
def home():
    return render_template_string(html_template)

# URL modification route
@app.route('/modify_url', methods=['POST'])
def modify_url_page():
    original_url = None
    modified_url = None

    if request.method == 'POST':
        original_url = request.form.get('url')
        if original_url:
            modified_url = modify_url(original_url)

    return render_template_string(html_template, original_url=original_url, modified_url=modified_url)

if __name__ == '__main__':
    app.run(debug=True)