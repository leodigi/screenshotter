import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
from PIL import Image

# Function to generate a dummy favicon image
def generate_dummy_favicon():
    img = Image.new('RGB', (16, 16), color = 'white')
    return img

# Function to take full page screenshot using Selenium
def take_screenshot(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure headless mode so browser isn't opened visibly
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    # Set window size to a large number to capture the full page
    driver.set_window_size(1920, 1080)
    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    return screenshot

# Streamlit app
def main():
    st.title("Website Screenshot Generator")

    # Dummy favicon image
    favicon = generate_dummy_favicon()

    # Input URL(s) from user
    urls = st.text_area("Enter URL(s) (separate multiple URLs with new lines):")

    if st.button("Generate Screenshots"):
        urls = urls.split('\n')  # Split URLs by new lines
        for url in urls:
            st.write(f"Generating screenshot for: {url}")
            try:
                screenshot = take_screenshot(url)
                # Display screenshot
                st.image(screenshot, caption=url, use_column_width=True)
            except Exception as e:
                st.write(f"Error generating screenshot for {url}: {e}")

if __name__ == "__main__":
    main()
