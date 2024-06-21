# Behavioral Analysis on E-commerce product reviews with LLM

This Python project uses LangChain and OpenAI's GPT-3.5-turbo model to perform behavioral analysis on e-commerce product reviews. The project analyzes reviews to determine sentiment, anger levels, contentment, and extracts key information such as the item and brand. This provides a modular and efficient way to process and gain insights from customer feedback.

## Features

- Sentiment Analysis (Positive, Negative)
- Anger Detection (True, False)
- Contentment Detection (True, False)
- Extraction of Item and Brand Information
- Modular and scalable code structure

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ecommerce_reviews_llm.git
    cd ecommerce_reviews_llm
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key:**
    - Create a `.env` file in the project root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. **Prepare your reviews:**
    - Add your product reviews to the `dress_reviews` list in the `main()` function.

2. **Run the analysis:**
    ```bash
    python main.py
    ```

3. **View the results:**
    - The processed results will be printed to the console as a list of JSON objects.

## Example

```python
dress_reviews = [
    "I had such high hopes for this dress and really wanted it to work for me. i initially ordered the petite small (my usual size) but i found this to be outrageously small...",
    "I'm 5ft 5in and 125 lbs. i ordered the s petite to make sure the length wasn't too long. i typically wear an xs regular in retailer dresses. if you're less busty...",
    # Add more reviews here
]

# Expected Output
[
    {
        "Sentiment": "Negative",
        "Anger": True,
        "Content": False,
        "Item": "Dress",
        "Brand": "Unknown"
    },
    {
        "Sentiment": "Positive",
        "Anger": False,
        "Content": True,
        "Item": "Dress",
        "Brand": "Unknown"
    },
    # More results...
]
