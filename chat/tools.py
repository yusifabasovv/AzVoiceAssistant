import json
from datetime import datetime
from langchain.utilities import GoogleSearchAPIWrapper
from dataclasses import dataclass


@dataclass
class Functions:
    "Functions for gpt function call"

    def search_google(self, input):
        """Search web for any information"""
        search = GoogleSearchAPIWrapper(k=3)
        return json.dumps({"input": input, "answer": search.run(input)[:2000]})

    def get_current_date_and_time(self):
        """Get current or today's date and time."""
        now = datetime.today()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        return json.dumps({"current_date": current_date, "current_time": current_time})
