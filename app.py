# app.py
import gradio as gr
from agent import run_research

# ── UI ────────────────────────────────────────────────────────────────────────
def research_interface(topic, progress=gr.Progress()):
    if not topic.strip():
        return "Please enter a topic to research."

    progress(0.1, desc="Starting research agent...")
    progress(0.4, desc="Searching the web...")
    progress(0.6, desc="Reading sources...")
    progress(0.7, desc="Synthesizing report...")

    report = run_research(topic)

    progress(1.0, desc="Done!")
    return report

# ── Gradio Blocks UI ──────────────────────────────────────────────────────────
with gr.Blocks(
    title="AI Research Agent",
    theme=gr.themes.Soft(),
) as demo:

    gr.Markdown("""
    #  AI Research Agent
    **Powered by LangGraph + Tavily + Gemini**
    
    Enter any topic → Agent searches the web, reads 5 sources, and returns a structured report in under 60 seconds.
    """)

    with gr.Row():
        with gr.Column(scale=3):
            topic_input = gr.Textbox(
                label="Research Topic",
                placeholder="e.g. 'quantum computing breakthroughs 2025' or 'impact of AI on jobs'",
                lines=2,
            )
        with gr.Column(scale=1):
            submit_btn = gr.Button("🚀 Research", variant="primary", size="lg")
            clear_btn = gr.Button("Clear", size="lg")

    # Example topics — makes the demo immediately usable
    gr.Examples(
        examples=[
            ["artificial intelligence in healthcare 2025"],
            ["climate change solutions and carbon capture"],
            ["Python vs JavaScript for backend development"],
            ["electric vehicle market trends"],
            ["blockchain technology use cases beyond crypto"],
        ],
        inputs=topic_input,
        label="Try these examples",
    )

    report_output = gr.Markdown(
        label="Research Report",
        value="Your research report will appear here...",
    )

    # Wire up buttons
    submit_btn.click(
        fn=research_interface,
        inputs=[topic_input],
        outputs=[report_output],
    )

    clear_btn.click(
        fn=lambda: ("", "Your research report will appear here..."),
        outputs=[topic_input, report_output],
    )

    gr.Markdown("""
    ---
    *Built with LangGraph + Tavily Search + Google Gemini 2.5 Flash*
    """)

if __name__ == "__main__":
    demo.launch(share=False)  