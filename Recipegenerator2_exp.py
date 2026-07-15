import gradio as gr
from google import genai

client = genai.Client(api_key="os.environ["GEMINI_API_KEY"]")

def generate_recipe(recipe_name):
    prompt = f"""
    Generate a complete recipe for "{recipe_name}".

    Include:
    1. Recipe Name
    2. Ingredients (with quantities)
    3. Preparation Time
    4. Cooking Time
    5. Servings
    6. Step-by-step Instructions
    7. Cooking Tips
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

demo = gr.Interface(
    fn=generate_recipe,
    inputs=gr.Textbox(
        label="Recipe Name",
        placeholder="Enter a recipe name (e.g., Vegetable Biryani)"
    ),
    outputs=gr.Textbox(
        label="Generated Recipe",
        lines=25
    ),
    title="Recipe Generator",
    description="Enter the name of any recipe to generate its complete cooking instructions."
)

demo.launch()