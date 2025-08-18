import gradio as gr
import os
from datetime import datetime

POST_FILE = "posts.txt"

# Load posts
if os.path.exists(POST_FILE):
    with open(POST_FILE, "r", encoding="utf-8") as f:
        posts = f.read().split("\n\n")
else:
    posts = []

def add_post(name, location, note, photo):
    if not name or not location:
        return "⚠️ Please enter both plant name and location!", "\n\n".join(posts)

    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    post = f"🌱 {name}\n📍 {location}\n📝 {note}\n📅 {date}"

    # Save photo if uploaded
    if photo:
        photo_path = f"photo_{len(posts)}.png"
        photo.save(photo_path)
        post += f"\n📸 Saved as {photo_path}"

    posts.append(post)

    # Save all posts
    with open(POST_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(posts))

    return "✅ Post added!", "\n\n".join(posts)

demo = gr.Interface(
    fn=add_post,
    inputs=[
        gr.Textbox(label="🌱 Plant Name"),
        gr.Textbox(label="📍 Location"),
        gr.Textbox(label="📝 Note (optional)"),
        gr.Image(type="pil", label="📸 Upload Plant Photo (optional)")
    ],
    outputs=[
        gr.Textbox(label="Status"),
        gr.Textbox(label="🌍 Community Feed", lines=15)
    ],
    title="EcoMind AI 🌳 Community Plant Tracker",
    description="Post your plants with notes + photos🌱"
)

demo.launch()
