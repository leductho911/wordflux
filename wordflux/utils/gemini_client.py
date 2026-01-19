from google import genai
import logging

logger = logging.getLogger(__name__)


class GeminiClientManager:
    """Quản lý Google Gemini API client"""
    
    def __init__(self, gemini_api_key: str):
        """
        Khởi tạo Gemini client
        """

        self.gemini_api_key = gemini_api_key
        if not self.gemini_api_key:
            raise ValueError("Gemini API key not found in config. Please check your config.yaml file.")
        
        self.client = genai.Client(api_key=self.gemini_api_key)
    
    def get_client(self) -> genai.Client:
        """Trả về Gemini client"""
        return self.client
