import time
import openai
import gradio as gr

openai.api_key = 'YOUR APIKEY'
messages = []
def chat_with_gpt(input):
    messages.append({"role":"user","content":input})   # 添加 user 回應
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=500,
        temperature=0.5,
        messages=messages
    )
    ai_msg = response.choices[0].message.content.replace('\n','\n')
     # 將輸入的代碼轉換為Markdown格式的代碼塊
    markdown_code = f'<code>{ai_msg}</code>'
    # 將轉換後的Markdown格式代碼塊返回給Gradio Text框元件進行顯示
    messages.append({"role":"assistant","content":ai_msg})   # 添加 ChatGPT 回應
    return markdown_code 
def output_ans(input):
    chat_with_gpt(input)
    

demo = gr.Blocks()
with demo:
    btn = gr.Button(value="Run")
    txt_3 = gr.Textbox(value="", label="input")
    masssrkdown=gr.Markdown(r"股票")
    btn.click(output_ans, inputs=[txt_3], outputs=[masssrkdown])
if __name__ == "__main__":
    demo.launch()