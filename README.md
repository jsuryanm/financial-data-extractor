# Financial Data Extractor

A Python-based web application built with Streamlit and LangChain that extracts and analyzes financial data from various sources. This tool uses LLM's to intelligently process financial information and present it in a structured, easy-to-understand format.

## Features

- **AI-Powered Extraction**: Leverages LangChain and large language models for intelligent data processing
- **Interactive Web Interface**: User-friendly Streamlit dashboard for easy data extraction
- **Automated Data Processing**: Extracts financial metrics and key performance indicators
- **Real-time Analysis**: Process and visualize financial data instantly
- **Clean Data Output**: Structured and formatted financial information
- **Modular Architecture**: Separation of data extraction logic and UI components

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.12 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jsuryanm/financial-data-extractor.git
   cd financial-data-extractor
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys** (if using LLM providers)
   
   Create a `.env` file in the project root or set environment variables:
   ```bash
   # Example for OpenAI
   OPENAI_API_KEY=your_api_key_here
   
   # Or other LLM providers as configured
   ```

## Usage

### Running the Application

Launch the Streamlit web application:

```bash
streamlit run streamlit.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Data Extractor Module

You can also use the data extraction functionality directly in your Python scripts:

```python
from data_extractor import extract_financial_data

# Your implementation here
```

## Project Structure

```
financial-data-extractor/
├── data_extractor.py    # Core data extraction logic
├── streamlit.py         # Streamlit web application
├── requirements.txt     # Python dependencies
├── LICENSE             # MIT License
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## Components

### `data_extractor.py`
Contains the core functionality for extracting and processing financial data.

### `streamlit.py`
Implements the web interface using Streamlit framework, providing an interactive dashboard for users.

## Dependencies

The project uses the following Python packages (see `requirements.txt` for specific versions):
- **streamlit** - Web application framework
- **langchain** - Framework for developing applications powered by language models
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- Additional packages as specified in requirements.txt

## How It Works

1. **Input**: Users provide financial data or documents through the web interface
2. **AI Processing**: LangChain processes the data using language models to extract relevant financial information
3. **Validation**: The data extractor module validates and structures the extracted information
4. **Output**: Results are displayed in a structured format with visualizations

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Jayasuryan Mutyala**
- GitHub: [@jsuryanm](https://github.com/jsuryanm)

## Acknowledgments

- Thanks to the Streamlit community for the excellent framework
- LangChain for providing powerful tools for building LLM applications
- Open source contributors who inspire continuous learning

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for similar problems

## Roadmap

Future enhancements planned:
- [ ] Support for multiple data sources
- [ ] Advanced visualization options
- [ ] Export functionality (CSV, Excel, PDF)
- [ ] Historical data comparison
- [ ] API integration for real-time data

## Disclaimer

This tool is for educational and research purposes. Always verify financial data from official sources before making any financial decisions.

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!
