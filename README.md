# Vimeo Video Search CLI Tool

This project provides a command-line interface (CLI) tool to search videos on your Vimeo account using the official Vimeo Python SDK. The tool leverages the Vimeo API to search for videos based on a query string and supports pagination to fetch multiple pages of results.

## Features

- **Search Videos**: Search for videos in your Vimeo account by providing a search string.
- **Pagination**: Fetch multiple pages of search results.
- **Environment Configuration**: Securely manage API credentials using a `.env` file.
- **Customizable Results**: Specify the maximum number of results to retrieve.

## Prerequisites

- Python 3.x
- Vimeo API credentials (Access Token)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yashasolutions/vimeosearch.git
   cd vimeosearch
   ```

2. **Install Dependencies**

   Use pip to install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment Variables**

   Create a `.env` file in the project directory with your Vimeo API credentials:

   ```
    # https://developer.vimeo.com/
    # Create an app - set access preferences and generate token
    VIMEO_CLIENT_ID="XXX"
    VIMEO_CLIENT_SECRET="XXX"
    VIMEO_ACCESS_TOKEN="XXXX"
   ```

## Usage

### Command-Line Interface

To search for videos, use the command-line tool as follows:

```bash
python vimeo_search.py "your search query" --max_results 100
```

- **search query**: The string to search for videos.
- `--max_results`: (Optional) Maximum number of videos to fetch. Default is 50.

### Example

```bash
python vimeo_search.py "nature" --max_results 50
```

This command searches for videos containing the word "nature" in your Vimeo account and fetches up to 50 results.

## Output

The tool outputs the search results in JSON format, providing detailed information about each video, including title, files, and more.

## Error Handling

If the API request fails, an error message will be displayed with details about the failure.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Acknowledgments

- [Vimeo API](https://developer.vimeo.com/api/reference) - The official API documentation for Vimeo.
- [vimeo.py](https://github.com/vimeo/vimeo.py) - The official Python library for Vimeo's API.
