import openai

class OpenAIHelper:
    def __init__(self, api_key):
        self.client = openai(api_key="k-proj-tKRngd9LAihAHRr3ksa4T3BlbkFJ1Rjhpq2o6V1SDAaDERbP")

    def generate_image(self, prompt):
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        return image_url
